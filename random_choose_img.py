import os
import random
import shutil

# 原始文件夹路径
source_folder = r"G:\pro_dataset\License\License\images\train"

target_folder = r"G:\pro_dataset\License\License\images\val"

# 获取原始文件夹下的所有图片文件路径
all_image_files = [os.path.join(source_folder, f) for f in os.listdir(source_folder) if f.endswith(".jpg") or f.endswith(".png")]

# 共6531张图片，随机选择 681 个图片文件作为测试集
sample_image_files = random.sample(all_image_files, 681)

# 生成 sampled_files.txt
output_file_path = os.path.join(source_folder, "sampled_files.txt")
with open(output_file_path, "w") as f:
    f.write("\n".join(sample_image_files))
print(f"已将随机选择的 {len(sample_image_files)} 个文件路径保存到 '{output_file_path}'.")

# 移动文件和相应的 txt 文件
for image_file in sample_image_files:
    filename = os.path.basename(image_file)
    target_image_path = os.path.join(target_folder, filename)
    txt_file_path = os.path.splitext(image_file)[0] + ".txt"
    txt_target_path = os.path.join(target_folder, os.path.basename(txt_file_path))

    # 对应的 txt 文件是否存在
    if os.path.exists(txt_file_path):
        shutil.move(image_file, target_image_path)
        shutil.move(txt_file_path, txt_target_path)
        print(f"已移动文件: {image_file} 和 {txt_file_path}")
    else:
        shutil.move(image_file, target_image_path)
        print(f"已移动文件: {image_file}")

print(f"成功移动了 {len(sample_image_files)} 个图片文件和相应的 {len(sample_image_files)} 个 txt 文件到 {target_folder}.")