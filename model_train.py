from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization

from tensorflow.keras.preprocessing.image import ImageDataGenerator

# -----------------------------
# 1. データ読み込み（自作データ）
# -----------------------------
datagen = ImageDataGenerator(
    rescale=1.0/255,
    validation_split=0.2,
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1
)

train_data = datagen.flow_from_directory(
    "converted/faces",     # ← Javaで保存した前処理済み画像
    target_size=(128, 128),
    color_mode="rgb",
    class_mode="categorical",
    batch_size=32,
    subset="training"
)

val_data = datagen.flow_from_directory(
    "converted/faces",     # ← 同上
    target_size=(128, 128),
    color_mode="rgb",
    class_mode="categorical",
    batch_size=32,
    subset="validation"
)


# -----------------------------
# 2. モデル構築（強化版3層CNN）
# -----------------------------
model = Sequential([
    # 第1層
    Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
    BatchNormalization(),
    MaxPooling2D(),
    
    # 第2層
    Conv2D(64, (3,3), activation='relu'),
    BatchNormalization(),
    MaxPooling2D(),

    # 第3層
    Conv2D(128, (3,3), activation='relu'),
    BatchNormalization(),
    MaxPooling2D(),


    Flatten(),

    Dense(128, activation='relu'),
    Dropout(0.5),

    Dense(2, activation='softmax')  # takuma / other の2クラス
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# -----------------------------
# 3. 学習
# -----------------------------
model.fit(
    train_data,
    validation_data=val_data,
    epochs=10
)

# -----------------------------
# 4. 保存
# -----------------------------
model.export("saved_model")
print("SavedModel saved in ./saved_model/")
print(train_data.class_indices)






