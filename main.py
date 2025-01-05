# WELCOME TO GOOBED'S CONNECT 4 GAME
import connect4board
import Winloss
import BoardList
import random

# Function to place opponent's piece
def place_opponent_piece(choice):
    ranges = {1: (1, 3), 2: (1, 3), 3: (2, 4), 4: (3, 5), 5: (4, 6), 6: (5, 7), 7: (5, 7)}
    randNum = random.randint(*ranges[choice])
    columns = {
        1: ["cc", "v", "o", "h", "a"], 2: ["dd", "w", "p", "i", "b"], 3: ["ee", "x", "q", "j", "c"],
        4: ["ff", "y", "r", "k", "d"], 5: ["gg", "z", "s", "l", "e"], 6: ["hh", "aa", "t", "m", "f"],
        7: ["ii", "bb", "u", "n", "g"]
    }
    for key in columns[randNum]:
        if BoardList.d[key] == " ":
            BoardList.d[key] = "O"
            break

# Function to reset the board
def reset_board():
    for key in BoardList.d.keys():
        BoardList.d[key] = " "

# Function to handle a move
def handle_move(choice, symbol):
    columns = {1: ["cc", "v", "o", "h", "a"], 2: ["dd", "w", "p", "i", "b"], 3: ["ee", "x", "q", "j", "c"],
               4: ["ff", "y", "r", "k", "d"], 5: ["gg", "z", "s", "l", "e"], 6: ["hh", "aa", "t", "m", "f"],
               7: ["ii", "bb", "u", "n", "g"]}
    for key in columns[choice]:
        if BoardList.d[key] == " ":
            BoardList.d[key] = symbol
            break

# Main game function
def MainGame():
    looper, loopster = True, True
    MyVal2 = 0

    while loopster:
        print("╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╭╮╱╭╮")
        print("┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮┃┃╱┃┃")
        print("┃╰━━┳╮╭┳━━┳━━┳━╮┃┃╱╰╋━━┳━╮╭━╮╭━━┳━┻╮╭╯┃╰━╯┃")
        print("╰━━╮┃┃┃┃╭╮┃┃━┫╭╯┃┃╱╭┫╭╮┃╭╮┫╭╮┫┃━┫╭━┫┃╱╰━━╮┃")
        print("┃╰━╯┃╰╯┃╰╯┃┃━┫┃╱┃╰━╯┃╰╯┃┃┃┃┃┃┃┃━┫╰━┫╰╮╱╱╱┃┃")
        print("╰━━━┻━━┫╭━┻━━┻╯╱╰━━━┻━━┻╯╰┻╯╰┻━━┻━━┻━╯╱╱╱╰╯")
        print("╱╱╱╱╱╱╱┃┃")
        print("╱╱╱╱╱╱╱╰╯")

        intro = input("          𝕋𝕪𝕡𝕖 𝔼 ℕ 𝕋 𝔼 ℝ 𝕥𝕠 𝕡𝕝𝕒𝕪\n")
        if intro.lower() != "enter":
            print("Try again")
            continue

        connect4board.connect4board()

        while looper:
            choice = int(input("Where would you like to drop a chip? (Enter 1 - 7)"))
            handle_move(choice, "X")
            place_opponent_piece(choice)
            connect4board.connect4board()
            result = Winloss.Winloss(MyVal2)
            if result == 1:
                print("YOU WIN!")
            elif result == 2:
                print("YOU LOST! :(")
            if result in [1, 2]:
                looper = False
                another = input("Would you like to play again? (Enter Yes or No)\n")
                if another.lower() == "yes":
                    reset_board()
                    looper = loopster = True
                else:
                    loopster = False

MainGame()