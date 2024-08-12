import os
import cv2
from ultralytics import YOLO

# 设置输入和输出文件夹路径
input_folder = '/home/vkeline/yyf/datasets/0321/'
output_folder = '/home/vkeline/yyf/datasets/0321_vehicle/'

# 创建输出文件夹
os.makedirs(output_folder, exist_ok=True)

# 加载预训练的 YOLOv8 模型
model = YOLO('/home/vkeline/yyf/model/vehicle.pt')

# 遍历输入文件夹中的所有图片
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # 读取图片
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        # 进行目标检测
        results = model.predict(image)

        # 获取检测结果
        boxes = results[0].boxes.xyxy.cpu().numpy()  # 目标框坐标

        # 遍历每个检测到的目标框
        for i, box in enumerate(boxes):
            # 将坐标转换为整数
            x1, y1, x2, y2 = [int(coord) for coord in box]

            # 裁剪目标框区域
            cropped_image = image[y1:y2, x1:x2]

            # 保存裁剪后的图片
            output_path = os.path.join(output_folder, f'cropped_{i}_{filename}')
            cv2.imwrite(output_path, cropped_image)