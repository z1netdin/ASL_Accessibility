import os
import random
import shutil

# Paths
base_path = "datasets/asl_alphabet/images"
train_path = os.path.join(base_path, "train")
val_path = os.path.join(base_path, "val")

# Create val/ folders
os.makedirs(val_path, exist_ok=True)

# For each class folder (A, B, C, ..., Z)
for class_name in os.listdir(train_path):
    class_train_path = os.path.join(train_path, class_name)
    class_val_path = os.path.join(val_path, class_name)

    # Skip anything that is not a folder
    if not os.path.isdir(class_train_path):
        continue

    # Create val class folder if not exist
    os.makedirs(class_val_path, exist_ok=True)

    # List image files in the class folder
    images = [f for f in os.listdir(class_train_path) if f.endswith(('.jpg', '.png', '.HEIC'))]

    # Shuffle and pick 20%
    val_count = int(len(images) * 0.2)
    val_images = random.sample(images, val_count)

    # Move images to val folder
    for img in val_images:
        src = os.path.join(class_train_path, img)
        dst = os.path.join(class_val_path, img)
        shutil.move(src, dst)

    print(f"Moved {val_count} images to val/{class_name}")

print("\nDone! Your dataset is now split into train/ and val/")
