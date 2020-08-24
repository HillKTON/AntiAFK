from pynput.keyboard import Key, Listener

import interface
from bot import Bot


__version__ = '24.08.2020'


def on_press(key):
    if key == Key.f7:
        if bot.alive:
            bot.alive = False
            interface.log(type_inf='off')
        else:
            bot.alive = True
            interface.log(type_inf='on')
    elif key == Key.esc:
        bot.alive = False
        bot.mod = None
        main()


def main():
    while True:
        interface.main()
        user_input = input('>> ')
        if user_input in ('1', '2'):
            bot.mod = int(user_input)
            interface.info()
            break
        else:
            interface.error()


if __name__ == '__main__':
    bot = Bot()
    bot.start()
    main()
    with Listener(on_press=on_press) as listener:
        listener.join()
