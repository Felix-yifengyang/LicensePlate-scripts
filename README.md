# LicensePlate-scripts

- **convert.py**：Convert txt from PPOCRLabel to YOLOv8 format
- **random_choose_img.py**：Randomly select a specified number of images and move to specified folder
- **depart.py**: When there are a large number of `Label.txt` file, you can generate a `Label.txt` file that matches the current folder based on the file name in the folder.
- **get_coor.py**: This is a "predict" script, and you will get the predicted images and labels. If there are 2 or more labels in one image, the txt file has 2 or more lines.
- **clipping.py**: After running `get_coor.py`, you will get the predicted images, then by using this script, you will get the clipped and transformed(Perspective Trasformation) images.
- **running.py**: Using the PaddleOCR to predict images.
- **clipping_vehicle.py**: Use `vehicle.pt` to detect the vehicle and clipping.
