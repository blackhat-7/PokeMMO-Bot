from itertools import cycle
import time

from core.player import Player
from pynput.mouse import Listener

import pyautogui as pt


if __name__ == '__main__':
    time.sleep(3)
    player = Player()
    movements = cycle([
        player.move_right,
        player.move_down,
        player.move_left,
        player.move_up
    ])
    while True:
        if player.is_in_battle_mode():
            print(f'Battling')
            player.battle()
        else:
            next(movements)()
            print(f'Moving')
        time.sleep(0.5)
    # pt.displayMousePosition()

    