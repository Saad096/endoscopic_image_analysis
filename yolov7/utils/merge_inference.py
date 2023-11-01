import os
import cv2
import numpy as np

original_directory = (
    "/home/saadalam/Desktop/Endoscopic_Image_Analysis/Datasets/testing/images"
)
annotated_directory = "/home/saadalam/Desktop/Endoscopic_Image_Analysis/BBox"
inference_directory = (
    "/home/saadalam/Desktop/Endoscopic_Image_Analysis/Inferences/Results"
)
output_directory = "/home/saadalam/Desktop/Endoscopic_Image_Analysis/merged_analysis"
os.makedirs(output_directory, exist_ok=True)

for image_filename in os.listdir(original_directory):
    if image_filename.endswith(".jpg"):  # Adjust the file extension as needed
        original_path = os.path.join(original_directory, image_filename)
        annotated_path = os.path.join(annotated_directory, image_filename)
        inference_path = os.path.join(inference_directory, image_filename)

        if os.path.exists(annotated_path) and os.path.exists(inference_path):
            original_image = cv2.imread(original_path)
            annotated_image = cv2.imread(annotated_path)
            inference_image = cv2.imread(inference_path)

            # Get image dimensions for resizing and framing
            height, width, _ = original_image.shape

            # Create a blank frame with three boxes for images
            merged_image = 255 * np.ones((height, 3 * width, 3), dtype=np.uint8)

            # Copy the images to their respective boxes in the frame
            merged_image[:, :width] = original_image
            merged_image[:, width : 2 * width] = annotated_image
            merged_image[:, 2 * width :] = inference_image

            # Add image titles
            font = cv2.FONT_HERSHEY_SIMPLEX
            title_color = (0, 0, 255)  # Red (BGR color code)
            title_thickness = 2
            title_font_scale = 0.8
            cv2.putText(
                merged_image,
                "Original",
                (10, 30),
                font,
                title_font_scale,
                title_color,
                title_thickness,
            )
            cv2.putText(
                merged_image,
                "Annotated",
                (width + 10, 30),
                font,
                title_font_scale,
                title_color,
                title_thickness,
            )
            cv2.putText(
                merged_image,
                "Inference",
                (2 * width + 10, 30),
                font,
                title_font_scale,
                title_color,
                title_thickness,
            )

            # Save the merged image with titles
            merged_image_filename = os.path.splitext(image_filename)[0] + "_merged.jpg"
            merged_image_path = os.path.join(output_directory, merged_image_filename)
            cv2.imwrite(merged_image_path, merged_image)
        else:
            print(f"Missing files for image: {image_filename}")
