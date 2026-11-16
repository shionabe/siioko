# 色補正の34種（LUT つき）

- 使い方：コマンド（例 `/teal-and-orange`）か名前で指定されたら、`scripts/apply_lut.py --lut <番号か名前>` でかけます。
- LUT は撮った絵の色を変えるだけです。光の向きや影は作れません（光は生成のときに決めます）。

| # | 名前 | コマンド | LUT |
|---|---|---|---|
| 1 | High-Key Airy（ハイキー・エアリー） | `/high-key-airy` | `luts/01_high-key-airy.cube` |
| 2 | Teal and Orange（ティール＆オレンジ） | `/teal-and-orange` | `luts/02_teal-and-orange.cube` |
| 3 | Bleach Bypass（銀残し） | `/bleach-bypass` | `luts/03_bleach-bypass.cube` |
| 4 | Cross-Processed（クロス・プロセス） | `/cross-processed` | `luts/04_cross-processed.cube` |
| 5 | Desaturated（デサチュレート） | `/desaturated` | `luts/05_desaturated.cube` |
| 6 | Technicolor（テクニカラー） | `/technicolor` | `luts/06_technicolor.cube` |
| 7 | Duotone（デュオトーン） | `/duotone` | `luts/07_duotone.cube` |
| 8 | Red Wash（レッド・ウォッシュ） | `/red-wash` | `luts/08_red-wash.cube` |
| 9 | Hyper-Saturated（ハイパーサチュレート） | `/hyper-saturated` | `luts/09_hyper-saturated.cube` |
| 10 | Colour Negative（カラー・ネガ） | `/colour-negative` | `luts/10_colour-negative.cube` |
| 11 | Pastel（パステル） | `/pastel` | `luts/11_pastel.cube` |
| 12 | Warm Amber（ウォーム・アンバー） | `/warm-amber` | `luts/12_warm-amber.cube` |
| 13 | Cool Blue（クール・ブルー） | `/cool-blue` | `luts/13_cool-blue.cube` |
| 14 | Matrix Green（マトリックス・グリーン） | `/matrix-green` | `luts/14_matrix-green.cube` |
| 15 | Yellow Tint（イエロー・ティント） | `/yellow-tint` | `luts/15_yellow-tint.cube` |
| 16 | Magenta Wash（マゼンタ・ウォッシュ） | `/magenta-wash` | `luts/16_magenta-wash.cube` |
| 17 | Complementary Palette（補色の配色） | `/complementary-palette` | `luts/17_complementary-palette.cube` |
| 18 | Analogous Palette（類似色の配色） | `/analogous-palette` | `luts/18_analogous-palette.cube` |
| 19 | Monochromatic Palette（単色の配色） | `/monochromatic-palette` | `luts/19_monochromatic-palette.cube` |
| 20 | Split Toning（スプリット・トーン） | `/split-toning` | `luts/20_split-toning.cube` |
| 21 | Crushed Blacks（クラッシュド・ブラック） | `/crushed-blacks` | `luts/21_crushed-blacks.cube` |
| 22 | Lifted Blacks（リフテッド・ブラック） | `/lifted-blacks` | `luts/22_lifted-blacks.cube` |
| 23 | Print Film Emulation（フィルム・プリント） | `/print-film-emulation` | `luts/23_print-film-emulation.cube` |
| 24 | Kodachrome（コダクローム） | `/kodachrome` | `luts/24_kodachrome.cube` |
| 25 | Fuji Greens（フジ・グリーン） | `/fuji-greens` | `luts/25_fuji-greens.cube` |
| 26 | Day-for-Night（デイ・フォー・ナイト） | `/day-for-night` | `luts/26_day-for-night.cube` |
| 27 | Infrared（インフラレッド） | `/infrared` | `luts/27_infrared.cube` |
| 28 | Neon Noir（ネオン・ノワール） | `/neon-noir` | `luts/28_neon-noir.cube` |
| 29 | 1970s Vintage（70年代ビンテージ） | `/1970s-vintage` | `luts/29_1970s-vintage.cube` |
| 30 | Night Vision（ナイト・ビジョン） | `/night-vision` | `luts/30_night-vision.cube` |
| 31 | Sickly Green-Yellow（シックリー・グリーンイエロー） | `/sickly-green-yellow` | `luts/31_sickly-green-yellow.cube` |
| 32 | Thermal（サーマル） | `/thermal` | `luts/32_thermal.cube` |
| 33 | Earth Tones（アースカラー） | `/earth-tones` | `luts/33_earth-tones.cube` |
| 34 | Blown-Out Highlights（ブロウンアウト・ハイライト） | `/blown-out-highlights` | `luts/34_blown-out-highlights.cube` |

---

