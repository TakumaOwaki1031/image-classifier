# image-classifier
TnsorFLow learning model with java
Java から TensorFlow SavedModel を読み込み、画像分類を行うコンポーネントです。
モデルの学習は Python（TensorFlow）で行い、推論は Java（Gradle プロジェクト）で実行します。

【特徴】
• 	Python + TensorFlow による モデル学習
• 	SavedModel 形式でのモデル保存
• 	Java（TensorFlow Java API）での推論
• 	画像前処理（リサイズ・正規化）を Python/Java で統一
• 	Gradle によるビルド・実行
• 	個人情報などは除外済み

【使い方】
1. 画像データの変換（BatchConverter.java）
分類したい画像を 最大 2 枚 用意してください。
以下の設定を、あなたの環境に合わせて変更します。

String[] classes = {"ME", "OTHER"};
String inputRoot = "raw/faces/";      // ← ここを目的の画像フォルダに変更
String outputRoot = "converted/faces/";

設定後、 を実行すると、
画像が学習用フォーマットに変換され、 converted/faces/に保存されます。

2. モデルの学習（model.train.py）
Python で学習スクリプトを実行します。

python model.train.py

学習が完了すると、 ディレクトリが生成されます。
このモデルを Java 側で使用します。

3. 推論 UI の起動（App.java）
Java 側のメインクラス App.java を実行します。

gradle run

UI が表示されるので、判定したい画像を選択してください。
モデルが me / other のどちらかを推論します。

【環境】
• 	Python 3.13.1
• 	TensorFlow 2.20.0
• 	Java 21.0.8
• 	Gradle 8.14.4
• 	Windows 11
