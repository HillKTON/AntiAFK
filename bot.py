from threading import Thread
from time import sleep

from pynput.keyboard import Controller


class Bot(Thread):
    def __init__(self):
        super(Bot, self).__init__()
        self.alive = True

    def run(self):
        keyboard = Controller()
        buttons = ('w', 'd', 's', 'a')
        while self.alive:
            for bt in buttons:
                keyboard.press(bt)
                sleep(.2)
                keyboard.release(bt)
