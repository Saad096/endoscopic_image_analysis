# Endoscopic Image Analysis
### Installation
Clone the repo
``` shell
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
gdown https://drive.google.com/uc?id=1kgFsCWKE3wcg84KPODLnuMSlHj1qzRms
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

``` shell
# train p5 models
python3 train_aux.py --cfg cfg/training/yolov7-e6e.yaml --data data/coco.yaml --workers 4 --device 0 --batch-size 8 --weights ../initial_weight/yolov7.pt --epochs 300 --img-size 640 --name trained_weights
```

To run inference command run following commands first to install xvfb pcackage on ubuntu os:

``` shell
sudo apt-get update
# Ater updaing the OS run following command to install the packae:
sudo apt-get install xvfb
```



### Run inference

``` shell
# with ensamble
xvfb-run -a python3 detect.py --weights trained_weights/best1.pt trained_weights/best2.pt trained_weights/best3.pt trained_weights/best4.pt --source ../Datasets/testing/images --img-size 640 --conf-thres 0.25 --iou-thres 0.5 --device 0 --view-img --save-txt --save-conf --classes 0 1 2 --agnostic-nms --augment --project ../inference/ --name exp2_results
```

### Run testing

``` shell
# with ensamble
python3 test.py \
    --weights trained_weights/best1.pt trained_weights/best2.pt trained_weights/best3.pt trained_weights/best4.pt \
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
