import os
import shutil
import random

# Define the paths to your own dataset directory
dataset_dir = "/home/saadalam/Desktop/Endoscopic_image_Analysis_dataset/"

# Define the output directory where you want to store the result dataset
output_dir = "endoscopic"

output_subdirs = ["instrument", "poly-p", "ulceratic-colitics"]

for subdir in output_subdirs:
    os.makedirs(os.path.join(output_dir, subdir, "images"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, subdir, "labels"), exist_ok=True)


# List all annotation .txt files in the labels directory
label_files = [
    file
    for file in os.listdir(os.path.join(dataset_dir, "labels"))
    if file.endswith(".txt")
]

# Shuffle the list to randomize the order
random.shuffle(label_files)

# Iterate through the annotation .txt files and copy corresponding images
for label_file in label_files:
    image_file = label_file.replace(".txt", ".jpg")
    with open(os.path.join(dataset_dir, "labels", label_file), "r") as file:
        # Read the content of the .txt file
        content = file.readline()
        class_id = int(content.split()[0])  # Extract the class ID from the content
        shutil.copy(
            os.path.join(dataset_dir, "images", image_file),
            os.path.join(output_dir, output_subdirs[class_id], "images", image_file),
        )
        shutil.copy(
            os.path.join(dataset_dir, "labels", label_file),
            os.path.join(output_dir, output_subdirs[class_id], "labels", label_file),
        )

print("Dataset splitting and copying completed.")
