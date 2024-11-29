from ultralytics import YOlO

model= YOLO('yolov8n.yaml')

results=model.train(data='data.yaml',epochs=1)