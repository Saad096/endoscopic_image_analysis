
# Install required packages

```shell
pip install -r requirements.txt
```


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
