# endoscopic_image_analysis
Detect polyp, instrument, ulcerative colitis in endoscopic images using YOLOv7. Medical images
# Data Processing Scripts

This repository contains a set of Python scripts for data processing and conversion. Each script serves a specific purpose and can be used to manipulate data as described below.

## 1. `convert_json.py`

**Description:** Converts a JSON file to a different format.

**Usage:**

**Arguments:**
- `input_file`: The input JSON file to be converted.
- `output_file`: The name of the output file where the converted data will be saved.

## 2. `filter_class.py`

**Description:** Filters data based on class and saves relevant files.

**Usage:**

**Arguments:**
- `input_directory`: The directory containing text and image files.
- `output_directory`: The directory where filtered text and image files will be saved.

## 3. `filter512.py`

**Description:** Filters and saves images with a specific shape (512x512).

**Usage:**

**Arguments:**
- `input_directory`: The directory containing image files.
- `output_directory`: The directory where filtered images will be saved.
- `--target_shape` (Optional): Desired image shape in the format "height width channels."

Feel free to use these scripts to process your data efficiently.

For detailed information about each script, please refer to their respective source code.

