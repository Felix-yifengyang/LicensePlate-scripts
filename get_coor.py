# import os
# import cv2
# from ultralytics import YOLO
#
# # 设置输入文件夹路径
# input_folder = "/home/vkeline/yyf/datasets/License/test/"
#
# output_folder = "/home/vkeline/yyf/runs/pose/predict7/"
# os.makedirs(output_folder, exist_ok=True)
#
# # 加载预训练的 YOLOv8 模型
# model = YOLO("/home/vkeline/yyf/runs/pose/train6/weights/best.pt")
#
# """
# # 创建txt标注文件
# """
#
# def txt_create(name, msg):
#         full_path = output_folder + name + '.txt' # 要创建的文件路径
#         # 直接覆盖
#         file = open(full_path, 'w', encoding='utf-8')
#         file.write(msg + '\n')
#         file.close()
#
# """
# # 坐标归一化
# """
#
# def xywh(xmin, ymin, xmax, ymax):
#     x = round((xmin + xmax) / 2.0, 6)
#     y = round((ymin + ymax) / 2.0, 6)
#     w = round((xmax - xmin) / 1.0, 6)
#     h = round((ymax - ymin) / 1.0, 6)
#     return x, y, w, h
#
#
# """
# # 获得图中的坐标，输出YOLO格式的Label.txt
# """
#
# def get_coord():
# # 遍历输入文件夹中的所有图片
#     for filename in os.listdir(input_folder):
#         if filename.endswith('.jpg') or filename.endswith('.png'):
#             # 读取图片
#             image_path = os.path.join(input_folder, filename)
#             # print(image_path)
#             """
#             # Sample: "/home/vkeline/yyf/runs/pose/predict2/0111-B1A-3504000026-18122435000500866437-1.jpg"
#             """
#             image_name = image_path.split('/')[-1].split('.')[0]
#             """
#             # 提取出"0111-B1A-3504000026-18122435000500866437-1"
#             """
#             image = cv2.imread(image_path)
#
#             # 使用model进行目标检测
#             results = model.predict(image, save=True)
#
#             # 获取检测结果
#             keypoints = results[0].keypoints.cpu().numpy()  # 目标点坐标
#             # print(keypoints)
#             """
#             # 打印后的结果
#             0: 480x640 1 License, 7.1ms
#             Speed: 1.3ms preprocess, 7.1ms inference, 0.9ms postprocess per image at shape (1, 3, 480, 640)
#             ultralytics.engine.results.Keypoints object with attributes:
#
#             conf: None
#             data: array([[[     498.62,      525.26],
#                     [      589.5,      530.06],
#                     [     587.74,      583.06],
#                     [     495.83,      576.43]]], dtype=float32)
#             has_visible: False
#             orig_shape: (960, 1280)
#             shape: (1, 4, 2)
#             xy: array([[[     498.62,      525.26],
#                     [      589.5,      530.06],
#                     [     587.74,      583.06],
#                     [     495.83,      576.43]]], dtype=float32)
#             xyn: array([[[    0.38955,     0.54714],
#                     [    0.46055,     0.55214],
#                     [    0.45917,     0.60735],
#                     [    0.38737,     0.60045]]], dtype=float32)
#             /home/vkeline/yyf/runs/pose/predict2/0112-Z21-3504000044-19120335000501162242-1.jpg
#             """
#             # 遍历每个检测到的目标点
#             for i, kps in enumerate(keypoints):
#                 if keypoints.shape[1] == 0: # 表示no detections
#                     continue
#                 # 提取归一化后的关键点坐标
#                 xyn = kps.xyn
#                 # print(xyn)
#                 """
#                 [[[    0.38955     0.54714]
#                   [    0.46055     0.55214]
#                   [    0.45917     0.60735]
#                   [    0.38737     0.60045]]]
#                 """
#                 x = xyn[0, :, 0]
#                 y = xyn[0, :, 1]
#                 yolo_data = xywh(min(x), min(y), max(x), max(y))
#                 # 将关键点坐标写入 TXT 文件
#                 txt_create(image_name, "0 %s %s %s %s %s %s %s %s %s %s %s %s" % (
#                 str(yolo_data[0]), str(yolo_data[1]), str(yolo_data[2]), str(yolo_data[3]),
#                 str(round(x[0], 6)),
#                 str(round(y[0], 6)),
#                 str(round(x[1], 6)),
#                 str(round(y[1], 6)),
#                 str(round(x[2], 6)),
#                 str(round(y[2], 6)),
#                 str(round(x[3], 6)),
#                 str(round(y[3], 6))))
#
# if __name__ == "__main__":
#     get_coord()


"""
=============================================================================================================
上面的方法也可以实现相同的功能
"""

"""
如果一张图中有两个Label，则txt文件中会有两行
"""
from ultralytics import YOLO

# 设置输入文件夹路径
input_folder = "/home/vkeline/yyf/datasets/License/test/"

model = YOLO("/home/vkeline/yyf/runs/pose/train6/weights/best.pt")

model.predict(input_folder, save=True, save_txt=True, imgsz=640)