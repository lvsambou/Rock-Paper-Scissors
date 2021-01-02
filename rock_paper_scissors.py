from random import randint
from time import sleep


usr_scores = 0
cmptr_scores = 0


def start():
    play = """
    ......Let's play !......
    ..........Rock..........
    .........Paper..........
    ........Scissors........
    
    """
    print(play)
    while game():
        pass
    scores()


def game():
    usr = move()
    cmptr = randint(1, 3)
    verif(usr, cmptr)
    result(usr, cmptr)
    return play_again()


def move():
    while True:
        print()
        usr = input("1 - Rock, 2 - Paper, 3 - Scissors\nPlease enter your choice : ")
        try:
            usr = int(usr)
            if usr in (1, 2, 3):
                return usr
        except ValueError:
            pass
        print("I didn't understand that... Please enter 1, 2 or 3.")


def verif(usr, cmptr):
    res = 0
    if usr == 1 and cmptr == 2:
        res = 1
    elif usr == 2 and cmptr == 1:
        res = 2
    elif usr == 3 and cmptr == 1:
        res = 3
    elif usr == 3 and cmptr == 2:
        res = 4
    elif usr == 2 and cmptr == 3:
        res = 5
    elif usr == 1 and cmptr == 3:
        res = 6
    return res


def result(usr, cmptr):
    print("...")
    sleep(1)
    print("...")
    sleep(1)
    print("...")
    sleep(0.5)
    print("Computer make his games...")
    global usr_scores, cmptr_scores
    if usr == cmptr:
        print("Tie game.")
    else:
        if verif(usr, cmptr) in (2, 4, 6):
            print("You Won ! Well played !")
            usr_scores += 1
        else:
            print("Computer unlucky won... Sorry for you !")
            cmptr_scores += 1


def play_again():
    ask = input("Do you want to play again ? (y/n) ")
    if ask.lower() in ("y", "yes", "yeah", "of course"):
        return ask
    else:
        print("Ok, thanks for playing with us ! See ya' ")


def scores():
    global usr_scores, cmptr_scores
    print("HIGH SCORES")
    print("Player : ", usr_scores)
    print("Computer : ", cmptr_scores)


if __name__ == '__main__':
    start()
