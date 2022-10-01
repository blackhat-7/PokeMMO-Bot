import os
import cv2


class GameObject:
    def __init__(self, img_path: list):
        self.img_path = img_path
        self.img = cv2.imread(os.path.join('images', *img_path), 0)
        self.width = self.img.shape[1]
        self.height = self.img.shape[0]
        self.locations = []
