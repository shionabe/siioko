# ショット 28種（大きさ9＋アングル19）

ショットの大きさは「観客に渡す情報の量」、アングルは「誰の目で見るか・力関係」を決める。

| # | 種類 | ショット | 感じさせること | 使う場面 | プロンプトの英語 | AI での注意 |
|---|---|---|---|---|---|---|
| 1 | 大きさ | 超引き（エクストリーム・ワイド） | 場所のスケール・人の小ささ・孤立 | 場面の始まり（どこにいるか）／広い世界にひとり | `an extreme wide shot: the landscape fills the frame; she is a tiny figure you could almost miss` | 人物はほぼ判別できない大きさ。主役の顔が要る場面には使わない |
| 2 | 大きさ | 場所が主役の引き（ベリー・ワイド） | 何が起きる場所かは分かるが、人物はまだ強調されない | 人物を小さく、空間を大きく見せたいとき（AI で人物が大きくなりがちな時の第一候補） | `a very wide establishing shot: the place itself is the subject and she is not yet emphasized; a small figure low in the frame` | 「wide shot」と書くと人物が画面いっぱいの全身になる（テスト02・03 で 40〜45% 止まり）。very wide＋見下ろし＋手前の物で 27% まで小さくなった（テスト04） |
| 3 | 大きさ | 全身（ワイド・ロング・フル） | 立ち位置と体の動き | 全身の動き・服を見せる | `a full-body shot: head to shoes in frame, a little floor below her feet` | 全身が入る＝人物が画面いっぱいになる言葉。空間を見せたいなら S-VWS |
| 4 | 大きさ | 膝から上（ミディアム・ワイド／カウボーイ） | 体の動きと表情の両方 | 歩く・振り返る・2人の対立（手前に1人・奥に1人） | `a medium-wide shot from the knees up, head fully in frame` | — |
| 5 | 大きさ | 腰から上（ミディアム） | 会話の距離・ふつうの人の距離 | 会話・やりとり | `a medium shot from the waist up` | — |
| 6 | 大きさ | 胸から上（ミディアム・クローズアップ） | 表情と身ぶり | 会話の受け・反応 | `a medium close-up from the chest up` | — |
| 7 | 大きさ | 顔（クローズアップ） | 感情を近くで感じる | 気づき・涙・決意 | `a close-up: her face fills most of the frame` | キャラクターシートだけ渡すと寄れない（シートが全身へ引っぱる）。カットを分けて「画面に見えるもの」で書く |
| 8 | 大きさ | 部分（エクストリーム・クローズアップ） | ここが大事・緊張 | 目・指先・手紙の文字。超引きの直後に置くと落差で効く（T-LEONE） | `an extreme close-up of her eyes only; the top of the frame cuts her forehead` | 1ショットで変えられる大きさは約3倍まで。超引きから寄るならカットを分ける |
| 9 | 大きさ | 物の寄り（インサート） | この物は大事／人物が見ている物 | 手紙・画面・鍵・カード | `an extreme close-up insert of the letter on the nail, held still for a beat` | 意味のない寄り（時計・靴）は観客を混乱させる。物語に関係する物だけ |
| 10 | アングル | 目の高さ | 自然・人物を裁かない | ふつうの会話・観客と同じ目線 | `the camera at her eye level, level and steady` | — |
| 11 | アングル | 煽り（下から見上げる） | 力・迫力・英雄／悪役 | 決めの瞬間・強さを見せる | `low angle from knee height looking up at her; the sky and the ceiling loom behind her` | 人物がまわりより小さく入ると「驚き・荘厳」に変わる |
| 12 | アングル | 地面すれすれ（ワームズ・ビュー） | ドラマチック・見慣れない | 足元から始まる・人物の先に何かがある予感 | `the camera lies almost on the floor, 8 cm high, tilted steeply up: she stands full-length in the centre and the tall window looms above her` | アートホテル③で本人提案の「床スレスレ・背後から煽り」がそのまま出た（成功例） |
| 13 | アングル | 俯瞰（見下ろす） | 小ささ・弱さ・罪の重さ | 孤立・追いつめられた場面 | `seen from high above on the stairs, looking down on her; she is small in the frame` | 封竜学院テスト04：階段の途中から見下ろす＋手前の縁で人物が初めて30%を切った |
| 14 | アングル | 真上（神の視点） | 突き放した客観・切り離された人 | 状況が分からない人・複雑な動き・振り付け | `a straight-down overhead view from directly above her` | 真上からの俯瞰（床の円＋日だまり）は安定して出る |
| 15 | アングル | 空撮（ドローン） | 大きな世界の中の人物・場所の紹介 | 場所の確立・旅 | `an aerial view from high above the rooftops` | ドローンの大旋回は AI の定番＝やりすぎると AI っぽい |
| 16 | アングル | 傾き（ダッチ） | 不安・何かがおかしい | 緊張が高まる場面（高まるほど傾ける） | `the horizon tilts slightly, more as the tension rises` | ①本目で「画角を斜めにするだけ」では不穏感が出なかった。不穏は光（部屋の光を低く・顔は片側だけ）の方が効く。CameraBench ではロール（傾き）を回転の1つとして扱う。ダッチは「傾いたまま」、M-ROLL は「回っていく」。【v16】怒りは「ダッチ約15度（画面全体を時計回りに）＋構えて叩き割る」。水平の画面は「力が感じられない」 |
| 17 | アングル | 肩越し | 話しかけられている側・関係 | 会話・相手を見る | `over her right shoulder: the soft back of her head fills the frame-left quarter; he is sharp beyond` | 「右肩越し」と書いても、肩が画面のどちらに入るかは向きで変わる。肩が画面のどちらに入るかで書く。並んで座る2人の肩越しは幾何的に撮れない |
| 18 | アングル | 主観（POV） | その人の目で見る・一緒に体験する | 扉を開ける・何かを見つける・恋 | `her own point of view: the camera IS her eyes; we look out of her, never at her` | クリップの先頭に置く。客観の後に置くと客観に戻る。Wan で前方の POV を書くと前にもう1台の車が出た |
| 19 | アングル | 自撮り | SNS の日常・本人の語り | 冒頭のフック・旅の記録 | `a proper arm's-length selfie at about 50 cm, on the phone's normal 1x main camera (~26 mm)` | 0.5x（超広角）を書くと丸い黒縁が出て POV にも伝染した。黒縁・fisheye の単語を書かない |
| 20 | アングル | 物の視点（見慣れない視点） | SNS で手を止める・のぞき見られる恐怖 | 炉の中から・トランクの中から・額縁の内側から・画面の中から | `seen from inside the furnace, through the flames, looking out at her face lit by the fire` | 実写では置けない場所でも AI なら置ける＝AI 動画がいちばん得をする視点 |
| 21 | アングル | 少し上から（10〜15°） | 自然で好ましい・顔がきれいに見える | ふつうの寄り・ポートレート・商品 | `the camera just above her eye line, looking down at her only a little` | 商品撮影の角度の表：真上90°／鳥の目65°／ハイ45°／上から30°／少し上10〜15°／正面0°／ヒーロー−15°／ロー−45°／地面すれすれ−75°。角度の数字が効くかは未確認なので、文は「目の高さより少し上」の言葉で |
| 22 | アングル | 少し下から（ヒーロー・−15°） | 堂々・頼もしい（A-LOW ほど大げさでない） | 登場・決意・商品を立派に見せる | `the camera a little below her chest height, tilted gently up at her` | A-LOW（膝の高さ・−45°）と A-WORM（地面すれすれ・−75°）の手前の段。迫力を出しすぎたくないときに |
| 23 | アングル | 後ろから（同じ方向を見る） | 期待・一緒に発見する | 扉を開ける・景色を前にする | `the camera stands directly behind her, looking the same way she is facing; her back fills the lower frame and the view ahead opens beyond her` | トレンド18② では左右を守るため後ろからが多すぎた（顔が見えない）。見せ場の顔は前側から |
| 24 | アングル | 腰の高さ | 地に足のついた・くだけた | 歩く・西部劇の決闘・日常 | `the camera at her hip height, level, looking slightly up at her face` | — |
| 25 | アングル | 真横（プロフィール） | 観察・シルエットがはっきり | 考える横顔・向かい合う2人 | `seen directly from the side, her profile clean against the dark wall` | 封竜学院テスト05 の横顔の寄りで使った |
| 26 | アングル | 斜め（スリークォーター） | 立体感・自然なポートレート | ふつうの寄り・会話 | `seen from about 45 degrees off her front, both the front and the side of her face readable` | — |
| 27 | アングル | ツーショット | 関係・距離・緊張 | 2人の会話・並ぶ・対立 | `both of them in one frame, the gap between them clearly readable` | 2人の距離で関係を見せる（近い＝親密・遠い＝心の距離） |
| 28 | アングル | さかさま | 非現実・ショック・世界がひっくり返る | 夢・倒れる・価値観が変わる瞬間 | `the whole frame is turned upside down; she stands on what looks like the ceiling` | — |
