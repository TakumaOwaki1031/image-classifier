from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rescale=1.0/255,
    validation_split=0.2
)

train_data = datagen.flow_from_directory(
    "faces",
    target_size=(128, 128),
    color_mode="rgb",
    class_mode="categorical",
    batch_size=32,
    subset="training"
)

print(train_data.class_indices)
