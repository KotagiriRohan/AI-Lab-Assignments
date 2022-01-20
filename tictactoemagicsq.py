from random import choice

from itertools import combinations

playing_board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
fixed_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
human_moves = []*5
computer_moves = []*4
positions_left = [1, 2, 3, 4, 5, 6, 7, 8, 9]
magic_positions_left = [1, 2, 3, 4, 5, 6, 7, 8, 9]
magic_square_board = [8, 3, 4, 1, 5, 9, 6, 7, 2]
player = "human"
turn = 1
won = False
new_position = 0


class switch:
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return False

    def __call__(self, *values):
        return self.value in values


def displayBoard(arr):
    print("\t" + str(arr[0]) + " | " + str(arr[1]) + " | " + str(arr[2]))
    print("\t--------")
    print("\t" + str(arr[3]) + " | " + str(arr[4]) + " | " + str(arr[5]))
    print("\t--------")
    print("\t" + str(arr[6]) + " | " + str(arr[7]) + " | " + str(arr[8]))


def initializeGame():
    print("\n\n############################################")
    print("\tGame - Tic Tac Toe(Magic Square)!")
    print("############################################\n\n")
    print("Board positions:\n")
    displayBoard(fixed_positions)
    print("\n\nInitial Board:\n")
    displayBoard(playing_board)
    print("\n-------------------------------------------------------------------")


def setPlayer():
    global player
    player = "human" if (turn % 2) else "computer"


def generateRandomPosition():
    return choice(positions_left)


def addPositionToBoard(position):
    magic_square_value = magic_square_board[int(position)-1]
    playing_board[int(position)-1] = "X" if (player == "human") else "O"
    positions_left.remove(int(position))
    magic_positions_left.remove(magic_square_value)
    human_moves.append(magic_square_value) if (
        player == "human") else computer_moves.append(magic_square_value)
    increamentTurn()


def increamentTurn():
    global turn
    turn += 1


def checkInput(value):
    return 1 if (value.isdigit() and int(value) > 0 and int(value) < 10 and int(value) in positions_left) else 0


def takeInput():
    human_input = input()
    input_passed = checkInput(human_input)
    if (input_passed):
        return human_input
    else:
        print("Please enter a valid position!")
        return 0


def displayChanceInformation():
    if(player == "human"):
        while (True):
            print("\n\nTurn " + str(turn) + " -> " + "You (Enter any position from " +
                  str(positions_left) + "): ", end=' ')
            human_input = takeInput()

            if human_input:
                break

            else:
                continue
        print()
        return human_input
    else:
        print("\n\nTurn " + str(turn) + " -> " + "Computer\n")


def displayWinningStatement():
    print("\n\n#############################\n")
    print("\t   You Won!" if (player == "human") else "\tComputer Won!")
    print("\n#############################\n\n")


def displayDrawStatement():
    print("\n\n###########################\n")
    print("\tGame draw!")
    print("\n###########################\n\n")


def checkIfWon(arr):
    for combination in combinations(human_moves if (player == "human") else computer_moves, 3):
        if (sum(combination) == 15):
            global won
            won = True
            break


def humanChance():
    human_input = displayChanceInformation()
    addPositionToBoard(human_input)
    if (turn > 3):
        checkIfWon(human_moves)


def computerChance():
    displayChanceInformation()
    new_random_position = generateRandomPosition()
    addPositionToBoard(new_random_position)


def checkWinningPosition(player):
    winning_position_exists = False
    for combination in combinations(human_moves if (player == "human") else computer_moves, 2):
        colinear_condition_variable = 15 - sum(combination)
        if (colinear_condition_variable < 10 and colinear_condition_variable > 0 and colinear_condition_variable in magic_positions_left):
            global new_position
            new_position = magic_square_board.index(
                colinear_condition_variable) + 1
            winning_position_exists = True

            if (player == "computer"):
                global won
                won = True
            break

    return winning_position_exists



def startGame():
    while (turn != 10):
        setPlayer()
        with switch(turn) as case:
            if case(1, 2, 3):
                if (player == "computer"):
                    computerChance()
                else:
                    humanChance()
                displayBoard(playing_board)
            elif case(4, 5, 6, 7, 8, 9):
                if (player == "human"):
                    humanChance()
                else:
                    displayChanceInformation()
                    if (checkWinningPosition('computer')):
                        addPositionToBoard(new_position)
                    elif (checkWinningPosition('human')):
                        addPositionToBoard(new_position)
                    else:
                        computerChance()
                displayBoard(playing_board)
            else:
                print("Please enter a valid position!\n\n")
            if (won):
                displayWinningStatement()
                break
    if (not won):
        displayDrawStatement()

if __name__ == "__main__":
    initializeGame()
    startGame()
