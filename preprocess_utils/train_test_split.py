import os
import random
import shutil


# Set the path to your dataset directory
dataset_dir = "Dataset_dir"

# Define the output directories for training, validation, and testing
train_dir = "training"
val_dir = "validation"
test_dir = "testing"

# Define the split ratios
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# Ensure the output directories exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)
# Get a list of all image files in the images directory
image_files = [
    file
    for file in os.listdir(os.path.join(dataset_dir, "images"))
    if file.endswith(".jpg")
]

# Shuffle the list of image files
random.shuffle(image_files)

# Calculate the split points
num_images = len(image_files)
num_train = int(train_ratio * num_images)
num_val = int(val_ratio * num_images)

# Split the data
train_images = image_files[:num_train]
val_images = image_files[num_train : num_train + num_val]
test_images = image_files[num_train + num_val :]


child_directory = ["images", "labels"]

os.makedirs(os.path.join(val_dir, child_directory[0]), exist_ok=True)
os.makedirs(os.path.join(val_dir, child_directory[1]), exist_ok=True)

os.makedirs(os.path.join(train_dir, child_directory[0]), exist_ok=True)
os.makedirs(os.path.join(train_dir, child_directory[1]), exist_ok=True)

os.makedirs(os.path.join(test_dir, child_directory[0]), exist_ok=True)
os.makedirs(os.path.join(test_dir, child_directory[1]), exist_ok=True)

listq = []
# Copy image files and corresponding label files to their respective directories
for image_file in train_images:
    annotation_file = image_file.replace(".jpg", ".txt")
    # print(len(annotation_file))
    shutil.copy(
        os.path.join(dataset_dir, "images", image_file),
        os.path.join(train_dir, "images"),
    )
    shutil.copy(
        os.path.join(dataset_dir, "labels", annotation_file),
        os.path.join(train_dir, "labels"),
    )

for image_file in val_images:
    annotation_file = image_file.replace(".jpg", ".txt")
    shutil.copy(
        os.path.join(dataset_dir, "images", image_file), os.path.join(val_dir, "images")
    )
    shutil.copy(
        os.path.join(dataset_dir, "labels", annotation_file),
        os.path.join(val_dir, "labels"),
    )

for image_file in test_images:
    annotation_file = image_file.replace(".jpg", ".txt")
    shutil.copy(
        os.path.join(dataset_dir, "images", image_file),
        os.path.join(test_dir, "images"),
    )
    shutil.copy(
        os.path.join(dataset_dir, "labels", annotation_file),
        os.path.join(test_dir, "labels"),
    )

print(
    "Dataset split into training, validation, and testing sets with corresponding annotation files."
)
