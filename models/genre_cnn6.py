
















import easyocr
import cv2
import os

reader = easyocr.Reader(['en','ko'])  # 영어 지원
image = cv2.imread(os.path.join(os.path.dirname(__file__),'신 테니스의 왕자 베스트 게임즈 테즈카 vs 아토베_85899345920.jpg'))
# print(os.path.join(os.path.dirname(__file__),'shark.jpg'))
# OCR 적용
results = reader.readtext(image)
for (bbox, text, prob) in results:
    if prob > 0.4:
        print(f'Detected text: {text} with probability: {prob:.4f}')
