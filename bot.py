from threading import Thread
from time import sleep

from pynput.keyboard import Controller


class Bot(Thread):
    def __init__(self):
        super(Bot, self).__init__()
        self.mod = None
        self.alive = False

    def run(self):
        keyboard = Controller()
        while True:
            while self.alive:
                if self.mod == 1:
                    for bt in ('w', 'd', 's', 'a'):
                        keyboard.press(bt)
                        sleep(.2)
                        keyboard.release(bt)
                elif self.mod == 2:
                    for bt in ('d', 'a'):
                        keyboard.press(bt)
                        sleep(1)
                        keyboard.release(bt)
            sleep(1)
