from ultralytics import YOLO

#加载YOLOv8模型
model = YOLO('yolov8n.pt')  

#设置数据集路径
data_yaml = 'C:/Users/yoyi9/Desktop/yoyi/dataset/dataset.yaml'

#使用找到的最佳学习率进行训练
model.train(data=data_yaml, epochs=30, batch=50, imgsz=640, lrf = 0.001) 

# 在测试集上验证模型
results = model.val()

#保存模型
model.save('yolov8_trained_model.pt')
