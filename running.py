from paddleocr import PaddleOCR, draw_ocr
import os
from PIL import Image

ocr = PaddleOCR(use_GPU=False,
                rec_model_dir='./ocr/',
                det_model_dir='./det/',
                rec_char_dict_path= './ocr/hphm_dict.txt',
                use_space_char= False) # need to run only once to download and load model into memory
img_dir = './transformed/'
for filename in os.listdir(img_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(img_dir, filename)
        result = ocr.ocr(img_path)
        for line in result:
            print(line)
        image = Image.open(img_path).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        im_show = draw_ocr(image, boxes, txts, scores, font_path='./doc/fonts/simfang.ttf')
        im_show = Image.fromarray(im_show)
        im_show.save('/home/vkeline/yyf/PaddleOCR-release-2.5/outcome/' + filename)