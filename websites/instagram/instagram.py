import instaloader
from rich.console import Console
import os
from time import sleep


def dodaj_konto_instagram():
    console = Console()
    with open('./websites/instagram/accounts.txt', 'a') as f:
        console.print('Wpisz nazwę konta:', style = 'bold cyan')
        name = input()
        if type(instagram(name)) == int:
            f.write(f'{name}\n')
            console.print('Pomyślnie zapisano konto!', style = 'bold green')
            sleep(1.5)
            os.system('cls')


def instagram(name):
    bot = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(bot.context, name)
    return profile.followers