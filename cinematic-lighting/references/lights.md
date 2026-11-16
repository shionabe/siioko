# 光の50種（プロンプトつき）

- 使い方：下の「LIGHTING:」の行を、SKILL.md の「プロンプトの型」の頭のあとに付けます。
- 下の文は、どの画像にも合うように書いた見本です。そのまま使わず、相手の画像に合わせて直します。
  - 「the subject」は写っている人や物、「the background」「the room」は実際の背景や部屋（例：本棚・キッチン・カフェ・車の中）に置きかえます。
  - 「frame-left（画面の左）」は、画像の窓や光の元がある側に合わせます。窓がない画像なら「a large light just outside frame-left」のように、画面の外にある光に置きかえます。
  - ろうそく・ランプ・電球の飾りなど、画像にない光る物を足すときは、それだけを足すと書きます（ほかの物は変えない）。
- 色補正の言葉（teal and orange、LUT、color grade など）は入れません。色は光を決めたあとに付けます（five-points.md の「色は後から」）。

---

## A. 顔と部屋の基本の光（1〜19）

### 1. Window light｜ウィンドウ・ライト（窓の光）
- コマンド：`/window-light`
- どんな場面に：昼の室内。いちばん自然で、まず試す光です。

```
LIGHTING: the ceiling lights are off. Soft daylight from the window at frame-left is the only light. It falls on the side of the subject's face toward the window and fades gradually across the face; the background falls off into soft darkness.
```

### 2. Rembrandt light｜レンブラント・ライト（レンブラント）
- コマンド：`/rembrandt-light`
- どんな場面に：落ち着いた肖像や会話の場面。頬に小さな三角の光が残ります。

```
LIGHTING: the ceiling lights are off. One soft light comes from high at frame-left, in front of the subject and about 45 degrees to the side. It lights the frame-left side of the face. On the frame-right cheek, just below the eye, a small triangle of light remains; the rest of the frame-right side of the face is in soft shadow that keeps the skin texture. The background is a step darker than the face.
```

### 3. Soft light｜ソフト・ライト（柔らかい光）
- コマンド：`/soft-light`
- どんな場面に：やさしい・静かな場面。影の境目がゆっくりぼけます。

```
LIGHTING: the ceiling lights are off. One very large, soft light, like a big frosted window, sits very close to the subject, just outside the frame, high at frame-left and about 45 degrees to the side. Because the light is so large and so close, the edge between light and shadow on the face is a slow, gentle gradient, and the shadow side keeps all its detail. The background is a step darker.
```

### 4. Hard light｜ハード・ライト（硬い光）
- コマンド：`/hard-light`
- どんな場面に：夏の日差し・緊張した場面。影の境目がくっきりします。

```
LIGHTING: the ceiling lights are off. Hard, direct sunlight from the window at frame-left hits the subject's face: sharp-edged dark shadows from the nose and hair, bright highlights on the cheek; the line between light and shadow is crisp. The parts of the room away from the window are in shade.
```

### 5. Negative fill｜ネガティブ・フィル（ネガティブフィル）
- コマンド：`/negative-fill`
- どんな場面に：顔に立体感と深さを出したいとき。影の側を黒い布で暗いままにします。

```
LIGHTING: the ceiling lights are off. Soft daylight from the window at frame-left lights the subject's face. A black cloth just outside frame-right takes away all bounced light, so the frame-right side of the face stays in deep, clean shadow; the line between light and shadow runs down the middle of the nose.
```

### 6. Volumetric haze｜ボリューメトリック・ヘイズ（ヘイズ）
- コマンド：`/haze`
- どんな場面に：光の筋を見せたいとき。教会・古い部屋・朝の倉庫など。

```
LIGHTING: late afternoon. The ceiling lights are off. Low sunlight comes through the window at frame-left. The whole room is filled with a light atmospheric haze, so the sunlight shows as visible shafts of light with fine dust floating in them. The dark parts of the room stay dark.
```

### 7. Split light｜スプリット・ライト（スプリット）
- コマンド：`/split-light`
- どんな場面に：迷い・二面性・ミステリー。顔がちょうど半分に分かれます。

