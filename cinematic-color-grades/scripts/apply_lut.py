#!/usr/bin/env python3
"""画像・動画に 3D LUT（.cube）をかけるスクリプト。

使い方の例:
  python3 apply_lut.py 入力.png 出力.png --lut teal-and-orange
  python3 apply_lut.py 入力.jpg 出力.jpg --lut 02 --strength 0.75 --compare 比較.jpg
  python3 apply_lut.py 入力.mp4 出力.mp4 --lut bleach-bypass
  python3 apply_lut.py --list

--lut には、.cube のパス・番号（02）・名前（teal-and-orange）のどれでも書けます。
画像には numpy と Pillow が要ります。動画には ffmpeg が要ります。
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
LUT_DIR = os.path.join(os.path.dirname(HERE), "luts")
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".bmp"}
VIDEO_EXT = {".mp4", ".mov", ".m4v", ".mkv", ".webm", ".avi"}


def list_luts():
    return sorted(f for f in os.listdir(LUT_DIR) if f.endswith(".cube"))


def find_lut(key):
    """パス・番号・名前から .cube のパスを探す。"""
    if os.path.isfile(key):
        return key
    k = key.strip().lstrip("/").lower().replace("_", "-").replace(" ", "-")
    k = k[:-5] if k.endswith(".cube") else k
    for f in list_luts():
        stem = f[:-5]
        num, name = stem.split("_", 1)
        if k in (stem, name) or (k.isdigit() and int(k) == int(num)):
            return os.path.join(LUT_DIR, f)
    sys.exit(f"LUT が見つかりません: {key}\n--list で一覧を出せます。")


def load_cube(path):
    """.cube を読み、(N, N, N, 3) の表を [青][緑][赤] の順で返す。"""
    size, dmin, dmax, rows = None, [0.0] * 3, [1.0] * 3, []
    with open(path, encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            word = line.split()[0].upper()
            if word == "LUT_3D_SIZE":
                size = int(line.split()[1])
            elif word == "DOMAIN_MIN":
                dmin = [float(v) for v in line.split()[1:4]]
            elif word == "DOMAIN_MAX":
                dmax = [float(v) for v in line.split()[1:4]]
            elif word == "LUT_1D_SIZE":
                sys.exit("1D LUT には対応していません。3D LUT を使ってください。")
            elif word[0].isdigit() or word[0] in "-.":
                rows.append([float(v) for v in line.split()[:3]])
    import numpy as np
    if size is None or len(rows) != size ** 3:
        sys.exit(f".cube の中身が正しくありません: {path}")
    table = np.asarray(rows, dtype=np.float32).reshape(size, size, size, 3)
    return table, np.asarray(dmin, np.float32), np.asarray(dmax, np.float32)


def apply_table(rgb, table, dmin, dmax):
    """rgb（0〜1 の float 配列 H×W×3）に三線形補間で LUT をかける。"""
    import numpy as np
    n = table.shape[0]
    x = (rgb - dmin) / (dmax - dmin)
    x = np.clip(x, 0.0, 1.0) * (n - 1)
    i0 = np.floor(x).astype(np.int32)
    i0 = np.minimum(i0, n - 2)
    f = x - i0
    r0, g0, b0 = i0[..., 0], i0[..., 1], i0[..., 2]
    fr, fg, fb = f[..., 0:1], f[..., 1:2], f[..., 2:3]
    out = 0
    for db, wb in ((0, 1 - fb), (1, fb)):
        for dg, wg in ((0, 1 - fg), (1, fg)):
            for dr, wr in ((0, 1 - fr), (1, fr)):
                out = out + table[b0 + db, g0 + dg, r0 + dr] * (wb * wg * wr)
    return np.clip(out, 0.0, 1.0)


def grade_image(src, dst, lut_path, strength):
    import numpy as np
    from PIL import Image
    im = Image.open(src)
    alpha = im.getchannel("A") if im.mode in ("RGBA", "LA") else None
    rgb = np.asarray(im.convert("RGB"), dtype=np.float32) / 255.0
    table, dmin, dmax = load_cube(lut_path)
    graded = apply_table(rgb, table, dmin, dmax)
    mixed = rgb * (1 - strength) + graded * strength
    out = Image.fromarray((mixed * 255 + 0.5).astype(np.uint8))
    if alpha is not None and not dst.lower().endswith((".jpg", ".jpeg")):
        out.putalpha(alpha)
    save_kw = {"quality": 95} if dst.lower().endswith((".jpg", ".jpeg", ".webp")) else {}
    out.save(dst, **save_kw)
    return im.convert("RGB"), out.convert("RGB")


def make_compare(before, after, path, max_width=2400):
    """左に元、右に色補正後を並べた画像を作る。間に細い白い線。"""
    from PIL import Image, ImageDraw, ImageFont
    w, h = before.size
    line = max(2, w // 400)
    sheet = Image.new("RGB", (w * 2 + line, h), "white")
    sheet.paste(before, (0, 0))
    sheet.paste(after, (w + line, 0))
    d = ImageDraw.Draw(sheet)
    size = max(14, w // 40)
    try:
        font = ImageFont.load_default(size=size)
    except TypeError:  # 古い Pillow
        font = ImageFont.load_default()
    pad = size // 2
    for x, label in ((pad, "Before"), (w + line + pad, "After")):
        box = d.textbbox((x + pad, pad * 2), label, font=font)
        d.rectangle([box[0] - pad, box[1] - pad, box[2] + pad, box[3] + pad], fill=(0, 0, 0))
        d.text((x + pad, pad * 2), label, fill=(255, 255, 255), font=font)
    if sheet.width > max_width:
        sheet = sheet.resize((max_width, round(sheet.height * max_width / sheet.width)))
    sheet.save(path, quality=92)


def grade_video(src, dst, lut_path, strength):
    if shutil.which("ffmpeg") is None:
        sys.exit("ffmpeg が見つからないため、動画には色補正をかけられません。\n"
                 "ffmpeg を入れるか、動画の1コマを画像にして試してください。\n"
                 "（.cube を編集アプリに読み込めば、動画にもそのまま使えます）")
    tmp = tempfile.mkdtemp()
    shutil.copy(lut_path, os.path.join(tmp, "lut.cube"))  # パスの記号でつまずかないように
    if strength >= 0.999:
        vf = "lut3d=file=lut.cube"
    else:
        vf = (f"split[a][b];[b]lut3d=file=lut.cube[g];"
              f"[g][a]blend=all_mode=normal:all_opacity={strength:.3f}")
    cmd = ["ffmpeg", "-y", "-i", os.path.abspath(src), "-vf", vf,
           "-map", "0:v:0", "-map", "0:a?", "-c:v", "libx264", "-crf", "18",
           "-pix_fmt", "yuv420p", "-c:a", "copy", os.path.abspath(dst)]
    try:
        subprocess.run(cmd, cwd=tmp, check=True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    p = argparse.ArgumentParser(description="画像・動画に 3D LUT（.cube）をかけます。")
    p.add_argument("input", nargs="?")
    p.add_argument("output", nargs="?")
    p.add_argument("--lut", help=".cube のパス・番号・名前")
    p.add_argument("--strength", type=float, default=1.0, help="かける強さ 0〜1（初期値 1）")
    p.add_argument("--compare", help="ビフォー・アフターの比較画像の保存先（画像のみ）")
    p.add_argument("--list", action="store_true", help="入っている LUT の一覧を出す")
    a = p.parse_args()

    if a.list:
        print("\n".join(list_luts()))
        return
    if not (a.input and a.output and a.lut):
        p.error("入力・出力・--lut を指定してください。")
    strength = min(max(a.strength, 0.0), 1.0)
    lut_path = find_lut(a.lut)
    ext = os.path.splitext(a.input)[1].lower()

    if ext in VIDEO_EXT:
        grade_video(a.input, a.output, lut_path, strength)
        if a.compare:
            print("比較画像は画像のときだけ作ります。")
    elif ext in IMAGE_EXT:
        if os.path.splitext(a.output)[1].lower() not in IMAGE_EXT:
            sys.exit("画像を入れたときは、出力も画像（.png や .jpg）にしてください。")
        before, after = grade_image(a.input, a.output, lut_path, strength)
        if a.compare:
            make_compare(before, after, a.compare)
            print(f"比較画像: {a.compare}")
    else:
        sys.exit(f"この形式には対応していません: {ext}")
    print(f"できました: {a.output}（LUT: {os.path.basename(lut_path)}、強さ {strength:.0%}）")


if __name__ == "__main__":
    main()