### 1. High-Key Airy｜ハイキー・エアリー
- コマンド：`/high-key-airy`
- LUT：`luts/01_high-key-airy.cube`
- どんな色か：全体が明るく、影もうすい。白っぽくふんわりした色です。
- どんな場面に：朝の部屋・広告・やさしい日常の場面に。

### 2. Teal and Orange｜ティール＆オレンジ
- コマンド：`/teal-and-orange`
- LUT：`luts/02_teal-and-orange.cube`
- どんな色か：肌はあたたかいオレンジ、影は青緑に寄せます。
- どんな場面に：映画らしさを手早く出したいとき。アクションや街の場面に。

### 3. Bleach Bypass｜銀残し
- コマンド：`/bleach-bypass`
- LUT：`luts/03_bleach-bypass.cube`
- どんな色か：色がうすく、明暗のコントラストが強い。ざらっとした重い色です。
- どんな場面に：戦い・事件・重い空気の場面に。

### 4. Cross-Processed｜クロス・プロセス
- コマンド：`/cross-processed`
- LUT：`luts/04_cross-processed.cube`
- どんな色か：色がずれて、明るい所が黄緑っぽくなります。
- どんな場面に：ミュージックビデオ・ふしぎな場面・90年代の雰囲気に。

### 5. Desaturated｜デサチュレート
- コマンド：`/desaturated`
- LUT：`luts/05_desaturated.cube`
- どんな色か：色をほとんど抜いて、灰色に近づけます。
- どんな場面に：さびしい・まじめ・重い話の場面に。

### 6. Technicolor｜テクニカラー
- コマンド：`/technicolor`
- LUT：`luts/06_technicolor.cube`
- どんな色か：赤や青がこってり出る、昔のハリウッド映画の色です。
- どんな場面に：華やかな場面・ミュージカル・おとぎ話に。

### 7. Duotone｜デュオトーン
- コマンド：`/duotone`
- LUT：`luts/07_duotone.cube`
- どんな色か：画面全体を2つの色だけで作ります。
- どんな場面に：ポスター風・ミュージックビデオ・印象に残したい1枚に。

### 8. Red Wash｜レッド・ウォッシュ
- コマンド：`/red-wash`
- LUT：`luts/08_red-wash.cube`
- どんな色か：画面全体が深い赤に染まります。
- どんな場面に：危険・情熱・警報の場面に。

### 9. Hyper-Saturated｜ハイパーサチュレート
- コマンド：`/hyper-saturated`
- LUT：`luts/09_hyper-saturated.cube`
- どんな色か：すべての色を最大まで鮮やかにします。
- どんな場面に：ポップな広告・夢の中・おもちゃのような世界に。

### 10. Colour Negative｜カラー・ネガ
- コマンド：`/colour-negative`
- LUT：`luts/10_colour-negative.cube`
- どんな色か：フィルムのネガのように色が反転します。
- どんな場面に：SF・異世界・ぞっとする場面に。

### 11. Pastel｜パステル
- コマンド：`/pastel`
- LUT：`luts/11_pastel.cube`
- どんな色か：明るくやわらかい、お菓子のような色です。
- どんな場面に：かわいい・やさしい・青春の場面に。

### 12. Warm Amber｜ウォーム・アンバー
- コマンド：`/warm-amber`
- LUT：`luts/12_warm-amber.cube`
- どんな色か：全体を金色・オレンジに寄せます。
- どんな場面に：夕方・思い出・なつかしい場面に。

### 13. Cool Blue｜クール・ブルー
- コマンド：`/cool-blue`
- LUT：`luts/13_cool-blue.cube`
- どんな色か：全体を青に寄せます。
- どんな場面に：冷たい・孤独・病院や夜の場面に。

### 14. Matrix Green｜マトリックス・グリーン
- コマンド：`/matrix-green`
- LUT：`luts/14_matrix-green.cube`
- どんな色か：画面全体にうすい緑がかかります。
- どんな場面に：SF・デジタルの世界・不気味な場面に。

### 15. Yellow Tint｜イエロー・ティント
- コマンド：`/yellow-tint`
- LUT：`luts/15_yellow-tint.cube`
- どんな色か：ほこりっぽい黄色〜オレンジがかかります。
- どんな場面に：砂漠・暑い国・乾いた場面に。

### 16. Magenta Wash｜マゼンタ・ウォッシュ
- コマンド：`/magenta-wash`
- LUT：`luts/16_magenta-wash.cube`
- どんな色か：ピンク〜紫がかかります。
- どんな場面に：夢・人工的・ポップな場面に。

### 17. Complementary Palette｜補色の配色
- コマンド：`/complementary-palette`
- LUT：`luts/17_complementary-palette.cube`
- どんな色か：赤と緑のような反対の色を画面でぶつけます。
- どんな場面に：人物を背景から目立たせたいとき。

