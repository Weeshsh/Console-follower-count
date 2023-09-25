import tweepy
from time import sleep
from rich.console import Console
import os


def dodaj_konto_twitter():
    console = Console()
    with open('./websites/twitter/accounts.txt', 'a') as f:
        console.print('Wpisz nazwę konta:', style = 'bold cyan')
        name = input()
        if type(twitter(name)) == int:
            f.write(f'{name}\n')
            console.print('Pomyślnie zapisano konto!', style = 'bold green')
            sleep(1.5)
            os.system('cls')


def twitter(name):
    consumer_key = 'Sx2Jl3bA5Cph678VJPKgbIa8i'
    consumer_secret = 'pbgHqTqVorSGiAx6eFo6qDBUQ1VSz8AiUZ5zfZ80hrympw16Xc'
    access_token = '1436008801765842944-esfdLAiCoahD19iEZ7rXOZ1sdz27hk'
    access_token_secret = 'MtRBWoz6Jm1NgFwBsCY3vnb1KkJj5VrOT9xlV3jr7c55T'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        user = api.get_user(screen_name=name)
        return user.followers_count

    except tweepy.TweepError as e:
        print(f"Error: {e}")