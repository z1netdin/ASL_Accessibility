from ultralytics import YOLO

model = YOLO("yolov8n-cls.pt") 

model.train(
    data="datasets/asl_alphabet",  
    epochs=30,
    imgsz=224
)
