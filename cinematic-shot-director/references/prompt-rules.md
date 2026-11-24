# プロンプトの型と注意

## 画像のプロンプト（① 静止画／③ の最初の1枚）
```
[If images are attached:] Image 1 is the character: take only her face, hair, makeup and costume; ignore the grey backdrop, the layout and the studio light. Image 2 is the location: use it as the set.

SCENE: [場所を先に書く：部屋・窓・光の元・手前の物]. [人物が何をしている様子か]. 
EMOTION: [気持ちを表情としぐさで：目・口・手・肩・息].
SHOT: [ショットの大きさ＋アングル：shots.md の英語].
COMPOSITION: [構図：compositions.md の英語。置き場所・大きさ（何と同じ大きさか）・カメラの高さ・空ける側に何があるか・手前のぼけた物].
LIGHT: [光の元と向き：窓の光が左から、など].
Photorealistic film still, 16:9, natural colours, no text.
```

## 動画のプロンプト（② 動画／③ の動画）
```
[③ のとき:] Image 1 is the first frame. Keep her face, costume, the room and the light exactly as in the image.
[② で画像があるとき:] Image 1 is the character (face, hair, makeup and costume only). Image 2 is the location, used as the set.

SCENE: [場所]. [人物がこれから何をするか：秒ごとに書くと出やすい（0–2s ..., 2–5s ...）].
EMOTION: [気持ちとその変化を、表情としぐさで].
SHOT AND COMPOSITION: [始まりのショットと構図].
CAMERA: [moves.md の英語＋何に反応して動くか（動く理由）＋終わりに何が見えるか].
One continuous take.
NEGATIVE: no change to her face or identity, no new people, no extra objects, no warped or melting background, no cuts, no text.
```

## 書き方のコツ（試して効いたこと）
### カメラの動き
- **寄るときは「ズーム」と書かない。「カメラそのものが近づく（a physical dolly move, not a zoom）」と書く**。ズームと書くと、背景ごと平たく大きくなるだけ
- 引くときは、**最後の画面に何が見えるか**まで書く（書かないと人物が大きいまま残る）
- パンは「右へ振る」より「**背景が画面の右から左へ流れる**」と書く方が出る
- 手持ちは「スマホで撮った」「撮っている人」と書かない（スマホや人が映る）。**揺れの大きさ**で書く（light handheld sway … no jitter）
- 固定は「最後まで動かさない（perfectly still for the whole shot）」とはっきり書く（AI は少し動こうとする）
- 回り込みは 90〜180° まで。1周させると顔や背中の服が変わりやすい
- ドリーズーム（めまい効果）・クレーンは出にくい。出なくても困らない場面で使う
- 1ショットに動きは1つ。人物の激しい動きとカメラの大きな動きを同時に頼むと崩れやすい
- 撮った動画を参照にして、あとからカメラワークを付けることもできる（「Re-film the same moment as if a second camera operator had been there」＋「The first frame matches the framing of the reference video; do not widen it」）

### 構図
- 大きさは％でなく「**何と同じ大きさか**」で書く（例：her head is the size of the window latch）
- **人物より先に場所を書く**
- **手前に1つ、ぼけた物を置く**と奥行きが出る（3層）
- 空ける側（視線の先）に**物を書く**（何も書かないと詰められる）
- 額縁（窓・扉ごし）は、枠の画像を渡すより言葉で書く
- 「wide shot」と書くだけでは、人物は画面の4割より小さくならない → 何かと比べて大きさを書き、見下ろす角度を足す

### 気持ち
- 気持ちの名前だけでなく、**目・口・手・肩・息**で書く（例：her lips part and her eyes stop moving）
- 気持ちだけ書くと、表情は変わるが置き場所はほぼ同じ。構図だけ書くと、置き方は変わるが表情はふつう。**両方書く**

## 出なかったとき
| 起きたこと | 直し方 |
|---|---|
| 寄ったのに背景が平たい | 「not a zoom, the camera itself moves closer, the foreground slides past」を足す |
| 動画が元より引いた所から始まる | 「The first frame matches …; do not widen it」を足す |
| 人物が真ん中・大きいまま | 場所を先に書く／何かと比べて大きさ／見下ろす角度 |
| 顔が別人になる | 回り込みの角度を小さく／「the same person throughout」を足す |
| 途中でカットが入る | 「One continuous take, no cuts」を本文の頭と NEGATIVE の両方に |
| 空から回るのに目の高さのまま | カメラの高さを数字で（about three metres above the floor）＋上から何が見えるか（the top of her head, the floor around her）＋「The camera never comes down to eye level」 |
| 回り込みが小さく、背景が変わらない | 角度を数字で（a full half circle, 180 degrees）＋始め・途中・終わりに後ろに何が来るかを並べる（window → curtain → painting） |
| スライダーで別の場所に切り替わる | 手前の物を名指しで置く（the fruit bowl very close to the lens at the right edge）＋動く距離（about half a metre）＋「the camera never leaves the room」 |
| 激震からの急停止が寄らない | 秒で区切る（0〜2.5秒は揺れながら寄る／2.5秒でぴたりと止まる）＋止まった画の大きさ（her two wide eyes fill the whole width of the frame） |
| ダッチアングルが傾かない | 角度の数字＋傾いて見える物を並べる（the window frames run diagonally, the floor slopes steeply）＋「the frame never straightens and is never level」 |
| バレットタイムで人物が消える・別のカットに飛ぶ | 「跳ぶ＋時間が止まる」を同時に頼むと作れずにカットでごまかす。跳ばせず「手紙を軽く投げる → 手紙とほこりが宙で止まる → カメラだけ90°回る」＋「最後まで彼女が真ん中」（2026-11-21 で出た） |
| 窓を通り抜けず、窓の手前で止まる | 2回とも窓台と窓枠が手前に残った（窓の外の画像を参照に入れていると、その画で止まりやすい【推測】）。通り抜けは編集で2本をつなぐ方が確実 |
| 前を後ろ向きに下がるのに人物が近づいて大きくなる | 5秒だと歩き出すまでで終わる → 8秒（176クレジット）＋「最初のコマから歩いている」。それでもカメラが人物より遅く、だんだん大きくなる |
| 無限ズーム（入れ子）が出ない | 絵の中の絵（Droste）と書いても、窓や絵まで寄るだけだった（2026-11-20・2回）。生成で作らず、編集で同じ画を小さく重ねて寄る方が確実 |
