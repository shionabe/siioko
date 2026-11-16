---
name: cinematic-color-grades
description: 画像や動画に、映画のような色（カラーグレーディング）を LUT でかけるスキル。62種の LUT（ティール＆オレンジ・銀残し・テクニカラー・スプリットトーン・フィルムプリント・70年代ビンテージなどの色の型34種と、『真珠の耳飾りの少女』『グランド・ブダペスト・ホテル』『アメリ』など映画の色28種）を同梱し、スクリプトでかけて、元との見比べも返す。クレジットはかからない。「カラーグレーディング」「色補正」「LUT」「映画っぽい色」「ルック」「この色にしたい」「色見本」と言われたとき、62種の名前や映画の名前が出たとき、`/teal-and-orange` `/bleach-bypass` のような色のコマンドが送られたときは、必ずこのスキルを使う。
---

# cinematic-color-grades｜映画の色を LUT でかける

## 進め方
1. **ファイルを受け取る**：画像（png・jpg など）か動画（mp4・mov など）。
2. **色を決める**
   - コマンド（例 `/teal-and-orange`）や名前・番号が来たら、その LUT を使う（`references/grades.md`）。
   - 色見本（映画のひとコマ・配色の画像）を渡されて「この色に」と言われたら、見本の明暗・影の色・明るい所の色・鮮やかさを言葉にして、近い LUT を1〜3個選び、理由を1行ずつ書いて選んでもらう。
3. **かける**：
   ```
   python3 scripts/apply_lut.py 入力 出力 --lut <番号か名前> --strength 1.0 --compare 比較.jpg
   ```
   - 画像には numpy と Pillow、動画には ffmpeg が要ります。ffmpeg がない環境では、動画はできないと伝え、.cube を編集アプリで使う方法を案内する。
4. **返す**：色をかけたファイル＋元との見比べ（画像のとき）。強すぎたら「50%・75% でもかけられます」と伝える。

## 映画の色は3つでできている
1. **物の色**（壁が赤い・服が緑）：生成のときに言葉で書く
2. **光**（夕方・ランプが1つだけ）：生成のときに言葉で書く
3. **色補正**（全体の色合い）：最後に LUT でかける

色見本の画像をそのまま AI に渡して「この色にして」と頼むと、上から1色で塗ったような絵になりがちです。1と2は言葉で書き、3はこのスキルの LUT で分けてかけるのがコツです。

物の色と光を言葉で書くときの型（英語）：
```
Keep the same person, pose, framing and camera position. OBJECT COLORS: the walls are deep brick red, the curtains are olive green, the dress is mustard yellow. LIGHT: early evening, only the desk lamp is on, warm light from frame-right, the rest of the room falls into soft shadow.
```

## LUT は光を作れない
LUT は撮った絵の色を変えるだけです。光の向きや影の形は変わりません。光を変えたいときは、生成のときに光を書きます（光のスキル：cinematic-lighting）。