```
LIGHTING: the ceiling lights are off. One soft light from exactly 90 degrees at frame-left, at the height of the subject's eyes. The frame-left half of the face is lit; the frame-right half falls into shadow; the line between them runs straight down the middle of the nose. The background is dark.
```

### 8. Dappled light｜ダップルド・ライト（木漏れ日）
- コマンド：`/dappled-light`
- どんな場面に：晴れた日のやさしい場面・思い出のシーン。

```
LIGHTING: a sunny day. The ceiling lights are off. Sunlight comes through the leaves of a tree outside the window at frame-left; small soft spots of sunlight and leaf shadows dapple the subject's face, neck and clothes. The background is in soft shade.
```

### 9. Golden hour backlight｜ゴールデンアワー・バックライト（夕日の逆光）
- コマンド：`/golden-backlight`
- どんな場面に：夕方・別れ・なつかしい場面。髪のふちが金色に光ります。

```
LIGHTING: late afternoon. The ceiling lights are off. The sun is low, just outside the window at frame-left and slightly behind the subject. A thin warm orange edge of sunlight outlines the hair, the side of the neck and the shoulder. The face, turned toward the window, is in soft shade but still readable. Long warm shadows of the window frame run across the floor toward the camera.
```

### 10. Moonlight｜ムーンライト（月明かり）
- コマンド：`/moonlight`
- どんな場面に：夜・静かな場面・ひとりの時間。

```
LIGHTING: night. All lights in the room are off. The only light is cold blue moonlight coming through the window at frame-left. It falls as a pale rectangle on the floor and lights the frame-left side of the subject's face and body; the frame-right side of the subject and the background fall into deep blue darkness.
```

### 11. Candlelight｜キャンドルライト（ろうそく）
- コマンド：`/candlelight`
- どんな場面に：夜・昔の時代・親しい会話。光がすぐに暗くなります。

```
LIGHTING: night. All other lights are off and any window shows a dark night. The only light is a lit candle on the table beside the subject (add one if there is none). It lights the face and hands from low and to the side with warm light; the light falls off quickly, and the background is almost black.
```

### 12. Top light｜トップ・ライト（真上から）
- コマンド：`/top-light`
- どんな場面に：取り調べ・孤独・重い空気。目が影に沈みます。

```
LIGHTING: the ceiling lights are off. One hard light straight above the subject's head. The hair and the tops of the cheekbones are bright; the eyes sit in dark shadow; a short shadow falls below the nose and chin. The background is dark.
```

### 13. Rim light｜リム・ライト（縁の光）
- コマンド：`/rim-light`（緑の縁の光は `/rim-light green`）
- どんな場面に：暗い背景から人を浮かせたいとき。夜の場面に。
- 色違い：縁の光を緑にすると、不思議な・少し不安な空気になります。下の2つ目の文を使います。

```
LIGHTING: the ceiling lights are off. One light behind the subject, high at frame-right, hidden outside the frame. It draws a thin bright edge along the hair, the back of the neck and the shoulder. The face is lit only softly by light bouncing around the room, so it stays readable but darker than the edge. The background is dark.
```

緑の縁の光（色違い）：

```
LIGHTING: the ceiling lights are off. One green light behind the subject, high at frame-right, hidden outside the frame. It draws a thin bright green edge along the hair, the back of the neck and the shoulder. The face is lit only softly by dim bounced light, so it stays readable but much darker than the green edge. The background is dark.
```

### 14. Firelight｜ファイアライト（暖炉の火）
- コマンド：`/firelight`
- どんな場面に：冬の夜・家族の場面・キャンプ。光がゆらぐ暖かさ。

```
LIGHTING: night. All other lights are off and any window shows dark night. A fireplace just outside the frame at frame-right throws warm orange firelight from low at frame-right onto the subject's face, body and the nearby furniture, with large soft shadows thrown up onto the background.
```

### 15. Blue hour｜ブルーアワー（ブルーアワー）
- コマンド：`/blue-hour`
- どんな場面に：日が沈んだすぐあと。さびしい・静かな場面。

