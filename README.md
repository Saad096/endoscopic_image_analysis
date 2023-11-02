# Endoscopic Image Analysis
### Installation
Clone the repo
``` shell
git clone --branch saad https://github.com/axcelerateai/endoscopic_image_analysis.git
```
Install required packages
```shell
pip install -r requirements.txt
```
Go to working Directory folder and download trained_weights and dataset
``` shell
cd yolov7
# After cloning project repository daownload trained_weights
wget --no-check-certificate -r https://drive.google.com/drive/folders/1IxS8Leyz3DEvZC2blT_OwdEpV6rviBS9?usp=sharing
# Download Datasets
wget --no-check-certificate -O archive.zip https://drive.google.com/file/d/1aw2sLKRZ9Q0pRZziiTKfZ1wswo8JQTgL/view?usp=sharing
# Extract Dataset
unzip archive.zip -d .. 
```

### Train model

``` shell
# train p5 models
python3 train_aux.py --cfg cfg/training/yolov7-e6e.yaml --data data/coco.yaml --workers 4 --device 0 --batch-size 8 --weights ../initial_weight/yolov7.pt --epochs 100 --img-size 640 --name trained_weights
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
xvfb-run -a python3 detect.py --weights trained_weights/best1.pt trained_weights/best2.pt trained_weights/best3.pt trained_weights/best4.pt --source ../Datasets/testing/images --img-size 640 --conf-thres 0.25 --iou-thres 0.5 --device 1 --view-img --save-txt --save-conf --classes 0 1 2 --agnostic-nms --augment --project ../inference/ --name exp2_results
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
    --device 1 \
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
