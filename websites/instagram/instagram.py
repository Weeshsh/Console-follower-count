import instaloader
from rich.console import Console
import os
from time import sleep
from dotenv import load_dotenv

load_dotenv()


def dodaj_konto_instagram():
    console = Console()
    with open("./websites/instagram/accounts.txt", "a") as f:
        console.print("Wpisz nazwę konta:", style="bold cyan")
        name = input()
        if type(instagram(name)) == int:
            f.write(f"{name}\n")
            console.print("Pomyślnie zapisano konto!", style="bold green")
            sleep(1.5)
            os.system("cls")


import instaloader


def instagram(name):
    bot = instaloader.Instaloader()
    username = os.getenv("INST_USERNAME")
    print(username)
    password = os.getenv("INST_PASSWORD")
    bot.login(username, password)
    profile = instaloader.Profile.from_username(bot.context, name)

    return profile.followers
