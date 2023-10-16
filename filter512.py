import cv2
import os
import argparse

def filter_and_save_images(input_dir, output_dir, target_shape):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through the files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):  # Add more extensions as needed
            # Load the image using OpenCV
            image_path = os.path.join(input_dir, filename)
            image = cv2.imread(image_path)

            if image is not None:
                # Check if the image shape matches the target shape
                if image.shape == target_shape:
                    # Save the image to the output directory
                    output_path = os.path.join(output_dir, filename)
                    cv2.imwrite(output_path, image)

    print(f"Images with shape {target_shape} saved to the output folder.")

#the code will start running from here
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter and save images with the target shape to the output directory.")
    parser.add_argument("input_dir", help="Path to the input directory")
    parser.add_argument("output_dir", help="Path to the output directory")
    parser.add_argument("--target_shape", default=(512, 512, 3), type=int, nargs=3, help="Desired image shape (height width channels)")

    args = parser.parse_args()
    filter_and_save_images(args.input_dir, args.output_dir, tuple(args.target_shape))
