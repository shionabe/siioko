---
name: cinematic-lighting
description: 画像や動画の「光」だけを変えて、シネマティックにするスキル。光50種（窓の光・レンブラント・ネオン・月明かり・逆光・ヘイズ・シルエットなど）から選んで、光だけを変える英語のプロンプトを書く。「シネマティックに」「映画っぽく」「ライティング」「照明を変えたい」「光を変えて」「リライト」「relight」と言われたとき、50種の光の名前が出たとき、`/window-light` `/rembrandt-light` `/neon` のような光のコマンドが送られたときは、必ずこのスキルを使う。
---

# cinematic-lighting｜光を変えてシネマティックにする

AI に「シネマティックに」とだけ頼んでも、映画っぽくはなりません。足りないのは「光の向き・硬さ・影・光の元」の指定です。
このスキルは、相手の画像に合わせて **光だけを変える** プロンプトを書きます。

## 進め方
1. **画像を見る**：写っている人や物・部屋・窓や光の元の位置を、短く言葉にする。
2. **光を決める**
   - コマンド（例 `/rembrandt-light`）や光の名前が来たら、その光を使う（`references/lights.md`）。
   - 「シネマティックに」だけのときは、短く2〜3個だけ聞く（どんな場面か・時間帯・気分）。そのあと、合う光を3つ選んで理由を1行ずつ書き、選んでもらう。
3. **プロンプトを書く**：下の「プロンプトの型」の頭に、`references/lights.md` のその光の `LIGHTING:` の行を付ける。
   - 「the subject」「the background」「the room」は、画像に写っている実際の物の名前に置きかえる。
   - 「frame-left / frame-right」は、画像の窓や光の元がある側に合わせる。
   - 画像にない光の元（ランプ・電球の飾りなど）を足すときは、それだけを足すと書く。
4. **返す**：英語のプロンプト（コードブロック）＋その光の説明を日本語で1〜2行。
5. **画像を作る**：
   - Claude に Higgsfield の MCP をつないでいれば、そのまま作れます。**クレジットがかかるので、作る前に必ず聞く。**
   - つないでいなければ、「画像と一緒に、このプロンプトを画像生成（ChatGPT・Higgsfield など）に貼ってください」と伝える。
6. 顔や服が変わってしまったら、`Keep everything the same` の行を強めて作り直す。

## プロンプトの型
```
Edit the attached image. Keep everything the same: the same person, face, hair, clothes, pose, framing, camera position, and every object in the scene. Change ONLY the lighting, as written below. Keep the original aspect ratio. Photorealistic, matte surfaces, clean image without grain.

LIGHTING: ...
```

## 光を書くときの5つのポイント（くわしくは `references/five-points.md`）
1. 光は1つの方向から（左右どちらから来るかを書く）
2. 影を埋めない（影の側は暗いままと書く）
3. 光の硬さを選ぶ（柔らかい＝影の境目がぼける／硬い＝くっきり）
4. ランプや窓など、光る物を画面に入れる
5. 背景を先に照らす・薄いもや（ヘイズ）で光の筋

色補正の言葉（teal and orange・LUT など）は、光のプロンプトに混ぜません。色は光を決めたあとに付けます。

