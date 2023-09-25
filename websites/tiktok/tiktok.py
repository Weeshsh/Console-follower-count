from time import sleep
from rich.console import Console
import os


def dodaj_konto_tiktok():
    console = Console()
    with open('./websites/tiktok/accounts.txt', 'a') as f:
        console.print('Wpisz nazwę konta:', style = 'bold cyan')
        name = input()
        if type(tiktok(name)) == int:
            f.write(f'{name}\n')
            console.print('Pomyślnie zapisano konto!', style = 'bold green')
            sleep(1.5)
            os.system('cls')


def tiktok(name):
    pass