#hangman game - start

def hangman(word):
    wrong = 0
    stages = ["",
             "____________          ",
             "|                     ",
             "|           |         ",
             "|           0         ",
             "|          /|\        ",
             "|          / \        ",
             "|                     "
             ]

    rletters = list(word)
    board = ["___"] * len(word)
    win = False
    print("Welcome to Hangman")