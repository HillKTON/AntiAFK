from pynput.keyboard import Key, Listener

import interface
from bot import Bot


bot = Bot()


def on_press(key):
    if key == Key.f7:
        if bot.alive:
            bot.alive = False
            interface.information(type_inf='off')
        else:
            bot.alive = True
            interface.information(type_inf='on')


def main():
    interface.main()
    bot.start()
    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == '__main__':
    main()
