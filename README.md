# AI動画ラボの配布スキル（Claude 用）

YouTube「AI動画ラボ」の動画で紹介した仕組みを、だれでも使える形にしたスキルです。

| スキル | できること |
|---|---|
| [youtube-design-system-builder](#youtube-デザインシステム構築スキル) | 集めた参考画像から、動画の「見た目の決まり」と見本帳（HTML）を作る |
| [youtube-motion-builder](#youtube-モーション構築スキル) | 動きの見本の探し方（検索ワード）と、Claude への頼み方・再現・保存 |
| [short-video-auto-edit](#ショート動画の半自動編集スキルclaude-用) | ショート動画1本を、台本から投稿の準備まで |
| [cinematic-lighting](#光のプロンプト50種cinematic-lighting) | 画像・動画の光だけを変えてシネマティックに（光50種） |
| [cinematic-color-grades](#カラーグレーディング62種cinematic-color-grades) | 画像・動画に映画の色を LUT でかける（62種・LUT つき） |
| [cinematic-shot-director](#ショート構図カメラワークの提案cinematic-shot-director) | やりたいことと気持ちを答えるだけで、ショット・構図・カメラワークを2案とプロンプトで提案（構図26・ショット28・カメラワーク40） |

---

# YouTube デザインシステム構築スキル

Claude に「いい感じに」と頼んでも、あなたの「いい感じ」は伝わりません。色・文字・背景・使わない物までを言葉にして渡すと、AI と認識がそろいます。このスキルは、あなたが Pinterest などで集めた画像から、その「言葉」を一緒に作ります。

- 画像を貼ると、Claude が画像を読み、**7つの質問を1つずつ、選んで答える形**で聞いてきます（印象・色・文字・小さな印・背景・カードの見た目・やらないこと）
- 毎回、Pinterest と Google Fonts で探すための**検索ワード**も出ます
- 最後に **見本帳（1つの HTML ファイル）** と、AI に毎回渡す **design-system.md** ができます
- 上品・ポップ・ダーク・かわいい など、ジャンルは問いません

## 入れ方

**claude.ai（ブラウザ・アプリ）**
1. このページの一覧にある `youtube-design-system-builder.skill` を開き、右上の「ダウンロード」ボタン（↓）で保存
2. claude.ai の「設定 → Skills → 追加 → Skills をアップロード」で、保存したファイルを選ぶ

**Claude Code**
```
git clone https://github.com/shionabe/siioko.git
cp -r siioko/youtube-design-system-builder ~/.claude/skills/
```

## 使い方
Claude に「デザインシステムを作りたい」と話しかけて、集めた画像を貼るだけ。

---

# YouTube モーション構築スキル

AI は動きが苦手と言われますが、**動きの見本を見せる**と、テンポや出し方までかなり再現してくれます。このスキルは、見本の探し方から Claude への頼み方、保存して使い回すまでを一緒に進めます。

- 「どこで使う動きか」（章の区切り・目次・数字・流れ図・文字の出し方 など）を、選んで答える形で聞いてきます
- Pinterest・Instagram・YouTube で探すための**検索ワード**（英語・日本語）が出ます
- 気に入った見本を貼ると、動きを分解して、**Claude にそのまま貼れる依頼文**を作ります
- 再現して見本と並べて確かめ、うまくいった動きは名前を付けて保存。次から一言で呼び出せます

## 入れ方

**claude.ai（ブラウザ・アプリ）**
1. このページの一覧にある `youtube-motion-builder.skill` を開き、右上の「ダウンロード」ボタン（↓）で保存
2. claude.ai の「設定 → Skills → 追加 → Skills をアップロード」で、保存したファイルを選ぶ

**Claude Code**
```
git clone https://github.com/shionabe/siioko.git
cp -r siioko/youtube-motion-builder ~/.claude/skills/
```

## 使い方
Claude に「モーションを作りたい」と話しかけるだけ。

---

# ショート動画の半自動編集スキル（Claude 用）

TikTok・Instagram リール・YouTube ショートの動画1本を、Claude に係を分けて任せて作るスキルです。
**台本 → 素材 → 編集 → 投稿の準備**まで Claude が進め、あなたは「方向を決める」と「仕上がりの確認」だけ。

YouTube「AI動画ラボ」の動画で紹介した仕組みを、だれでも使える形にしたものです。

## できること
1. **最初の聞き取り**：商材・ブランド・アカウント・キーワード・編集ソフトなどを聞いて、設定ファイルに保存（2回目から聞かない）
2. **見本の動画の分析**：伸びている動画の「なぜ伸びたか」を、テロップや切り替えまで分解
3. **台本と法律の壁打ち**：切り口 → 冒頭の言葉 → 台本。薬機法・景品表示法・ステマ規制などの「目安」チェック
4. **素材の設計**：手持ちで足りる所／撮る所／AI で作る所／編集で描く所を分ける
5. **編集**：仮編集 → 本編集。完成の MP4、または編集ソフト用のファイル・並べ方の表
6. **確認**：書き出した動画を Claude が自分でチェック
7. **投稿の準備**：キャプション・ハッシュタグ・日時（ブラウザ操作ができれば予約まで。ボタンを押す前に必ず確認）

## 入れ方
### claude.ai（ブラウザ・アプリ）
1. このページの一覧にある `short-video-auto-edit.skill` を開き、右上の「ダウンロード」ボタン（↓）で保存
2. claude.ai の「設定 → Skills → 追加 → Skills をアップロード」で、保存したファイルを選ぶ

### Claude Code
ターミナルで次の2行を実行します。
```bash
git clone https://github.com/shionabe/siioko.git
cp -r siioko/short-video-auto-edit ~/.claude/skills/
```

## 使い方
Claude に「ショート動画を作りたい」と話しかけるだけ。最初に聞き取りが始まります。

## 使う環境で、できることが変わります
| 使う所 | できること |
|---|---|
| Claude Code（パソコン） | 全部（MP4 の書き出しには ffmpeg が要ります） |
| claude.ai のチャットだけ | 聞き取り・分析・台本・素材の表・チェック。編集は「並べ方の表」を見てご自身で |
| ブラウザ操作（Claude in Chrome など） | 見本をブラウザで見る・予約投稿 |

## 編集ソフト
どのソフトでも使えます。ソフトを使わなければ Claude が MP4 まで作ります。Premiere Pro・DaVinci Resolve・Final Cut Pro は編集ファイル（XML）も出します（読み込めるかは最初に短い動画で確かめてください）。CapCut は「並べ方の表」を見て並べる形です。

## ご注意
- 法律のチェックは**目安**です。最終の判断はご自身で（迷ったら専門家・メーカーに）
- 見本の動画・音楽をそのまま使わないでください（著作権・アカウントの評価）
- AI の生成でお金を使うときは、Claude が見積もりを出して確認します


---

# 光のプロンプト50種（cinematic-lighting）

AI に「シネマティックに」とだけ頼んでも、映画っぽくはなりません。足りないのは光の指定です。画像を Claude に入れて `/rembrandt-light` のようなコマンドを送ると、**光だけを変える**英語のプロンプトが返ってきます。

- 窓の光・レンブラント・ネオン・月明かり・逆光・ヘイズ・シルエットなど50種
- 「シネマティックにしたい」とだけ伝えると、場面に合う光を3つ提案
- Higgsfield の MCP をつないでいれば、そのまま画像も作れます（クレジットがかかるので、作る前に確認します）

## 入れ方
**claude.ai**：`cinematic-lighting/cinematic-lighting.skill` を開いて「ダウンロード」（↓）→ claude.ai の「設定 → Skills → 追加 → Skills をアップロード」
**Claude Code**：
```
git clone https://github.com/shionabe/siioko.git
cp -r siioko/cinematic-lighting ~/.claude/skills/
```

---

# カラーグレーディング62種（cinematic-color-grades）

画像や動画に、映画のような色を LUT でかけるスキルです。生成ではなく色を「かける」だけなので、クレジットはかかりません。

- ティール＆オレンジ・銀残し・テクニカラー・スプリットトーン・フィルムプリント・70年代ビンテージなどの色の型34種と、『真珠の耳飾りの少女』『グランド・ブダペスト・ホテル』『アメリ』など映画の色28種
- 画像や動画を Claude に入れて `/teal-and-orange` のようなコマンドを送ると、色をかけたファイルと元との見比べが返ってきます
- LUT だけ使いたい方は `cinematic-color-grades/cinematic-color-grades_LUT62.zip`（Premiere・DaVinci・Final Cut・Filmora・CapCut で使えます）

## 入れ方
**claude.ai**：`cinematic-color-grades/cinematic-color-grades.skill` を開いて「ダウンロード」（↓）→ claude.ai の「設定 → Skills → 追加 → Skills をアップロード」
**Claude Code**：
```
git clone https://github.com/shionabe/siioko.git
cp -r siioko/cinematic-color-grades ~/.claude/skills/
```

## ライセンス
MIT

---

# ショート・構図・カメラワークの提案（cinematic-shot-director）

キャラクターと背景の画像を渡して、「この人が何をするか」「どんな気持ちか」を答えるだけで、ショットの大きさ・構図・カメラワークを2案（王道／意外な案）と理由で提案し、そのまま貼れる英語のプロンプトまで書くスキルです。

- 中身：構図26種・ショット28種・カメラワーク40種
- 記事（構図26選）：https://higgsfield.ai/@shion_movie_creator/blogs/26-cinematic-compositions-jp

## 入れ方

**claude.ai**：`cinematic-shot-director/cinematic-shot-director.skill` を開いて「ダウンロード」（↓）→ claude.ai の「設定 → Skills → 追加 → Skills をアップロード」

**Claude Code**
```
git clone https://github.com/shionabe/siioko.git
cp -r siioko/cinematic-shot-director ~/.claude/skills/
```