## コマンドの一覧（50種）
| # | コマンド | 光 | 日本語 |
|---|---|---|---|
| 1 | `/window-light` | Window light | ウィンドウ・ライト（窓の光） |
| 2 | `/rembrandt-light` | Rembrandt light | レンブラント・ライト（レンブラント） |
| 3 | `/soft-light` | Soft light | ソフト・ライト（柔らかい光） |
| 4 | `/hard-light` | Hard light | ハード・ライト（硬い光） |
| 5 | `/negative-fill` | Negative fill | ネガティブ・フィル（ネガティブフィル） |
| 6 | `/haze` | Volumetric haze | ボリューメトリック・ヘイズ（ヘイズ） |
| 7 | `/split-light` | Split light | スプリット・ライト（スプリット） |
| 8 | `/dappled-light` | Dappled light | ダップルド・ライト（木漏れ日） |
| 9 | `/golden-backlight` | Golden hour backlight | ゴールデンアワー・バックライト（夕日の逆光） |
| 10 | `/moonlight` | Moonlight | ムーンライト（月明かり） |
| 11 | `/candlelight` | Candlelight | キャンドルライト（ろうそく） |
| 12 | `/top-light` | Top light | トップ・ライト（真上から） |
| 13 | `/rim-light` | Rim light | リム・ライト（縁の光） |
| 14 | `/firelight` | Firelight | ファイアライト（暖炉の火） |
| 15 | `/blue-hour` | Blue hour | ブルーアワー（ブルーアワー） |
| 16 | `/lightning` | Lightning | ライトニング（稲妻） |
| 17 | `/shadow-pattern` | Shadow pattern | シャドウ・パターン（壁の模様） |
| 18 | `/high-key` | High key | ハイ・キー（ハイキー） |
| 19 | `/low-key` | Low key | ロー・キー（ローキー） |
| 20 | `/spotlight` | Spotlight | スポットライト（スポットライト） |
| 21 | `/neon` | Neon | ネオン（ネオン） |
| 22 | `/incandescent` | Incandescent | インキャンデセント（白熱灯） |
| 23 | `/noir` | Noir | ノワール（ノワール） |
| 24 | `/silhouette` | Silhouette | シルエット（シルエット） |
| 25 | `/sodium-vapour` | Sodium vapour | ソディウム・ベイパー（オレンジの街灯） |
| 26 | `/bare-bulb` | Bare bulb | ベア・バルブ（裸電球） |
| 27 | `/mixed-color` | Mixed color temperature | ミックスド・カラー・テンパラチャー（暖色と寒色） |
| 28 | `/cast-shadow` | Cast shadow | キャスト・シャドウ（落ちる影） |
| 29 | `/bloom` | Bloom / halation | ブルーム／ハレーション（にじみ） |
| 30 | `/flashlight` | Flashlight | フラッシュライト（懐中電灯） |
| 31 | `/screen-light` | Screen light | スクリーン・ライト（画面の光） |
| 32 | `/fluorescent` | Fluorescent | フローレセント（蛍光灯） |
| 33 | `/blinds` | Blinds | ブラインズ（ブラインド越しの光） |
| 34 | `/clamshell` | Clamshell | クラムシェル（クラムシェル） |
| 35 | `/cross-light` | Cross lighting | クロス・ライティング（交差する光） |
| 36 | `/kicker` | Kicker | キッカー（キッカー） |
| 37 | `/eye-light` | Eye light | アイ・ライト（目だけの光） |
| 38 | `/ring-light` | Ring light | リング・ライト（リングライト） |
| 39 | `/direct-flash` | Direct flash | ダイレクト・フラッシュ（カメラのフラッシュ） |
| 40 | `/snow-light` | Snow light | スノー・ライト（雪の照り返し） |
| 41 | `/lens-flare` | Lens flare | レンズ・フレア（レンズフレア） |
| 42 | `/dashboard-light` | Dashboard light | ダッシュボード・ライト（ダッシュボードの光） |
| 43 | `/police-lights` | Police lights | ポリス・ライツ（パトカーの光） |
| 44 | `/string-lights` | String lights | ストリング・ライツ（電球の飾り） |
| 45 | `/searchlight` | Searchlight | サーチライト（サーチライト） |
| 46 | `/explosion` | Explosion | エクスプロージョン（爆発） |
| 47 | `/muzzle-flash` | Muzzle flash | マズル・フラッシュ（銃の光） |
| 48 | `/laser-light` | Laser light | レーザー・ライト（レーザー） |
| 49 | `/blacklight` | Blacklight (UV) | ブラックライト（ブラックライト） |
| 50 | `/city-bokeh` | City bokeh | シティ・ボケ（街のぼけ） |
