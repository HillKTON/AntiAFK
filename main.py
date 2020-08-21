from pynput.keyboard import Key, Listener
from bot import Bot
from sys import exit


bot = Bot()


def stop(key):
    if key == Key.insert:
        bot.alive = False
        exit(0)


def main():
    bot.start()
    with Listener(on_press=stop) as listener:
        listener.join()


if __name__ == '__main__':
    main()
