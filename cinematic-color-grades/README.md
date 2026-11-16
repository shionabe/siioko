# cinematic-color-grades｜カラーグレーディング34種（Claude のスキル＋LUT）

画像や動画に、映画のような色をかける Claude のスキルです。34種の LUT（.cube）を同梱しています。
生成ではなく色を「かける」だけなので、**クレジットはかかりません**。

## できること
- 画像や動画を Claude に入れて `/teal-and-orange` のようなコマンドを送ると、LUT をかけたファイルと、元との見比べが返ってきます
- 色見本（映画のひとコマなど）を渡すと、近い LUT を選んでくれます
- 強さ（50%・75% など）も変えられます

## 入れ方
- **claude.ai**：`cinematic-color-grades.skill` をダウンロード → 設定 → 機能（Skills）→ スキルを追加 → アップロード
- **Claude Code**：`cinematic-color-grades` フォルダを `~/.claude/skills/` に置く

## LUT だけ使いたい方へ
`cinematic-color-grades_LUT34.zip` に .cube が34個入っています。Premiere・DaVinci Resolve・Final Cut Pro・Filmora・CapCut などで読み込めます。

## 注意
- LUT は撮った絵の色を変えるだけで、光の向きや影は作れません。光は生成のときに決めます（光のスキル：cinematic-lighting）
- 動画にかけるには ffmpeg が要ります

## ライセンス
MIT