```
LIGHTING: just after sunset. The ceiling lights are off and no lamps or candles are lit. Deep blue twilight comes through the window at frame-left and fills the room with soft, cool blue light. No direct sun. The room is dim and calm.
```

### 16. Lightning｜ライトニング（稲妻）
- コマンド：`/lightning`
- どんな場面に：嵐の夜・こわい場面・何かが起きる一瞬。

```
LIGHTING: night, a storm outside. All lights are off. A flash of lightning outside the window at frame-left throws a sudden, cold, bright white light across the room: hard shadows of the window frame on the floor, the subject's face and body lit harshly from frame-left, the rest of the room in deep darkness.
```

### 17. Shadow pattern｜シャドウ・パターン（壁の模様）
- コマンド：`/shadow-pattern`
- どんな場面に：背景がさびしいとき。壁にぼけた影の模様を足します。

```
LIGHTING: the ceiling lights are off. Soft daylight from the window at frame-left lights the subject's face. Behind the subject, soft, out-of-focus shadows of tree branches outside the window fall across the background wall, so the background has a gentle pattern of light and shade.
```

### 18. High key｜ハイ・キー（ハイキー）
- コマンド：`/high-key`
- どんな場面に：明るい・さわやか・広告やコメディ。影がほとんどありません。

```
LIGHTING: high-key lighting. The ceiling lights are off. Bright, soft white daylight floods in through the window at frame-left and bounces everywhere, so the whole scene is bright with almost no shadows; surfaces look lighter; airy and clean.
```

### 19. Low key｜ロー・キー（ローキー）
- コマンド：`/low-key`
- どんな場面に：サスペンス・重い場面。画面の大部分が暗くなります。

```
LIGHTING: low-key lighting. The ceiling lights are off. One small soft light from frame-left lights only the subject's face and the front of the body; about 80% of the frame, including the background and the floor, falls into deep shadow.
```

---

## B. 光の元と夜の光（20〜29）

### 20. Spotlight｜スポットライト（スポットライト）
- コマンド：`/spotlight`
- どんな場面に：舞台・告白・ひとりだけを目立たせたいとき。

```
LIGHTING: the room lights are off. One hard spotlight from high above and slightly in front of the subject makes a clear round pool of light on the subject and the floor around them. The edge of the pool is soft but distinct. Outside the pool the room falls into darkness, with only a faint spill of light on the nearest part of the background.
```

### 21. Neon｜ネオン（ネオン）
- コマンド：`/neon`
- どんな場面に：夜の街・バー・近未来。2色の光が顔で混ざります。

```
LIGHTING: the room lights are off. Two coloured neon lights hit the subject from the sides: hot pink neon from frame-left and electric blue neon from frame-right. The pink and blue meet on the face, with a soft blend down the middle of the face. The background is dark, with faint pink and blue reflections on its surfaces.
```

### 22. Incandescent｜インキャンデセント（白熱灯）
- コマンド：`/incandescent`
- どんな場面に：夜の家・昔の部屋・あたたかい場面。光の元のランプが画面に映ります。

```
LIGHTING: evening. The ceiling lights are off. A table lamp with a warm tungsten bulb and a fabric shade stands behind the subject at frame-left, clearly in the frame and a little out of focus (add one if there is none). Its warm amber light falls on the frame-left side of the face; the rest of the face falls off into soft shadow. The light on the face clearly comes from that lamp, and the corners of the room are dim.
```

### 23. Noir｜ノワール（ノワール）
- コマンド：`/noir`
- どんな場面に：探偵もの・秘密・夜の取引。顔の半分が真っ暗です。

```
LIGHTING: it is night. One hard, amber light comes from frame-right at face height, like a desk lamp just out of frame. It lights only the frame-right half of the subject's face; the other half falls into deep black shadow. The background is almost black. Film-noir mood.
```

### 24. Silhouette｜シルエット（シルエット）
- コマンド：`/silhouette`
- どんな場面に：顔を見せない場面・余韻・オープニング。

