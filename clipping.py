import os
import cv2
import numpy as np


def perspective_transform(img, src_pts, dst_pts):
    """
    执行图像的透视变换

    参数:
    img (numpy.ndarray): 输入图像
    src_pts (numpy.ndarray): 源图像上的四个点坐标,shape为(4, 2)
    dst_pts (numpy.ndarray): 目标图像上的四个点坐标,shape为(4, 2)

    返回:
    transformed_img (numpy.ndarray): 经过透视变换后的图像
    """
    # 计算透视变换矩阵
    M = cv2.getPerspectiveTransform(np.float32(src_pts), np.float32(dst_pts))

    # 执行透视变换
    transformed_img = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))

    return transformed_img

num = str(7) # 每次获得了predict文件夹后，只需要改数字就可以了
boot_folder = 'G:/pro_dataset/License/predict' + num
# 设置输入和输出文件夹路径
image_folder = boot_folder
label_folder = boot_folder+ '/labels'

# 创建输出文件夹
clipped_folder = boot_folder + '/clipped'
transformed_folder = boot_folder + '/transformed'
os.makedirs(clipped_folder, exist_ok=True)
os.makedirs(transformed_folder, exist_ok=True)

# 遍历输入文件夹中的所有图片
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # 读取图片
        image_path = os.path.join(image_folder, filename)
        image = cv2.imread(image_path)
        height, width, _ = image.shape

        # 根据label文件裁剪图像
        label_path = os.path.join(label_folder, os.path.splitext(filename)[0] + '.txt')
        if os.path.exists(label_path):
            with open(label_path, 'r') as label:
                lines = label.readlines()
                for i, line in enumerate(lines):
                    # 分割坐标信息
                    coords = list(map(float, line.strip().split()))
                    x1, y1, x2, y2, x3, y3, x4, y4 = coords[-8:]

                    # 将归一化坐标转换为图像的实际像素坐标
                    x1 = int(x1 * width)
                    y1 = int(y1 * height)
                    x2 = int(x2 * width)
                    y2 = int(y2 * height)
                    x3 = int(x3 * width)
                    y3 = int(y3 * height)
                    x4 = int(x4 * width)
                    y4 = int(y4 * height)

                    # 计算裁剪区域的坐标
                    x_min = min(x1, x2, x3, x4)
                    y_min = min(y1, y2, y3, y4)
                    x_max = max(x1, x2, x3, x4)
                    y_max = max(y1, y2, y3, y4)

                    # 裁剪图像
                    clipped_image = image[y_min:y_max, x_min:x_max]
                    
                    # 获得裁剪图像的尺寸
                    clipped_height, clipped_width, _ = clipped_image.shape

                    # 设定裁剪图片路径并保存
                    clipped_path = os.path.join(clipped_folder, f"{os.path.splitext(filename)[0]}_clip_{i+1}.jpg")
                    cv2.imwrite(clipped_path, clipped_image)

                    # 透视变换
                    clipped_x1 = x1 - x_min
                    # print(clipped_x1)
                    clipped_y1 = y1 - y_min
                    # print(clipped_y1)
                    clipped_x2 = clipped_x1 + (x2 - x1)
                    # print(clipped_x2)
                    clipped_y2 = y2 - y_min
                    # print(clipped_y2)
                    clipped_x4 = x4 - x_min
                    # print(clipped_x4)
                    clipped_x3 = clipped_x4 + (x3 - x4)
                    # print(clipped_x3)
                    clipped_y3 = clipped_y2 + (y3 - y2)
                    # print(clipped_y3)
                    clipped_y4 = clipped_y1 + (y4 - y1)
                    # print(clipped_y4)
                    # print("============================")
                    src_pts = np.array([[clipped_x1, clipped_y1], [clipped_x2, clipped_y2], [clipped_x3, clipped_y3], [clipped_x4, clipped_y4]], dtype=np.float32)
                    dst_pts = np.array([[0, 0], [clipped_width, 0], [clipped_width, clipped_height], [0, clipped_height]], dtype=np.float32)
                    transformed_img = perspective_transform(clipped_image, src_pts, dst_pts)

                    # 设定变换后的图片路径并保存
                    transformed_path = os.path.join(transformed_folder, f"{os.path.splitext(filename)[0]}_transform_{i+1}.jpg")
                    cv2.imwrite(transformed_path, transformed_img)
        else:
            print(f"Skipping {filename} - no label file found")