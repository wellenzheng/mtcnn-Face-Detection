from mtcnn import MTCNN
import cv2 as cv
import tensorflow as tf
import os

test_path = 'C:\\Users\\郑炜俊\\Desktop\\ML Experiment\\experiment4\\mtcnn_pytorch\\data\\test_images\\'
img_list = os.listdir(test_path)

detector = MTCNN()

for name in img_list:
    img = cv.cvtColor(cv.imread(test_path+name), cv.COLOR_BGR2RGB)
    detector.detect_faces(img)
    [
        {
            'box': [277, 90, 48, 63],
            'keypoints':
            {
                'nose': (303, 131),
                'mouth_right': (313, 141),
                'right_eye': (314, 114),
                'left_eye': (291, 117),
                'mouth_left': (296, 143)
            },
            'confidence': 0.99851983785629272
        }
    ]