```
LIGHTING: the ceiling lights are off. The background behind the subject is brightly and evenly lit by hidden lights. The subject's face and body receive no light at all, so the subject becomes a pure black silhouette: only the outline of the profile, hair and shoulders against the bright background.
```

### 25. Sodium vapour｜ソディウム・ベイパー（オレンジの街灯）
- コマンド：`/sodium-vapour`
- どんな場面に：夜の街角・駐車場・さびしい帰り道。ほぼオレンジ1色になります。

```
LIGHTING: it is night. The ceiling lights and the lamps in the room are off. The only light is a sodium-vapour street lamp outside the window at frame-left. Its monochrome orange light comes in through the window, lights the side of the subject's face and body that faces the window, and throws the window frame's shadow across the floor. Everything away from the window falls into dark orange-brown shadow. The whole image is almost one colour: deep sodium orange.
```

### 26. Bare bulb｜ベア・バルブ（裸電球）
- コマンド：`/bare-bulb`
- どんな場面に：地下室・古いアパート・追いつめられた場面。

```
LIGHTING: night. All other lights are off. A single bare light bulb with no shade hangs on a cord just above and slightly in front of the subject, visible at the top of the frame (add one if there is none). It glows warm yellow-white and throws hard light down onto the hair, forehead and shoulders, with dark shadows under the brows, nose and chin. The light falls off quickly; the walls are dim and the corners of the room are dark.
```

### 27. Mixed color temperature｜ミックスド・カラー・テンパラチャー（暖色と寒色）
- コマンド：`/mixed-color`
- どんな場面に：夕方の室内・気持ちがゆれる場面。暖かい色と冷たい色を左右に分けます。

```
LIGHTING: evening. The ceiling lights are off. A warm amber lamp just outside the frame at frame-right lights the frame-right side of the subject's face; cool blue dusk light from the window at frame-left lights the frame-left side. The two colors stay separate on the face and meet softly along the bridge of the nose.
```

### 28. Cast shadow｜キャスト・シャドウ（落ちる影）
- コマンド：`/cast-shadow`
- どんな場面に：南の国の午後・閉じこめられた気持ち。くっきりした影の形を見せます。

```
LIGHTING: a sunny afternoon. The ceiling lights are off. Wooden louvered shutters are half closed over the window at frame-left. Hard sunlight comes through the slats and falls as sharp stripes of light and shadow across the floor, the furniture, the subject's clothes, face and the wall behind. Between the stripes the room is in soft shade.
```

### 29. Bloom / halation｜ブルーム／ハレーション（にじみ）
- コマンド：`/bloom`
- どんな場面に：夢・回想・あこがれ。明るい所がふわっとにじみます。

```
LIGHTING: late afternoon. The ceiling lights are off. Bright low sunlight comes through the window at frame-left and slightly behind the subject. The brightest areas, the window, the edge of the hair and the shoulder, glow softly: light blooms outward from them with a gentle warm halo, and fine hair at the edges seems to melt into the glow. The face is in soft shade but readable; the dark parts of the room stay dark and clean, not hazy.
```

---

## C. いろいろな場面の光（30〜50）

### 30. Flashlight｜フラッシュライト（懐中電灯）
- コマンド：`/flashlight`
- どんな場面に：停電・探検・ホラー。丸い光の外は真っ暗です。

```
LIGHTING: it is night and the room lights are off. The only light is a handheld flashlight held just off-camera at frame-right. Its hard, cool-white beam makes a bright circle on the subject and on part of the background, with a sharp edge; everything outside the beam falls into near-black darkness.
```

### 31. Screen light｜スクリーン・ライト（画面の光）
- コマンド：`/screen-light`
- どんな場面に：夜にスマホやパソコンを見る場面。

```
LIGHTING: it is night and the room lights are off. The only light is the glow of a laptop or phone screen just below the frame in front of the subject. Soft cool-blue light lights the face from below and in front, brightest on the chin, cheeks and eyes; the background is almost black.
```

