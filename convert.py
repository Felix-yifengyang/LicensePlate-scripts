# txt_create是创建转换后的txt文件，即yolo格式的txt文件，一张图对应一个txt，地址一般是在./images中，或./labels中
# get_img_size是获得图片的尺寸 ，作用为后续的标准化准备，要记住地址末尾要加入"/"，地址一般是./images
# main函数中需要指定PPLabel生成的txt文件的路径
# main函数还需要指定的是生成的文件夹的路径，一般可以不管，只需要一次

import os
import cv2
import json

"""
# 读取数据文件
"""


def read_txt(file_name):
    data = []

    file = open(file_name, 'r', encoding='utf-8')
    file_data = file.readlines()     # 读取所有行
    for row in file_data:
        tmp_list = row.strip().split('\t')     # 按制表符分割
        data.append(tmp_list)     # 将每行数据插入data中
    file.close()
    return data

"""
# 创建文件夹
"""

def create_folder(filename):
    filename = filename.strip()
    filename = filename.rstrip("\\")
    isExists = os.path.exists(filename)
    if not isExists:
        os.makedirs(filename)
        print(filename + "创建成功")
        return True
    else:
        print(filename + "已存在")
        return False

"""
# 创建txt标注文件
"""


def txt_create(name, msg):
        filename = "G:/pro_dataset/License/License/images/traindata/###"      # 要创建的文件路径
        full_path = filename + "/" + name.split('.')[0] + '.txt'
        # 直接覆盖
        file = open(full_path, 'w', encoding='utf-8')
        file.write(msg + '\n')
        file.close()

"""
# 坐标归一化
"""

def normalization(xmin, ymin, xmax, ymax, img_w, img_h):
    x = round((xmin + xmax) / (2.0 * img_w), 6)
    y = round((ymin + ymax) / (2.0 * img_h), 6)
    w = round((xmax - xmin) / (1.0 * img_w), 6)
    h = round((ymax - ymin) / (1.0 * img_h), 6)
    return x, y, w, h

"""
# 每张图片的尺寸
"""

def get_img_size(img_path):
    img_path = "G:/pro_dataset/License/License/images/traindata/###/" + img_name     # 原始图片路径 
    """
    # 这行代码有点问题，传进来的是img_path，按理说改成img_name的，但不知道为什么没有影响 
    # 后续找到的原因可能是因为在局部变量找img_name，参数列表中也没找到img_name，但在外部的全局命名空间中查找img_name找到了。一切都是巧合
    """
    print(img_path)
    mat = cv2.imread(img_path)
    if mat is None:
        return mat
    return mat.shape

if __name__ == "__main__":
    data = read_txt("G:/pro_dataset/License/License/images/traindata/###/Label.txt")     # 原始数据表   #需要转换的标注文件
    # create_folder("G:/pro_dataset/License/License/labels")      # 新建的转换后文件路径，重复性比较大，一般运行一次就可以
    for img_data in data:
        img_name = img_data[0].split('/')[1]     # 每行数据提取图片名
        xywh = img_data[1]     # 每行数据提取坐标信息
        xywh_dict = json.loads(xywh)     # 转换为字典
        img_size = get_img_size(img_name)
        # print(xywh_dict)
        # print(img_size)
        if img_size is None:
            continue
        x_coords = []
        y_coords = []
        for item in xywh_dict:
            points = item['points']
            for point in points:
                x, y = point
                x_coords.append(x)
                y_coords.append(y)
            # print(x_coords, y_coords)
            yolo_data = normalization(min(x_coords), min(y_coords), max(x_coords), max(y_coords),
                                                      img_size[1], img_size[0])
            # print(yolo_data)
            txt_create(img_name,"0 %s %s %s %s %s %s %s %s %s %s %s %s" % (str(yolo_data[0]), str(yolo_data[1]), str(yolo_data[2]), str(yolo_data[3]),
                                                                            str(round(x_coords[0] / img_size[1], 6)),
                                                                            str(round(y_coords[0] / img_size[0], 6)),
                                                                            str(round(x_coords[1] / img_size[1], 6)),
                                                                            str(round(y_coords[1] / img_size[0], 6)),
                                                                            str(round(x_coords[2] / img_size[1], 6)),
                                                                            str(round(y_coords[2] / img_size[0], 6)),
                                                                            str(round(x_coords[3] / img_size[1], 6)),
                                                                            str(round(y_coords[3] / img_size[0], 6))))
