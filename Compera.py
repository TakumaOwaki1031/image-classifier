from PIL import Image
import numpy as np

# 1. Python側の前処理
img = Image.open("test.2.jpg").convert("RGB")
img = img.resize((128, 128), Image.BILINEAR)
py = np.array(img) / 255.0

# 2. Java側の前処理結果を読み込む ← ここに書く！
java_img = Image.open("test.2.jpg").convert("RGB")
java = np.array(java_img) / 255.0

# 3. 差分を計算
diff = np.abs(py - java)
print("max diff:", diff.max())
print("mean diff:", diff.mean())

