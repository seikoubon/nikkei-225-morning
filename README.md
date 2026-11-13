# 日経225先物｜朝の予測

[GitHub Pages](https://seikoubon.github.io/nikkei-225-morning/) · [更新元のサイト](https://nikkei-225-morning.seikou453202.chatgpt.site/)

大阪取引所・日経225先物ラージの日中始値から終値までの方向と騰落幅を表示する公開ダッシュボード。

- モデル：A7・ロジスティック回帰（方向）／Ridge回帰（騰落幅）。前日までの日経平均現物価格から計算した7特徴量を使用。
- 米国市場・為替・夜間先物は現行モデルの入力ではない。夜間終値は取得できた場合の参考表示。
- 本番予測と実績、過去検証2023–2024、参考2025–2026を分けて表示。
- 前営業日に保存した予測を正式採用した場合も、実際の発行時刻を保持する。

## ファイル

`public/index.html` は画面、`public/dashboard.json` は公開時点の本番記録、`public/history.json` は過去の予測・実績差の派生データ。学習用の元価格データや認証情報はこのリポジトリに含めない。

GitHub Pagesの配信データは、Actionsが更新元サイトの公開JSONを取得して生成する。予測の再計算は行わない。予約は平日06:55・07:25・16:55・17:55・21:55 JST。GitHubの予約実行は遅延する場合がある。画面下部の「記録更新」で元データの更新時刻を確認できる。

手動更新はActionsの `Publish forecast dashboard` → `Run workflow`。ローカルでの静的出力はPython 3.12以上で `python scripts/refresh.py _site`。

公開HTML・JSONは閲覧可能。更新元サイトへの書き込みは所有者認証が必要。
