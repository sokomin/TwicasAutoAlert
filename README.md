# TwicasAutoAlert
ツイキャス始まったら自動で枠開きたい、通知個別に欲しい人向け

# 使い方

* 下回りは https://github.com/tamago324/PyTwitcasting を使ってます
```
pip install pytwitcasting
```
* ツイキャスアプリ登録ページにてAPI追加
  * https://apiv2-doc.twitcasting.tv/#introduction
  * Callback URLは http://localhost:8080 を指定。
  * config.pyに記載してあげてください
* 付属のバッチファイル叩けば実行してくれます
* タスクスケジューラに5～15分に一度指定をしておくと便利

