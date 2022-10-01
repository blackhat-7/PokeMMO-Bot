import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import pyautogui as pt

from core.game import Game
from core.game_object import GameObject
from core import utils

class Player:
    def __init__(self):
        self.keyboard = KeyboardController()
        self.mouse = MouseController()
        self.x = Game.width // 2
        self.y = Game.height // 2

    def move_up(self):
        print("move_up")
        self.keyboard.press(Key.up)
        time.sleep(0.5)
        self.keyboard.release(Key.up)
    
    def move_down(self):
        print("move_down")
        self.keyboard.press(Key.down)
        time.sleep(0.5)
        self.keyboard.release(Key.down)
    
    def move_left(self):
        print("move_left")
        self.keyboard.press(Key.left)
        time.sleep(0.5)
        self.keyboard.release(Key.left)
    
    def move_right(self):
        print("move_right")
        self.keyboard.press(Key.right)
        time.sleep(0.5)
        self.keyboard.release(Key.right)

    def accept(self):
        self.keyboard.tap("z")
    
    def reject(self):
        self.keyboard.tap("x")
    
    def is_at_loc(self, x, y):
        if self.x <= x <= self.x + 100 \
            and self.y <= y <= self.y + 100:
                return True
        return (x - self.x, y - self.y)
    
    def move_to_loc(self, x, y):
        reached = False
        while not self.is_at_loc(x, y):
            x_diff, y_diff = self.is_at_loc(x, y)
            if x_diff > 0:
                self.move_right()
            elif x_diff < 0:
                self.move_left()
            if y_diff > 0:
                self.move_down()
            elif y_diff < 0:
                self.move_up()
            time.sleep(1)
        
    def is_in_battle_mode(self):
        fight_menu1 = utils.locate_object(['fight', 'menu1.png'])
        fight_menu2 = utils.locate_object(['fight', 'menu2.png'])
        return len(fight_menu1.locations) > 0 or len(fight_menu2.locations) > 0

    def battle(self):
        while self.is_in_battle_mode():
            pt.leftClick(500, 1100)
            time.sleep(0.5)
    
    def choose_my_move(self, move: str):
        if move == "fight":
            pt.click(500, 1100)
        elif move == "bag":
            pt.click(700, 1100)
        elif move == "pokemon":
            pt.click(500, 1150)
        elif move == "run":
            pt.click(700, 1150)

    def choose_battle_move(self, move: int):
        if move == 1:
            pt.click(500, 1100)
        elif move == 2:
            pt.click(700, 1100)
        elif move == 3:
            pt.click(500, 1150)
        elif move == 4:
            pt.click(700, 1150)
            

            

