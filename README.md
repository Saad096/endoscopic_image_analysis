# go to code folder
``` shell
cd yolov7
```



## Training

``` shell
# train p5 models
python3 train_aux.py --cfg cfg/training/yolov7-e6e.yaml --data data/coco.yaml --workers 4 --device 0 --batch-size 8 --weights ../weight/yolov7.pt --project Endoscopic_images_analysis --epochs 100 --img-size 640 --name Train_weights
```


## Inference

``` shell
# with ensamble
xvfb-run -a python3 detect.py --weights weights/best1.pt weights/best2.pt  weights/best3.pt weights/best4.pt --source ../Datasets/testing/images --img-size 640 --conf-thres 0.25 --iou-thres 0.45 --device 1 --view-img --save-txt --save-conf --classes 0 1 2 --agnostic-nms --augment --project ../Inferences --name Results
```





</details>

## Testing

``` shell
# with ensamble
python3 test.py \
    --weights weights/best1.pt weights/best2.pt  weights/best2.pt weights/best3.pt \
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
    --project Endoscopic_test \
    --name exp1 \
    --exist-ok \
    --no-trace \
    --v5-metric
```