### 18. Analogous Palette｜類似色の配色
- コマンド：`/analogous-palette`
- LUT：`luts/18_analogous-palette.cube`
- どんな色か：黄・オレンジ・赤のような隣どうしの色だけでまとめます。
- どんな場面に：まとまりのある、落ち着いた画面に。

### 19. Monochromatic Palette｜単色の配色
- コマンド：`/monochromatic-palette`
- LUT：`luts/19_monochromatic-palette.cube`
- どんな色か：1つの色の濃い・うすいだけで作ります。
- どんな場面に：静か・統一感・アート寄りの場面に。

### 20. Split Toning｜スプリット・トーン
- コマンド：`/split-toning`
- LUT：`luts/20_split-toning.cube`
- どんな色か：明るい所をあたたかく、影を冷たくします。
- どんな場面に：いちばん使いやすい映画の色。どんな場面にも。

### 21. Crushed Blacks｜クラッシュド・ブラック
- コマンド：`/crushed-blacks`
- LUT：`luts/21_crushed-blacks.cube`
- どんな色か：影を真っ黒にして、画面を引きしめます。
- どんな場面に：強い・かっこいい・夜の場面に。

### 22. Lifted Blacks｜リフテッド・ブラック
- コマンド：`/lifted-blacks`
- LUT：`luts/22_lifted-blacks.cube`
- どんな色か：黒を少し浮かせて、影をうすく白っぽくします。
- どんな場面に：思い出・やわらかい・フィルムっぽい場面に。

### 23. Print Film Emulation｜フィルム・プリント
- コマンド：`/print-film-emulation`
- LUT：`luts/23_print-film-emulation.cube`
- どんな色か：映画館のフィルムのような、濃さと色のなめらかさです。
- どんな場面に：映画っぽさを自然に足したいとき。

### 24. Kodachrome｜コダクローム
- コマンド：`/kodachrome`
- LUT：`luts/24_kodachrome.cube`
- どんな色か：赤と青が強く出る、あたたかい昔のフィルムの色です。
- どんな場面に：旅・家族の思い出・ヴィンテージの場面に。

### 25. Fuji Greens｜フジ・グリーン
- コマンド：`/fuji-greens`
- LUT：`luts/25_fuji-greens.cube`
- どんな色か：緑がミントっぽく、肌がやわらかく出ます。
- どんな場面に：自然・街歩き・おだやかな場面に。

### 26. Day-for-Night｜デイ・フォー・ナイト
- コマンド：`/day-for-night`
- LUT：`luts/26_day-for-night.cube`
- どんな色か：昼の映像を、暗い青で夜に見せます。
- どんな場面に：夜の場面を昼の素材で作りたいとき。

### 27. Infrared｜インフラレッド
- コマンド：`/infrared`
- LUT：`luts/27_infrared.cube`
- どんな色か：木や草が赤やピンクになる、ふしぎな色です。
- どんな場面に：夢・異世界・アート寄りの場面に。

### 28. Neon Noir｜ネオン・ノワール
- コマンド：`/neon-noir`
- LUT：`luts/28_neon-noir.cube`
- どんな色か：暗い画面に、シアンとマゼンタが鮮やかに出ます。
- どんな場面に：夜の街・サイバーパンク・クラブに。

### 29. 1970s Vintage｜70年代ビンテージ
- コマンド：`/1970s-vintage`
- LUT：`luts/29_1970s-vintage.cube`
- どんな色か：あたたかく少し色あせた、茶色〜オレンジの色です。
- どんな場面に：昔の時代・レトロ・なつかしい場面に。

### 30. Night Vision｜ナイト・ビジョン
- コマンド：`/night-vision`
- LUT：`luts/30_night-vision.cube`
- どんな色か：暗視カメラのような、ざらついた緑の画面です。
- どんな場面に：監視・潜入・ホラーの場面に。

### 31. Sickly Green-Yellow｜シックリー・グリーンイエロー
- コマンド：`/sickly-green-yellow`
- LUT：`luts/31_sickly-green-yellow.cube`
- どんな色か：くすんだ黄緑で、落ち着かない色です。
- どんな場面に：スリラー・不安・病気の場面に。

### 32. Thermal｜サーマル
- コマンド：`/thermal`
- LUT：`luts/32_thermal.cube`
- どんな色か：熱いところが赤や黄色に光る、温度計の色です。
- どんな場面に：SF・追跡・特別な視点の場面に。

### 33. Earth Tones｜アースカラー
- コマンド：`/earth-tones`
- LUT：`luts/33_earth-tones.cube`
- どんな色か：土や草のような、茶色とオリーブの色です。
- どんな場面に：自然・素朴・落ち着いた場面に。

### 34. Blown-Out Highlights｜ブロウンアウト・ハイライト
- コマンド：`/blown-out-highlights`
- LUT：`luts/34_blown-out-highlights.cube`
- どんな色か：明るい所が白く飛んで光ります。
- どんな場面に：夢・回想・まぶしい思い出の場面に。
