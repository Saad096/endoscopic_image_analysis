# Endoscopic Image Analysis
**Description:** 
Detect polyp, instrument, ulcerative colitis in endoscopic images using YOLOv7.

**Clone the repo:**
```shell
git clone --branch saad https://github.com/axcelerateai/endoscopic_image_analysis.git
```

Change directory to the project directory
```shell
cd endoscopic_image_analysis
```
Create virtual environment
```shell
python3 -m venv .env
# Activate virtual environment
source .env/bin/activate
```
Install required packages
```shell
pip install -r requirements.txt
```
#### Prepare and preprocess custom dataset by "preprocess_utils".

##### convert_to_Json.py
**Usage:** convert polygon json to yolo fromat bounding boxes

**Arguments:**
- `input_file`: The input JSON file to be converted.
- `output_file`: The name of the output file where the converted data will be saved.

##### filter_classes.py

**Description:** Filters data based on class and saves relevant files.

##### shape_filter.py

**Description:** Filters and saves images with a specific shape (512x512).

**Usage:**

**Arguments:**
- input_directory: The directory containing image files.
- output_directory: The directory where filtered images will be saved.
- target_shape: Desired image shape in the format "height width channels."

##### train_test_split.py

**Description:** Split dataset into required splitting ratio for training, testing and validation.

### Installation

Change directory to the model working directory and download trained_weights and datasets
``` shell
cd yolov7
```
Install gdown package.
``` shell
pip install gdown
``` 
After cloning project repository download trained_weights
```shell
# download trained_weights
gdown https://drive.google.com/uc?id=1P-FrH3GGdJa0tCwbPnShMLum98OhYbhs
# unzip trained_weights
unzip trained_weights.zip
rm trained_weights.zip
```
Download Datasets
```shell
gdown https://drive.google.com/uc?id=1e1aRXTEi8JlKid2-xdBlunUQxil-tMNf
# Extract Dataset
unzip Datasets.zip -d .. 
rm Datasets.zip
```

### Train model

```shell
# install wandb
pip install wandb
```

``` shell
# train p5 models
python3 train_aux.py --cfg cfg/training/yolov7-e6e.yaml --data data/coco.yaml --workers 4 --device 0 --multi-scale --batch-size 8 --weights ../initial_weight/yolov7.pt --epochs 300 --img-size 640 --name trained_weights
```


### Run inference
Run following commands first to install xvfb package:

``` shell
sudo apt-get update
# Ater updaing the OS run following command to install the packae:
sudo apt-get install xvfb
```

``` shell
# with ensamble
xvfb-run -a python3 detect.py --weights trained_weights/best1.pt trained_weights/best2.pt trained_weights/best3.pt trained_weights/best4.pt trained_weights/best5.pt --source ../Datasets/testing/images --img-size 640 --conf-thres 0.25 --iou-thres 0.5 --device 0 --view-img --save-txt --save-conf --classes 0 1 2 --agnostic-nms --augment --project ../inference/ --name exp2_results
```

### Run testing

``` shell
# with ensamble
python3 test.py \
    --weights trained_weights/best1.pt trained_weights/best2.pt trained_weights/best3.pt trained_weights/best4.pt trained_weights/best5.pt \
    --data data/coco.yaml \
    --batch-size 16 \
    --img-size 640 \
    --conf-thres 0.001 \
    --iou-thres 0.5 \
    --task test \
    --device 0 \
    --augment \
    --verbose \
    --save-txt \
    --save-hybrid \
    --save-conf \
    --project inference \
    --name test_exp2 \
    --exist-ok \
    --no-trace \
    --v5-metric
```

