def hangman(word):
    wrong = 0
    stages = ["",
        "__________         ",
              
        "|         |        ",
              
        "|         |        ",
              
        "|         0        ",
              
        "|        /|\       ",

        "|        / \       ",

        "|                  "
        ]
    rletters = list(word)
    board = ["___"]*len(word)
    win = False
    print("welcome to Hangmen!")

    while wrong < len(stages) - 1:
        print("\n")
        msq = "Guess a letter: "
        char = input(msq)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters = "$"
        else:
            wrong +=1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "___" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was " + word)

hangman("dog")
    