### 32. Fluorescent｜フローレセント（蛍光灯）
- コマンド：`/fluorescent`
- どんな場面に：病院・オフィス・コンビニ。冷たく少し不安な空気。

```
LIGHTING: the warm lamps are off. Long overhead fluorescent tube lights light the whole room from above with flat, slightly green-white light. Faces look a little pale and greenish, shadows are weak and soft, and the room feels cold and institutional.
```

### 33. Blinds｜ブラインズ（ブラインド越しの光）
- コマンド：`/blinds`
- どんな場面に：オフィス・探偵もの・昼の室内。横じまの光と影。

```
LIGHTING: the ceiling lights are off. Hard daylight comes through window blinds at frame-left and throws parallel horizontal stripes of light and shadow across the subject's face, body and the background. The stripes are crisp, and the gaps between them are dark.
```

### 34. Clamshell｜クラムシェル（クラムシェル）
- コマンド：`/clamshell`
- どんな場面に：美容・化粧品・きれいな顔のアップ。

```
LIGHTING: the ceiling lights are off. A soft light from directly in front and slightly above the subject's face, plus a soft fill from directly below, light the face evenly like a beauty portrait. There is a small soft shadow under the chin, and two catchlights appear in the eyes; the background is a step darker.
```

### 35. Cross lighting｜クロス・ライティング（交差する光）
- コマンド：`/cross-light`
- どんな場面に：アクション・対決・ミュージックビデオ。両側のふちが光ります。

```
LIGHTING: the ceiling lights are off. Two hard lights hit the subject from opposite sides, one from behind-left and one from behind-right, so both edges of the face and shoulders are bright and the center of the face falls into a narrow band of shadow. The background is dark.
```

### 36. Kicker｜キッカー（キッカー）
- コマンド：`/kicker`
- どんな場面に：暗い背景で、人の形をはっきりさせたいとき。

```
LIGHTING: the ceiling lights are off. A soft main light from frame-left lights the subject's face. A second, harder light from behind the subject at frame-right skims along the frame-right cheek, jaw and hair, leaving a thin bright edge that separates the subject from the dark background.
```

### 37. Eye light｜アイ・ライト（目だけの光）
- コマンド：`/eye-light`
- どんな場面に：にらむ・決意・心の声。目だけが光ります。

```
LIGHTING: the room is dim and moody. A narrow, soft strip of light falls only across the subject's eyes; the rest of the face and the room stay in shadow. The eyes shine with clear catchlights.
```

### 38. Ring light｜リング・ライト（リングライト）
- コマンド：`/ring-light`
- どんな場面に：配信・自撮り・美容の動画。目に丸い光が映ります。

```
LIGHTING: the ceiling lights are off. A ring light is placed right in front of the subject's face, just beside the camera. The face is lit very evenly with almost no shadows, there is a circular ring-shaped catchlight in each eye, and the background is darker than the face.
```

### 39. Direct flash｜ダイレクト・フラッシュ（カメラのフラッシュ）
- コマンド：`/direct-flash`
- どんな場面に：パーティー・夜遊び・スナップ写真の雰囲気。

```
LIGHTING: it is night and the room is dark. A camera flash fires straight from the camera position. The subject's face and clothes are lit harshly and flatly, with bright highlights on the skin and a hard dark shadow cast on the wall directly behind the subject; the far corners of the room fall into darkness, like a party snapshot.
```

### 40. Snow light｜スノー・ライト（雪の照り返し）
- コマンド：`/snow-light`
- どんな場面に：冬の朝・静かな場面。白く明るく、少し青い光。

```
LIGHTING: it is a snowy winter day outside the window at frame-left, and the room lights are off. Bright, cool, very soft daylight reflected from the snow fills the room from the window side. The skin and the room take a clean, slightly blue-white tone, and shadows are soft and pale.
```

### 41. Lens flare｜レンズ・フレア（レンズフレア）
- コマンド：`/lens-flare`
- どんな場面に：夏・青春・まぶしい朝。光がレンズに入って筋が出ます。

