import pandas as pd
import matplotlib.pyplot as plt

# 讀取CSV文件
df = pd.read_csv('C:/Users/yoyi9/Desktop/yoyi/runs/detect/train10/results.csv')


df.columns = [col.strip() for col in df.columns]  # 去除列名中的空格

# 再次檢查列名
print(df.columns)
# 提取數據
epochs = df['epoch']
train_box_loss = df['train/box_loss']
train_cls_loss = df['train/cls_loss']
val_box_loss = df['val/box_loss']
val_cls_loss = df['val/cls_loss']

plt.figure(figsize=(12, 6))

plt.plot(epochs, train_box_loss, label='Train Box Loss', color='blue', linestyle='--')
#plt.plot(epochs, train_cls_loss, label='Train Class Loss', color='orange', linestyle='--')
plt.plot(epochs, val_box_loss, label='Validation Box Loss', color='blue')
#plt.plot(epochs, val_cls_loss, label='Validation Class Loss', color='orange')

plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss Curve')
plt.legend()
plt.grid(True)
plt.show()