## コマンドの一覧（62種）
| # | コマンド | 色 | 日本語 |
|---|---|---|---|
| 1 | `/high-key-airy` | High-Key Airy | ハイキー・エアリー |
| 2 | `/teal-and-orange` | Teal and Orange | ティール＆オレンジ |
| 3 | `/bleach-bypass` | Bleach Bypass | 銀残し |
| 4 | `/cross-processed` | Cross-Processed | クロス・プロセス |
| 5 | `/desaturated` | Desaturated | デサチュレート |
| 6 | `/technicolor` | Technicolor | テクニカラー |
| 7 | `/duotone` | Duotone | デュオトーン |
| 8 | `/red-wash` | Red Wash | レッド・ウォッシュ |
| 9 | `/hyper-saturated` | Hyper-Saturated | ハイパーサチュレート |
| 10 | `/colour-negative` | Colour Negative | カラー・ネガ |
| 11 | `/pastel` | Pastel | パステル |
| 12 | `/warm-amber` | Warm Amber | ウォーム・アンバー |
| 13 | `/cool-blue` | Cool Blue | クール・ブルー |
| 14 | `/matrix-green` | Matrix Green | マトリックス・グリーン |
| 15 | `/yellow-tint` | Yellow Tint | イエロー・ティント |
| 16 | `/magenta-wash` | Magenta Wash | マゼンタ・ウォッシュ |
| 17 | `/complementary-palette` | Complementary Palette | 補色の配色 |
| 18 | `/analogous-palette` | Analogous Palette | 類似色の配色 |
| 19 | `/monochromatic-palette` | Monochromatic Palette | 単色の配色 |
| 20 | `/split-toning` | Split Toning | スプリット・トーン |
| 21 | `/crushed-blacks` | Crushed Blacks | クラッシュド・ブラック |
| 22 | `/lifted-blacks` | Lifted Blacks | リフテッド・ブラック |
| 23 | `/print-film-emulation` | Print Film Emulation | フィルム・プリント |
| 24 | `/kodachrome` | Kodachrome | コダクローム |
| 25 | `/fuji-greens` | Fuji Greens | フジ・グリーン |
| 26 | `/day-for-night` | Day-for-Night | デイ・フォー・ナイト |
| 27 | `/infrared` | Infrared | インフラレッド |
| 28 | `/neon-noir` | Neon Noir | ネオン・ノワール |
| 29 | `/1970s-vintage` | 1970s Vintage | 70年代ビンテージ |
| 30 | `/night-vision` | Night Vision | ナイト・ビジョン |
| 31 | `/sickly-green-yellow` | Sickly Green-Yellow | シックリー・グリーンイエロー |
| 32 | `/thermal` | Thermal | サーマル |
| 33 | `/earth-tones` | Earth Tones | アースカラー |
| 34 | `/blown-out-highlights` | Blown-Out Highlights | ブロウンアウト・ハイライト |
| 35 | `/pearl-earring` | Girl with a Pearl Earring | 真珠の耳飾りの少女 |
| 36 | `/lady-on-fire` | Portrait of a Lady on Fire | 燃ゆる女の肖像 |
| 37 | `/tulip-fever` | Tulip Fever | チューリップ・フィーバー |
| 38 | `/eternitys-gate` | At Eternity's Gate | 永遠の門 ゴッホの見た未来 |
| 39 | `/danish-girl` | The Danish Girl | リリーのすべて |
| 40 | `/ophelia` | Ophelia | オフィーリア |
| 41 | `/marie-antoinette` | Marie Antoinette | マリー・アントワネット |
| 42 | `/the-favourite` | The Favourite | 女王陛下のお気に入り |
| 43 | `/barry-lyndon` | Barry Lyndon | バリー・リンドン |
| 44 | `/amadeus` | Amadeus | アマデウス |
| 45 | `/anna-karenina` | Anna Karenina | アンナ・カレーニナ |
| 46 | `/emma` | Emma. | EMMA エマ |
| 47 | `/jeanne-du-barry` | Jeanne du Barry | ジャンヌ・デュ・バリー |
| 48 | `/the-duchess` | The Duchess | ある公爵夫人の生涯 |
| 49 | `/crimson-peak` | Crimson Peak | クリムゾン・ピーク |
| 50 | `/pans-labyrinth` | Pan's Labyrinth | パンズ・ラビリンス |
| 51 | `/shape-of-water` | The Shape of Water | シェイプ・オブ・ウォーター |
| 52 | `/the-illusionist` | The Illusionist | 幻影師アイゼンハイム |
| 53 | `/stardust` | Stardust | スターダスト |
| 54 | `/azkaban` | Harry Potter and the Prisoner of Azkaban | ハリー・ポッターとアズカバンの囚人 |
| 55 | `/grand-budapest` | The Grand Budapest Hotel | グランド・ブダペスト・ホテル |
| 56 | `/amelie` | Amélie | アメリ |
| 57 | `/pride-and-prejudice` | Pride & Prejudice | プライドと偏見 |
| 58 | `/atonement` | Atonement | つぐない |
| 59 | `/little-women` | Little Women | ストーリー・オブ・マイライフ／わたしの若草物語 |
| 60 | `/jane-eyre` | Jane Eyre | ジェーン・エア |
| 61 | `/midnight-in-paris` | Midnight in Paris | ミッドナイト・イン・パリ |
| 62 | `/chocolat` | Chocolat | ショコラ |
