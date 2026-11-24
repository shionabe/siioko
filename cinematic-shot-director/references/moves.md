# カメラの動き 40種

動きは「何に合わせて動かすか」を1つ決めてから選ぶ（見せたい情報／登場人物の気持ち／見ている人の気持ち）。どれにも合わないなら、動かさない（1の固定）を選ぶ。

| # | 動き | 感じさせること | 使う場面 | プロンプトの英語 | AI での注意 |
|---|---|---|---|---|---|
| 1 | 固定 | 演技に委ねる・閉じこめる・冷たい観察 | 告白・静けさ・コメディの間・落ち着いた人物 | `one continuous locked-off camera, perfectly still for the whole shot` | 生成ではカメラを固定し、手持ちの揺れは編集で足すと安定 |
| 2 | 寄る（プッシュイン／ドリーイン） | ここが大事・決意・心の葛藤 | 気づき・決断の直前 | `a slow, steady push-in toward her face as she reads the last line — a physical dolly move, not a zoom` | 「slow cinematic push-in」ではなく、何に反応して寄るかを書く。ズーム（レンズで大きくする）とドリー（カメラが近づく）は別物で、人もよく混同する（CameraBench）。寄るなら「カメラが近づく」と書く |
| 3 | 引く（プルアウト／ドリーアウト） | 心が離れる・孤立・見捨てられる／状況を明かす | 余韻・ひとりになる・種明かし | `the camera slowly pulls away from her, a physical move; she stays still and small as the empty room grows around her` | 引いた最後に「wide shot」と書くと人物が大きく残る。最後の画面に見えるものを並べる |
| 4 | 上がりながら引く（ドローン・プルアウェイ） | 世界の大きさ・物語の終わり | ラスト・場所の全貌 | `the camera rises and pulls back at the same time, revealing the whole rooftop and the city` | 終わりの画に何が見えるかを書く |
| 5 | パン（横に振る） | 視線を移す・期待（ゆっくり） | 見ている物を追う・情報を見せる | `the background sweeps across the frame from frame-right to frame-left while she stays in the same place in the frame` | 軌跡ではなく「背景がどちらへ流れるか」で書かないと出ない |
| 6 | ウィップパン（素早く振る） | 勢い・関係・時間と場所の移動 | テンポの速いつなぎ | `a fast whip pan blurs across to the next scene` | 0.8秒未満は硬いカットになる。生成でウィップパンを作ると崩れやすい → 前後のカットを別に作り、編集の whip（ぼけて横流し）でつなぐ手もある |
| 7 | ティルト（縦に振る） | 大きさ・驚き・見上げる | 足元から顔へ・建物を見上げる | `the camera tilts up from her boots to her face` | — |
| 8 | 横移動（トラック） | 並走・世界の紹介・速さ（視差） | 歩く人と並ぶ・飛ぶ車と並ぶ | `the camera moves sideways with her at the same speed; the pillars in the foreground slide past while the city behind drifts slowly` | 固定カメラの前を横切るだけだと奥が動かず合成っぽい。横に動くと手前と奥がずれて（視差）本当にそこにいる感じが出る |
| 9 | 横移動で明かす（ラテラル・リビール） | 発見・登場 | 柱や壁の向こうから人物を出す | `the camera slides sideways past a concrete pillar and reveals her standing behind it` | — |
| 10 | 追う（トラッキング） | どこへ行く？ 着いたら何が？ | 歩く・逃げる・追う | `the camera follows close behind her at walking pace, keeping the same distance` | 追う側の速さ（km/h）と主従（誰が先・何歩遅れる）を書く。追う動きは、追う相手がいて初めて成り立つ（CameraBench）。誰を・どの距離で追うかを書く |
| 11 | 回り込み（アーク） | 止まった人物に動き・親密・パニック・英雄 | 立ち止まる・決めの瞬間・会話の緊張 | `the camera circles halfway around her at the same distance, keeping her in the centre` | 超広角（107°）＋回り込みは普通のワイドになった（②本目）。広角は 84° まで |
| 12 | 宙でスローの回り込み | 決めの一瞬を引き延ばす・仲間の顔を順に見せる | 跳んで宙にいる瞬間・飛び込み・爆発の直前 | `camera whips around them in one fast continuous circling move, extreme slow motion at a quarter speed` | スタートフレームを渡すとそのコマで止まり、回り込まない。止めっぱなし（hold）は「止まってる」と言われる。生成約3秒 → 編集で3倍速にして約1秒。回り込んだ先で顔の寄りへ順に whip |
| 13 | 空から回る（エアリアル・オービット） | 場所の中の人物・壮大 | 場所の紹介・ラスト | `high above, the camera circles slowly around her standing alone on the rooftop` | — |
| 14 | 真上で回る（オーバーヘッド・ローテーション） | 夢・めまい・神の視点 | 倒れる・眠る・振り付け | `straight down from above, the camera slowly rotates around her` | — |
| 15 | 上下（クレーン／ペデスタル） | 気持ちの上がり下がり・世界を見せる | 登場・見上げる・降りてくる | `the camera rises slowly from her shoes to above her head (a pedestal up), staying level` | ティルト（向きを変える）とペデスタル（高さを変える）は別物。どちらかを書く |
| 16 | 低い位置で回り込む（ロー・アングル・アーク） | 英雄・迫力 | 決めのポーズ・登場 | `from knee height, the camera arcs around her, looking up` | — |
| 17 | ドリーズーム（めまい効果） | 内面の葛藤・世界がゆがむ／ふたりが近づく | 気づいてしまった瞬間 | `her size stays the same while the space behind her stretches away` | AI では出にくい。出なくても困らない場面だけ |
| 18 | 回転（カメラロール） | 平衡が崩れる・力関係の逆転 | パニック・悪役が上に立つ | `the frame slowly rolls a quarter turn around her` | — |
| 19 | 手持ち | 今起きている・ドキュメンタリー・パニック | のぞき見・混乱 | `light handheld sway that drifts with a breath, two small bumps, no jitter` | 「スマホで撮った」「撮っている人」と書くと人やスマホが映る。揺れは編集で足す方が確実 |
| 20 | クラッシュズーム | 文末の「！」・驚き・笑い | 気づき・オチ | `a sudden crash zoom onto her face` | 【v16】カメラの中のクラッシュズームは冒頭の掴みに効く：`like someone jamming the zoom button … overshoots a little, wobbles and settles; the focus hunts and snaps sharp`。ズームアウトは編集で付ける |
| 21 | ピント送り | 気づいた相手を観客に見せる | 手前の物 → 奥の人／肩越し → 相手 | `focus slides from the curtain edge 1.2 m away to her face 3 m away` | レンズの最短撮影距離（85mm は約1m）より手前に合わせない |
| 22 | ゆっくりズーム | じわじわ迫る緊張・人の目にない不自然さ | 不安・何かがおかしい・見つめられている | `the view slowly tightens on her face while the camera itself stays still` | 私たちは「寄るならドリー（M-PUSHIN）、ズームと書かない」で通してきた。ズームのまま書くと、背景の大きさが変わらず平たく見える。わざと不自然さを出したいときだけ。CameraBench でもズームは「レンズの変化」、前進は「カメラの移動」と分けている |
| 23 | 前を後ろ向きに下がる（歩きながら話す） | 会話の勢い・一緒に歩いている | 歩きながらの会話・決意して進む | `the camera moves backward just ahead of her at her walking pace, her face and shoulders held in frame as the street unfolds behind her` | M-TRACK（後ろから追う）の逆。顔が見え続ける。研究では lead-tracking（被写体の前を後ろ向きに下がる）と呼ぶ |
| 24 | 追いかける（追いつけない） | 切迫・逃げる／追う | 逃走・追跡 | `the camera races after her from behind, struggling to keep up, the walls rushing past` | 揺れは強めに出やすい。読みやすさを保つなら M-TRACK |
| 25 | 地面すれすれで並走（足元・車輪） | ざらつき・正体を隠す・速さを床で感じる | 登場の前振り・足音・車輪 | `the camera skims along at ground height beside her boots, the floor rushing through the frame` | 顔を見せずに誰かを予感させる（A-WORM の動く版）。「速い」と書くより、カメラの高さ（地面すれすれ・耳の高さ）と、レンズのすぐ前を物がかすめることを書く方が速さが出る（VideoGen の作例） |
| 26 | 短い横移動（スライダー） | 上品な奥行き・小さな発見 | 物の寄り・室内の狭い所・商品 | `the camera glides a short distance to the left; the bottle in the foreground slides faster than the shelf behind it` | M-TRUCK の小さい版。手前の物を入れると視差がはっきり出る |
| 27 | 寄って横をすり抜け、奥を見せる | 場面転換・発見・勢い | 人物の向こうにあるものを明かす | `the camera travels straight toward her, slips close past her shoulder and continues into the room beyond, revealing the open window` | 終わりに何が見えるかを書く |
| 28 | 体に固定（スノリカム） | めまい・酔い・強い主観 | パニック・酔う・追いつめられる | `the camera is fixed to her body, her face staying perfectly still in the frame while the whole street swings and lurches behind her` | 顔が止まり背景だけが揺れる、を言葉で |
| 29 | 物を通り抜ける | あり得ない連続・夢・世界の入れ替わり | 額縁・窓・鍵穴・壁を抜けて別の場所へ | `the camera keeps moving forward and passes straight through the painting's frame into the painted world, without slowing` | トレンド17 で「額縁の中を後ろ向きに通り抜ける」引きが通った。参照画像の額縁は「画」として貼られるので文で書く |
| 30 | タイムラプス（時間を縮める） | 時間の経過・変化 | 待つ・季節・一日の移り変わり | `the camera stays still while hours pass in seconds: clouds race, shadows sweep across the floor, the light turns from morning to dusk` | — |
| 31 | 地球まで引く | とてつもないスケール・ひとりの小ささ | ラスト・世界の大きさ | `starting close on her, the camera accelerates backward: the street, the city, the coastline, then the whole planet, her spot kept in the centre` | — |
| 32 | 無限ズーム（入れ子） | 催眠・あり得ないスケール | 絵の中の絵・夢の中の夢 | `the camera pushes endlessly forward; each scene opens into another complete scene inside it` | — |
| 33 | スピードランプ（途中だけスロー） | 衝撃・見せ場のリズム | アクションの決め・ジャンプ・ぶつかる瞬間 | `real speed, then the moment she leaves the ground slows almost to a stop, then snaps back to full speed as she lands` | 生成より編集で速さを変える方が確実 |
| 34 | バレットタイム（止まった時間を回る） | 一瞬の永遠・見せ場 | 跳躍・水しぶき・ぶつかる瞬間 | `time freezes mid-leap; the camera sweeps halfway around her while she hangs motionless in the air` | — |
| 35 | スローモーション | 一瞬の美しさ・重さ・余韻 | 水しぶき・髪・布・落ちる物・決めの瞬間 | `in slow motion, the drops of water hang in the air around her as her hair swings through the backlight` | 宙で止まる物を1つ決めて書くとスローが決まる（VideoGen）。ふつうの速さとスローを1つのショットに混ぜない（公式の書き方） |
| 36 | Steadicam / Gimbal (ステディカム / ジンバル) | 没入感、夢の中のような滑らかさ、終わらない追跡 | 迷路や長い廊下の移動、ダンスシーン | `Smooth Steadicam shot, fluid gliding camera movement, tracking closely behind character` | 最も「プロの映画」に見える動き。手ブレのない浮遊感がAIの動画補間と非常に相性が良い |
| 37 | FPV Drone (FPVドローン / レーシング飛行) | 圧倒的アドレナリン、超人的視点、スピードの狂気 | 近未来都市のチェイス、断崖絶壁の急降下 | `Fast FPV racing drone shot, dynamic acrobatics, skimming ground and banking sharply` | KlingやWan 2.1で極めてダイナミックに出力される。背景動画の生成として最高品質を誇る |
| 38 | POV Bodycam (ボディカメラ / 警察・兵士視点) | 生々しい現場記録、FPSゲーム感、切迫した危険 | 特殊部隊の突入、警察の現場検証 | `Police bodycam perspective, gritty chest-mounted wide angle, high-speed tactical advance` | 画面の隅に時刻コード（Timestamp）や魚眼の歪みをプロンプトで足すと、AIが実録映像化する |
| 39 | Shake-to-Lock (激震からの急停止) | 驚愕、静寂への急転落、息をのむ緊張感 | 爆発直後の静寂、銃声が止んだ瞬間 | `Camera violently shaking then suddenly coming to a complete dead halt on character's eyes` | 動から静へのギャップ演出。ショート動画のテンポコントロールに抜群の威力を発揮 |
| 40 | Dutch Roll Track (傾斜ローリングトラック) | 世界の秩序の破綻、悪夢の疾走、逃げ場のない狂気 | 精神病棟の廊下を疾走するシーン | `Canted Dutch angle tracking shot, gliding sideways through hallway at tilted 30-degree angle` | 静止したダッチアングルよりさらに不穏さが増す。サイコホラー動画のキラーショット |
