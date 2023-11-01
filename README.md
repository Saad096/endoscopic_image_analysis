
# Install required packages

```shell
pip install -r requirements.txt
```

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


# go to code folder
``` shell
cd yolov7
```

## Training

``` shell
# train p5 models
python3 train_aux.py --cfg cfg/training/yolov7-e6e.yaml --data data/coco.yaml --workers 4 --device 0 --batch-size 8 --weights ../initial_weight/yolov7.pt --epochs 100 --img-size 640 --name Trained_weights
```

To run inference command run following commands first to install xvfb pcackage on ubuntu os:

``` shell
sudo apt-get update
# Ater updaing the OS run following command to install the packae:
sudo apt-get install xvfb
```



## Inference

``` shell
# with ensamble
xvfb-run -a python3 detect.py --weights Trained_weights/best1.pt Trained_weights/best2.pt Trained_weights/best3.pt Trained_weights/best4.pt --source ../Datasets/testing/images --img-size 640 --conf-thres 0.25 --iou-thres 0.5 --device 1 --view-img --save-txt --save-conf --classes 0 1 2 --agnostic-nms --augment --project ../Inferences/ --name exp2_results
```





</details>

## Testing

``` shell
# with ensamble
python3 test.py \
    --weights Trained_weights/best1.pt Trained_weights/best2.pt Trained_weights/best3.pt Trained_weights/best4.pt \
    --data data/coco.yaml \
    --batch-size 16 \
    --img-size 640 \
    --conf-thres 0.001 \
    --iou-thres 0.5 \
    --task test \
    --device 1 \
    --augment \
    --verbose \
    --save-txt \
    --save-hybrid \
    --save-conf \
    --project Inferences \
    --name test_exp2 \
    --exist-ok \
    --no-trace \
    --v5-metric
```

