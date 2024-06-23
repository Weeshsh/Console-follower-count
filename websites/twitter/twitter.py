import tweepy
from time import sleep
from rich.console import Console
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()


def dodaj_konto_twitter():
    console = Console()
    with open("./websites/twitter/accounts.txt", "a") as f:
        console.print("Wpisz nazwę konta:", style="bold cyan")
        name = input()
        if type(twitter(name)) == int:
            f.write(f"{name}\n")
            console.print("Pomyślnie zapisano konto!", style="bold green")
            sleep(1.5)
            os.system("cls")


def twitter(name):
    consumer_key = os.getenv("CONSUMER_KEY")
    print(consumer_key)
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        user = api.get_user(screen_name=name)
        return user.followers_count

    except tweepy.TweepError as e:
        print(f"Error: {e}")
