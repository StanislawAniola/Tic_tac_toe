def introduction():
    print("Creator: Stanislaw Aniola")
    print("Game: Tic Tac Toe")
    print("Version: 1.1")
    print()
    print()
    # __________________________Pre_Intro_________________________________________________
    print()
    print("          |      |  ||||||  |      /|||\  /||||\  |\    /|  ||||||")
    print("          |      |  |       |      |      |    |  | \  / |  |")
    print("          |  /\  |  |||||   |      |      |    |  |  \/  |  |||||")
    print("          | /  \ |  |       |      |      |    |  |      |  |")
    print("          |/    \|  ||||||  |||||  \|||/  \||||/  |      |  ||||||")
    print()
    print("                           ||||||||  /||||\ ")
    print("                              |      |    | ")
    print("                              |      |    | ")
    print("                              |      |    | ")
    print("                              |      \||||/ ")
    print()
    print("                        ||||||||  |    |  ||||||")
    print("                           |      |    |  |")
    print("                           |      ||||||  ||||| ")
    print("                           |      |    |  |")
    print("                           |      |    |  ||||||")
    print()
    print("                     ////\     /\    |\    /|  ||||||")
    print("                     |        /  \   | \  / |  |")
    print("                     | \\\    /    \  |  \/  |  |||||")
    print("                     |   \\   ||||||  |      |  |")
    print("                     \\\\\\\|   |    |  |      |  ||||||")
    print()
    xx = input("press enter to move on...")
    print()
    print("RULES")
    print("Game is a simple version of Tic Tac Toe game.")
    print("You will see the board fill with numbers between 1 and 9")
    print("If you want to fill the displayed board, enter the")
    print("number when you want to place your mark.")
    print()
    x = input("press enter to move on...")


# ____________________________Main_part_of_Tic_Tac_Toe_______________________________________________________
def allGame():
    # ______________________________Intro___________________________________________
    print()
    playerX = input("Player 'X', enter your name: ")
    print(playerX, "Your mark is 'X'")
    print()
    playerO = input("Player 'O', enter your name: ")
    print(playerO,  "Your mark is 'O'")
    print()
    x4 = input("press enter to start!")
    print()
    # _____________________________________Variables_used_in_functions________________________________________________________
    board = [" "]
    boardend = [" "]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mark = ("X", "O")

    # ______________________________Play_Again_Cases____________________________________________________________________
    def playAgain():
        print("If you want to play again press Y. If not press N")
        playAgainChecker = input("Your decision is: ")
        if playAgainChecker == "Y":
            allGame()
            boardend.pop()
        elif playAgainChecker == "N":
            boardend.append(" ")
            exeFunction()
        elif playAgainChecker != "Y" or playAgainChecker != "N":
            playAgain()

    # ________________________________Win_Cases_________________________________________________________________________
    def winCases():
        if b[0] == b[1] == b[2] == mark[0] or b[3] == b[4] == b[5] == mark[0] or b[6] == b[7] == b[8] == mark[0]:
            print("The winner is ", playerX)
            playAgain()
        if b[0] == b[3] == b[6] == mark[0] or b[1] == b[4] == b[7] == mark[0] or b[2] == b[5] == b[8] == mark[0]:
            print("The winner is ", playerX)
            playAgain()
        if b[0] == b[4] == b[8] == mark[0] or b[2] == b[4] == b[6] == mark[0]:
            print("The winner is ", playerX)
            playAgain()
        if b[0] == b[1] == b[2] == mark[1] or b[3] == b[4] == b[5] == mark[1] or b[6] == b[7] == b[8] == mark[1]:
            print("The winner is ", playerO)
            playAgain()
        if b[0] == b[3] == b[6] == mark[1] or b[1] == b[4] == b[7] == mark[1] or b[2] == b[5] == b[8] == mark[1]:
            print("The winner is ", playerO)
            playAgain()
        if b[0] == b[4] == b[8] == mark[1] or b[2] == b[4] == b[6] == mark[1]:
            print("The winner is ", playerO)
            playAgain()
        if b[0] != 1 and b[1] != 2 and b[2] != 3 and b[3] != 4 and b[4] != 5 and b[6] != 7 and b[7] != 8 and b[8] != 9:
            print("It's a DRAW!")
            playAgain()

    # ___________________Display_Table_______________________________________
    def displayTable():
        print()
        print(b[0], "|", b[1], "|", b[2])
        print("__", "__", "__")
        print(b[3], "|", b[4], "|", b[5])
        print("__", "__", "__")
        print(b[6], "|", b[7], "|", b[8])
        print()
        print()
        print()

    # ____________________Player_X_Move______________________________________
    def xMove():
        try:
            mark
            letter = int(input('player "X" input is: '))
            if b[letter - 1] == 'X' or b[letter - 1] == 'O':
                print("This place is occupied")
                print()
                print()
                xMove()
            else:
                b[letter - 1] = mark[0]
                displayTable()
        except:
            print()
            print("enter the integer between 1 and 9")
            print("_________________________________")
            xMove()

    # __________________Player_O_Move___________________________________________________
    def oMove():
        try:
            mark
            letter = int(input('player "O" input is: '))
            if b[letter - 1] == 'X' or b[letter - 1] == 'O':
                print("This place is occupied")
                print()
                print()
                oMove()
            else:
                b[letter - 1] = mark[1]
                displayTable()
        except:
            print()
            print("enter the integer between 1 and 9")
            print("_________________________________")
            oMove()

    # _____________________Main_Function_____________________________________

    def exeFunction():
        if board == boardend:
            while board == boardend:
                xMove()
                winCases()
                if board != boardend:
                    end()
                else:
                    oMove()
                    winCases()

    def end():
        print("Thank you for playing My Game! ")

    displayTable()
    exeFunction()


introduction()
allGame()
