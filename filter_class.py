import os
import shutil
import cv2
import argparse

def copy_files_with_class_6(input_annotations_dir, output_annotations_dir, output_images_dir, desired_resolution):
    # Create the output directories if they don't exist
    if not os.path.exists(output_annotations_dir):
        os.makedirs(output_annotations_dir)
    if not os.path.exists(output_images_dir):
        os.makedirs(output_images_dir)

    # Loop through text files in the input directory
    for filename in os.listdir(input_annotations_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_annotations_dir, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                has_class_6 = any(line.split()[0] == '6' for line in lines)

            if has_class_6:
                # Extract the file name (excluding extension)
                file_name_no_ext = os.path.splitext(filename)[0]

                # Check if the corresponding image file exists
                image_filename = file_name_no_ext + ".jpg"  # Adjust the extension as needed
                image_path = os.path.join(input_annotations_dir, image_filename)
                if os.path.exists(image_path):
                    # Check the resolution of the image
                    image = cv2.imread(image_path)
                    height, width, _ = image.shape
                    if (height, width) == desired_resolution:
                        # Copy the text file to the output directory
                        shutil.copy(file_path, os.path.join(output_annotations_dir, filename))

                        # Copy the corresponding image file to the output images directory
                        shutil.copy(image_path, os.path.join(output_images_dir, image_filename))

    print("Text and image files with class 6 and the required resolution", desired_resolution, "copied to the output directories.")

#the code will start running from here.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy files with class 6 and desired resolution to output directories.")
    parser.add_argument("input_annotations_dir", help="Path to the input annotations directory")
    parser.add_argument("output_annotations_dir", help="Path to the output annotations directory")
    parser.add_argument("output_images_dir", help="Path to the output images directory")
    parser.add_argument("--resolution", default=(512, 512), type=int, nargs=2, help="Desired image resolution (height width)")
    
    args = parser.parse_args()
    copy_files_with_class_6(args.input_annotations_dir, args.output_annotations_dir, args.output_images_dir, tuple(args.resolution))
