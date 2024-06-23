from rich.console import Console
import os
import sys
import time
from websites.instagram.instagram import instagram, dodaj_konto_instagram
from websites.twitter.twitter import twitter, dodaj_konto_twitter
from websites.tiktok.tiktok import tiktok, dodaj_konto_tiktok


def slowprint(text):
    for c in text + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)


def output():
    console = Console()
    # instagram
    if os.stat("./websites/instagram/accounts.txt").st_size != 0:
        with open("./websites/instagram/accounts.txt") as f:
            console.print("---Instagram---", style="yellow")
            for line in f:
                name = line.strip()
                follower_count = "{:,}".format(instagram(name))
                slowprint(f"{name} -> {follower_count}")

    # twitter
    if os.stat("./websites/twitter/accounts.txt").st_size != 0:
        with open("./websites/twitter/accounts.txt") as f:
            console.print("---Twitter---", style="blue")
            for line in f:
                name = line.strip()
                follower_count = "{:,}".format(twitter(name))
                slowprint(f"{name} -> {follower_count}")

    # tiktok
    if os.stat("./websites/tiktok/accounts.txt").st_size != 0:
        with open("./websites/tiktok/accounts.txt") as f:
            console.print("---TikTok---", style="magenta")
            for line in f:
                name = line.strip()
                follower_count = "{:,}".format(tiktok(name))
                slowprint(f"{name} -> {follower_count}")


def main():
    os.system("cls")
    console = Console()
    console.print(
        "Witam w programie który sprawdza aktualny follower count konta na danej stronie.",
        style="bold cyan",
    )
    console.print("Czy chcesz dodać nowe konta do swojej listy?", style="bold cyan")
    console.print("[1] [green] Tak")
    console.print("[2] [red] Nie, pokaż wyniki")
    temp1 = int(input())
    os.system("cls")
    match temp1:
        case 1:
            console.print("Wybierz platformę z poniższch opcji:", style="bold cyan")
            console.print("[1] [yellow]Instagram")
            console.print("[2] [blue]Twitter")
            console.print("[3] [magenta]TikTok")
            temp2 = int(input())
            os.system("cls")
            match temp2:
                case 1:
                    dodaj_konto_instagram()
                    console.print("Czy chcesz dodać kolejne konto?", style="bold cyan")
                    console.print("[1] [green] Tak")
                    console.print("[2] [red] Nie")
                    temp3 = int(input())
                    os.system("cls")
                    while temp3 != 2:
                        dodaj_konto_instagram()
                        console.print(
                            "Czy chcesz dodać kolejne konto?", style="bold cyan"
                        )
                        console.print("[1] [green] Tak")
                        console.print("[2] [red] Nie")
                        temp3 = int(input())
                        os.system("cls")
                case 2:
                    dodaj_konto_twitter()
                    console.print("Czy chcesz dodać kolejne konto?", style="bold cyan")
                    console.print("[1] [green] Tak")
                    console.print("[2] [red] Nie")
                    temp3 = int(input())
                    os.system("cls")
                    while temp3 != 2:
                        dodaj_konto_twitter()
                        console.print(
                            "Czy chcesz dodać kolejne konto?", style="bold cyan"
                        )
                        console.print("[1] [green] Tak")
                        console.print("[2] [red] Nie")
                        temp3 = int(input())
                        os.system("cls")

                case 3:
                    pass
        case 2:
            output()


if __name__ == "__main__":
    main()
