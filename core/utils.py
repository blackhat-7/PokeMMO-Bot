import os
import random
import time
import keyboard
import cv2
import mss
import numpy as np
from core.game_object import GameObject


def get_screenshot():
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[0])
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGRA2GRAY)
        return screenshot


def locate_object(template_path: list, threshold: int=0.5, show=False):
    # Get images
    template = GameObject(template_path)
    screenshot = get_screenshot()

    # Template match
    result = cv2.matchTemplate(screenshot, template.img, cv2.TM_CCOEFF_NORMED)
    yloc, xloc = np.where(result >= threshold)

    # drop xloc, yloc if they are too close to each other
    for i, (x, y) in enumerate(zip(xloc, yloc)):
        dup = False
        for j, (x2, y2) in enumerate(list(zip(xloc, yloc))[i+1:]):
            if i != j:
                if abs(x - x2) < 20 and abs(y - y2) < 20:
                    dup = True
                    break
        if not dup: 
            template.locations.append((x, y))
    
    print(f"Found {len(template.locations)} {' '.join(template.img_path)}")
    if show:
        show_objects(screenshot, template)
    return template


def show_objects(image, template):
    for x, y in zip(template.locations):
        cv2.rectangle(image, (x, y), (x + template.width, y + template.height), (0, 0, 255), 2)
    cv2.namedWindow('objects', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('objects', 1280, 720)
    cv2.imshow('objects', image)
    cv2.waitKey()


def choose_random_object(template):
    idx = random.randint(0, len(template.locations) - 1)
    return template.locations[idx]