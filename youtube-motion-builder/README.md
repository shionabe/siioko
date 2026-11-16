# youtube-motion-builder（モーション構築スキル）

YouTube・SNS の動画の「モーション（図や文字が動いて出てくる演出）」を、見本探しから Claude での再現・保存まで一緒に進める Claude 用のスキルです。

- 最初に「どこで使う動きか」を選んで答える形で聞きます
- Pinterest・Instagram・YouTube で探すための**検索ワード**（英語・日本語）が出ます
- 気に入った見本の動画を貼ると、動きを分解して、**Claude にそのまま貼れる依頼文**を作ります
- 再現して見本と並べて確かめ、うまくいった動きは**名前を付けて保存**。次から一言で呼び出せます

## 入れ方

**claude.ai（ブラウザ・アプリ）**
1. ここから `youtube-motion-builder.skill` をダウンロード：https://github.com/shionabe/siioko/raw/master/youtube-motion-builder.skill
2. claude.ai の「設定 → Skills → 追加 → Skills をアップロード」で、ダウンロードしたファイルを選ぶ

**Claude Code**
```
git clone https://github.com/shionabe/siioko.git
cp -r siioko/youtube-motion-builder ~/.claude/skills/
```

## 使い方
「モーションを作りたい」と話しかけるだけ。見た目の決まり（色・文字）がまだなら、先に youtube-design-system-builder を使うと仕上がりがそろいます。

---
AI動画ラボ（YouTube）「Claude に自動編集させて、自分らしい動画にする方法」の配布物です。
