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

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
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

hangman("camel")