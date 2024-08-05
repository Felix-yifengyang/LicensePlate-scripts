import os
from concurrent.futures import ThreadPoolExecutor

# 设置图片文件夹路径
image_folder = 'G:/pro_dataset/License/License/images/traindata/0111'

# 设置包含文件名的txt文件路径
txt_file = 'G:/pro_dataset/License/License/images/traindata/plate-Label.txt'

# 读取txt文件并返回文件名列表
def read_txt(file_name):
    data = []

    with open(file_name, 'r', encoding='utf-8') as file:
        for row in file.readlines():
            tmp_list = row.strip().split('\t')
            data.append(tmp_list)
    return data

def create_txt(msg):
    filename = "G:/pro_dataset/License/License/images/traindata/0111"  # 要创建的文件路径
    full_path = os.path.join(filename, "0111.txt") # 文件夹名需要按需更改
    # 直接覆盖
    with open(full_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(['\t'.join(line) for line in msg])) # 还不懂

def check_file(img_data):
    img_name = os.path.splitext(img_data[0].split('/')[1])[0] # 返回了没有后缀的文件名
    # print(img_name)
    if img_name in image_files:
        return img_data
    else:
        return None

if __name__ == "__main__":
    data = read_txt(txt_file)
    image_list = os.listdir(image_folder)
    image_files = []

    for image in image_list:
        image_files.append(image.rsplit('.', 1)[0])
    with ThreadPoolExecutor() as executor:
        results = executor.map(check_file, data)

    txt = [result for result in results if result is not None]
    create_txt(txt)
