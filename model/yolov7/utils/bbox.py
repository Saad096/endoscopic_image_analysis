import os

images_directory = (
    "/home/saadalam/Desktop/Endoscopic_Image_Analysis/Datasets/testing/images"
)
labels_directory = (
    "/home/saadalam/Desktop/Endoscopic_Image_Analysis/Datasets/testing/labels"
)

# files = [f for f in os.listdir(labels_directory)]
# print(len(files))
# exit()
# os.makedirs("../BBox")
output_directory = "/home/saadalam/Desktop/Endoscopic_Image_Analysis/BBox"
import cv2

# images = [img for img in os.listdir(labels_directory)]
# print(len(images))


for image_filename in os.listdir(images_directory):
    if image_filename.endswith(".jpg"):  # Adjust the file extension as needed
        image_path = os.path.join(images_directory, image_filename)
        annotation_filename = os.path.splitext(image_filename)[0] + ".txt"
        annotation_path = os.path.join(labels_directory, annotation_filename)

        # Check if the annotation file exists for the image
        if os.path.exists(annotation_path):
            image = cv2.imread(image_path)
            image_height, image_width, _ = image.shape

            with open(annotation_path, "r") as annotation_file:
                lines = annotation_file.readlines()
                for line in lines:
                    parts = line.split()
                    class_id = int(parts[0])
                    x, y, width, height = map(float, parts[1:])

                    # Convert YOLO coordinates to pixel coordinates
                    left = int((x - width / 2) * image_width)
                    top = int((y - height / 2) * image_height)
                    right = int((x + width / 2) * image_width)
                    bottom = int((y + height / 2) * image_height)

                    # Draw bounding box on the image
                    color = (0, 255, 0)  # Green (BGR color code)
                    thickness = 2
                    image = cv2.rectangle(
                        image, (left, top), (right, bottom), color, thickness
                    )

            # Save the image with the bounding boxes
            output_path = os.path.join(output_directory, image_filename)
            cv2.imwrite(output_path, image)
        else:
            print(f"No annotation file found for image: {image_filename}")
