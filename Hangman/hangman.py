#hangman game - start
import random

def hangman():
    """Hangman game"""
    
    word_list = ["japan", "ghana", "austria", "australia","nicaragua", "jamaica", "england"]
    random_number = random.randint(0,6)
    word = word_list[random_number]
    wrong = 0
    stages = ["",
             "____________          ",
             "|                     ",
             "|           |         ",
             "|           0         ",
             "|          /|\     ",
             "|          / \     ",
             "|                     "
             ]

    rletters = list(word)
    board = ["___"] * len(word)
    win = False
    print("Welcome to Hangman")
    game_over = input("Quit game now: Yes or No: ")
    if "yes" == game_over.lower():
        print("See you another time!")
        
    else:
        while wrong < len(stages) - 1:
            print("\n")
            char = input("Guess a letter: ")
            if char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
            else:
                wrong += 1
            print((" ".join(board)))
            e = wrong + 1
            print("\n".join(stages[0: e]))
            if "___" not in board:
                print("You win!")
                print(" ".join(board))
                win = True
                break
        if not win:
            print("\n".join(stages[0: wrong]))
            print("You lose! it was {}.".format(word))

hangman()