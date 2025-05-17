from ultralytics import YOLO

model = YOLO("runs/classify/train3/weights/best.pt")
model.predict(source=0, imgsz=224, show=True)  # Use your webcam
