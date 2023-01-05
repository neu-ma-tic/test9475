# FortniteBot For Discord
## 詳細
Botバージョン:1.0.0<br>
LICENSE:MITLICENSE

## 導入
### 起動方法
まず[DiscordDeveloperPortal](https://discord.com/developers/applications/)へアクセスします<br>
ここで右上のNewApplicationを押してここからBotを作成します<br>
Botの名前を自由に決めて作成してください<br>
(Botの作成が分からない方は[こちら](https://discordpy.readthedocs.io/ja/latest/discord.html)のサイトを参考にしてください)<br>
BotのTokenが取得出来たら`config.json`の`token`の項目へ入れてください<br>
これでRunするとBotが起動するはずです
分からないことなどは[Discordサーバー](https://tel1hor.tel1horjp.repl.co/tel1horserver.html)で質問してください

### APIKeyについて
`stats`コマンドを使用するためには[Fortnite-api.com](https://fortnite-api.com/)のAPIKeyが必要です<br>
取得については書きませんが`config.json`の`apikey`の項目に入れることで使用することができます

### 解説
#### ファイルごとの解説
|ファイル名|詳細|
|-|-|
|main.py|Botの中心となる部分。<br>改造は上級者向け。|
|config.json|BotのTokenなどを入れたりするファイル。<br>Pythonに詳しくない限りこのファイル以外は触らないほうがいいと思われる。|
|value.json|触らないでください。|
|README.md|Botの仕様書。<br>ここの説明を読みながら起動することを推奨する。|
|LICENSE|Botのライセンス。<br>消さないでください。|

#### config.jsonの解説
|キー|データ|
|-|-|
|token|BotのTokenを入れるところ。|
|prefix|Botのコマンドのはじめにつける文字列。<br>初期設定は`fn.`|
|apikey|`stats`コマンドを使用する際に必要。<br>[Fortnite-api.com](https://fortnite-api.com/)から取得できる。|
|color|Embedのカラー。Hexで指定できる。<br>特にいじらなくても動くので問題なし。|

#### コマンドの解説
すべてのコマンドのはじめに`prefix`をつけて使用することができる。<br>
`prefix`は`config.json`内の項目で設定できる<br>
初期設定は`fn.`になっている<br>

|コマンド名|説明|使用方法|
|-|-|-|
|help|Botのコマンド一覧などを出したりするコマンド|なし|
|item|アイテムを検索できる|item [アイテム名]|
|brnews|現在のバトルロワイヤルのニュースを取得できる|なし|
|stats|プレイヤーの戦績を見ることができる<br>使用には`APIKey`の書き込みが必要|stats [ユーザー名]|
|shop|現在のデイリーショップの画像を取得できる|なし|

## その他
### 使用API
[Fortnite-api.com](https://fortnite-api.com/)<br>
[Nitestats.com](https://nitestats.com/)