```
LIGHTING: the ceiling lights are off. A strong low sun shines straight through the window at frame-left toward the camera. A visible lens flare streaks across the frame from the window, with a soft glow and a few round flare spots; the subject is lit from the side by warm sunlight.
```

### 42. Dashboard light｜ダッシュボード・ライト（ダッシュボードの光）
- コマンド：`/dashboard-light`
- どんな場面に：夜のドライブ・車の中の会話。

```
LIGHTING: it is night and the room lights are off. A small, low panel of soft blue-green light below the frame in front of the subject lights the face from below, like the dashboard of a car at night. The face is dim and cool, and everything else is in deep darkness.
```

### 43. Police lights｜ポリス・ライツ（パトカーの光）
- コマンド：`/police-lights`
- どんな場面に：事件・追われる場面。赤と青の光が入れかわります。

```
LIGHTING: it is night and the room lights are off. Flashing police lights outside the window at frame-left wash the room with alternating red and blue light. The frame-left side of the subject's face is red and the other side is blue, and colored light spills across the background; the rest of the room is dark.
```

### 44. String lights｜ストリング・ライツ（電球の飾り）
- コマンド：`/string-lights`
- どんな場面に：パーティー・カフェ・クリスマス。背景に小さな光の粒。

```
LIGHTING: it is evening and the ceiling lights are off. A string of small warm bulbs hangs across the background behind the subject (add one if there is none). The bulbs glow as small soft points in the background, and their warm light softly lights the face and hair; the room feels cozy and intimate.
```

### 45. Searchlight｜サーチライト（サーチライト）
- コマンド：`/searchlight`
- どんな場面に：脱出・見つかる瞬間。強い光の筋が通ります。

```
LIGHTING: it is night and the room lights are off. A powerful searchlight outside the window at frame-left sweeps into the room. A hard, bright beam of white light cuts across the room through a light haze and catches the subject; everything outside the beam is dark.
```

### 46. Explosion｜エクスプロージョン（爆発）
- コマンド：`/explosion`
- どんな場面に：アクション・大事件の瞬間。強いオレンジの光と長い影。

```
LIGHTING: it is night. A huge explosion outside the window at frame-left floods the room with intense flickering orange and yellow light. The frame-left side of the subject's face and body glow hot orange, long dark shadows stretch across the floor toward frame-right, and the far side of the room is in darkness.
```

### 47. Muzzle flash｜マズル・フラッシュ（銃の光）
- コマンド：`/muzzle-flash`
- どんな場面に：アクション・暗闇の一瞬。強い光がすぐ消えます。

```
LIGHTING: the room is almost completely dark. A single instant of bright yellow-white light, like a muzzle flash from a gun fired just off-camera at frame-right, hits the subject's face and the nearest part of the background for a split second. Hard light, very short falloff; the rest of the frame stays black.
```

### 48. Laser light｜レーザー・ライト（レーザー）
- コマンド：`/laser-light`
- どんな場面に：クラブ・SF・ライブ。空中に細い光の線が見えます。

```
LIGHTING: it is night and the room lights are off. Thin beams of bright green laser light cross the room through a light haze, drawing straight lines in the air. Green light catches the edges of the subject's face and clothes; the rest of the room is dark.
```

### 49. Blacklight (UV)｜ブラックライト（ブラックライト）
- コマンド：`/blacklight`
- どんな場面に：クラブ・ふしぎな夢・ホラー。白い物だけが光ります。

```
LIGHTING: the room lights are off. Ultraviolet blacklight fills the room with a deep violet glow. White and light-colored details, such as white fabric, paper and white objects, glow brightly; the skin looks dim purple and the rest of the room is dark violet.
```

### 50. City bokeh｜シティ・ボケ（街のぼけ）
- コマンド：`/city-bokeh`
- どんな場面に：夜景・デート・都会の夜。背景が丸い光のぼけになります。

```
LIGHTING: it is night. The room lights are off and the background behind the subject is replaced by out-of-focus city lights seen through a window: large soft round bokeh circles in warm orange and cool blue. Soft cool light from the city lights the subject's face from frame-left.
```
