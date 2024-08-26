import os
import shutil
from sklearn.model_selection import train_test_split

# Define paths
dataset_dir = 'dataset'
processed_data_dir = 'processed_data'

# Create the processed_data directory and subdirectories
os.makedirs(processed_data_dir, exist_ok=True)
train_dir = os.path.join(processed_data_dir, 'train')
val_dir = os.path.join(processed_data_dir, 'val')
test_dir = os.path.join(processed_data_dir, 'test')


# Helper function to split and copy data
def split_and_copy_data(source_dir, train_dest, val_dest, test_dest):
    categories = os.listdir(source_dir)
    for category in categories:
        category_path = os.path.join(source_dir, category)
        if not os.path.isdir(category_path):
            continue

        images = os.listdir(category_path)
        images = [img for img in images if img.endswith(('.png', '.jpg', '.jpeg'))]

        # Split the data into train, validation, and test
        train_imgs, val_test_imgs = train_test_split(images, test_size=0.3, random_state=42)
        val_imgs, test_imgs = train_test_split(val_test_imgs, test_size=0.5, random_state=42)

        # Create directories for the category
        os.makedirs(os.path.join(train_dest, category), exist_ok=True)
        os.makedirs(os.path.join(val_dest, category), exist_ok=True)
        os.makedirs(os.path.join(test_dest, category), exist_ok=True)

        # Copy files
        for img in train_imgs:
            shutil.copy(os.path.join(category_path, img), os.path.join(train_dest, category, img))
        for img in val_imgs:
            shutil.copy(os.path.join(category_path, img), os.path.join(val_dest, category, img))
        for img in test_imgs:
            shutil.copy(os.path.join(category_path, img), os.path.join(test_dest, category, img))


# Split and store leaf dataset
leaf_dataset_dir = os.path.join(dataset_dir, 'leaf dataset')
split_and_copy_data(leaf_dataset_dir, train_dir, val_dir, test_dir)

# Split and store plant dataset
plant_dataset_dir = os.path.join(dataset_dir, 'plant dataset')
split_and_copy_data(plant_dataset_dir, train_dir, val_dir, test_dir)

print(f"Data successfully split and stored in {processed_data_dir}")
