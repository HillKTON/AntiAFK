import colorama


def main():
    colorama.init()
    logo = f'AntiAFK Script'
    text = 'Для запуска или остановки скрипта нажмите F7...'
    print(colorama.Fore.LIGHTRED_EX + logo)
    print(colorama.Fore.CYAN + text)
    print(colorama.Style.RESET_ALL)


def information(type_inf: str):
    if type_inf == 'on':
        text = '[Info] Скрипт включен...'
        print(colorama.Fore.YELLOW + text)
        print(colorama.Style.RESET_ALL)
    elif type_inf == 'off':
        text = '[Info] Скрипт выключен...'
        print(colorama.Fore.YELLOW + text)
        print(colorama.Style.RESET_ALL)
