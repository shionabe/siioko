# シネマティックな光の5つのポイント

プロンプトを書くときも、直すときも、この5つを見ます。

## ① 光は1つの方向から
- 光がどちらから来るかを、はっきり書きます。
- 書き方の例：「from frame-left（画面の左から）」「high at frame-right（画面の右の高い所から）」
- 普通は、部屋全体を明るくしがちです。でも、光の向きがないと、画像が平らに見えます。だから、まず光を1つに決めます。

## ② 影を埋めない
- 影の側は、暗いままと書きます。
- 書き方の例：「the shadow side stays dark」「nothing fills the shadow」
- 書かないと、AI は影を明るくしてしまうことが多いです。影があるから、顔に立体感が出ます。

## ③ 光の硬さを選ぶ
- 柔らかい光：窓や大きいライト。影の境目がぼけます。やさしい・静かな場面に。
- 硬い光：強い日差しや小さいライト。影の境目がくっきりします。緊張・夏・強い場面に。
- 書き方の例：「soft light, the edge between light and shadow is a gentle gradient」「hard light, the line between light and shadow is crisp」

## ④ 光るものを画面に入れる
- ランプ・ろうそく・窓など、光の元を画面の中に入れます。
- 画面に光る物があると、「この光はここから来ている」と分かり、奥行きも出ます。
- 書き方の例：「a lit lamp stands behind the subject, clearly in the frame」

## ⑤ 背景を先に照らす・薄いもや（ヘイズ）で光の筋
- 人だけを照らすと、暗闇に浮いて見えます。背景を低く照らしてから、人を少しだけ明るくします。
- 部屋に薄いもや（ヘイズ）を入れると、窓の光が筋になって見えます。
- 書き方の例：「the background is lit at a low, warm level, but stays darker than the face」「a light atmospheric haze, visible shafts of light」

---

## 色は後から
- 光のプロンプトに、色補正の言葉（teal and orange、color grade、LUT など）を混ぜません。
- 色補正の言葉を混ぜると、光の向きや影より、色が先に変わってしまいます。
- 色は、光を決めたあとに、編集ソフトの LUT などで付けます。
- ただし、光そのものの色（ろうそくの暖かい色・月明かりの青・ネオンのピンク）は書いてかまいません。これは光の説明です。
