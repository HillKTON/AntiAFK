from os import system

import colorama
from main import __version__


def logo():
    logo_text = f'AntiAFK Script ({__version__})'
    print(f'{colorama.Fore.LIGHTRED_EX}{logo_text}'
          f'{colorama.Style.RESET_ALL}\n')


def main():
    colorama.init()
    system('cls')
    logo()
    mods = '1. [Круговой] Ваш персонаж будет ходить по кругу\n' \
           '2. [Туда-сюда] Ваш персонаж будет ходить из стороны в сторону'
    print(f'{colorama.Fore.CYAN}{mods}'
          f'{colorama.Style.RESET_ALL}\n')


def info():
    system('cls')
    logo()
    text = 'Для запуска или остановки скрипта нажмите F7...\n' \
           'Для выхода в клавное меню нажмите ESC...'
    print(f'{colorama.Fore.LIGHTCYAN_EX}{text}'
          f'{colorama.Style.RESET_ALL}\n\n\n')


def log(type_inf: str):
    if type_inf == 'on':
        text = '[Info] Скрипт включен...'
        print(f'{colorama.Fore.YELLOW}{text}'
              f'{colorama.Style.RESET_ALL}')
    elif type_inf == 'off':
        text = '[Info] Скрипт выключен...'
        print(f'{colorama.Fore.YELLOW}{text}'
              f'{colorama.Style.RESET_ALL}')


def error():
    system('cls')
    logo()
    text = 'Вы указали неверное значение...\n' \
           'Для продолжение нажмите Enter'
    input(f'{colorama.Fore.RED}{text}'
          f'{colorama.Style.RESET_ALL}\n\n\n')
