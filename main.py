moves = {
    "1": [" ", " ", " "],
    "2": [" ", " ", " "],
    "3": [" ", " ", " "]
}
players = ["X", "O"]
index = 0
move_made = False


def split(word):
    return [c for c in word]


def check_if_winner():
    global index

    print(f"    1    2    3  \n"
          f" 1 {moves['1'][0]}  | {moves['1'][1]}  | {moves['1'][2]}  \n"
          f"  ____+____+____\n"
          f" 2 {moves['2'][0]}  | {moves['2'][1]}  | {moves['2'][2]}  \n"
          f"  ____+____+____\n"
          f" 3 {moves['3'][0]}  | {moves['3'][1]}  | {moves['3'][2]}  \n")

    if moves['1'][0] == moves['1'][1] and moves['1'][1] == moves['1'][2] and moves['1'][0] != " ":
        print(f"{moves['1'][0]} wins.")
        index = 9
    elif moves['2'][0] == moves['2'][1] and moves['2'][1] == moves['2'][2] and moves['2'][0] != " ":
        print(f"{moves['2'][0]} wins.")
        index = 9
    elif moves['3'][0] == moves['3'][1] and moves['3'][1] == moves['3'][2] and moves['3'][0] != " ":
        print(f"{moves['3'][0]} wins.")
        index = 9
    elif moves['1'][0] == moves['2'][0] and moves['2'][0] == moves['3'][0] and moves['1'][0] != " ":
        print(f"{moves['1'][0]} wins.")
        index = 9
    elif moves['1'][1] == moves['2'][1] and moves['2'][1] == moves['3'][1] and moves['1'][1] != " ":
        print(f"{moves['1'][1]} wins.")
        index = 9
    elif moves['1'][2] == moves['2'][2] and moves['2'][2] == moves['3'][2] and moves['1'][2] != " ":
        print(f"{moves['1'][2]} wins.")
        index = 9
    elif moves['1'][0] == moves['2'][1] and moves['2'][1] == moves['3'][2] and moves['1'][0] != " ":
        print(f"{moves['1'][0]} wins.")
        index = 9
    elif moves['3'][2] == moves['2'][1] and moves['2'][1] == moves['1'][0] and moves['3'][2] != " ":
        print(f"{moves['3'][2]} wins.")
        index = 9


print("Welcome to Tic Tac Toe")
while index < 9:
    check_if_winner()

    if index % 2 != 0:
        move = input(f"{players[1]} moves (X, Y): ")
        while not move_made:
            if len(move) == 2:
                new_input = split(move)
                if moves[new_input[0]][int(new_input[1]) - 1] == " ":
                    moves[new_input[0]][int(new_input[1]) - 1] = "O"
                    move_made = True
                else:
                    move = input("Invalid move, please choose a coordinate that is empty (X, Y): ")
                    new_input = split(move)
            else:
                move = input("Invalid move, please choose a valid coordinate (X, Y): ")
    else:
        move = input(f"{players[0]} moves (X, Y): ")
        while not move_made:
            if len(move) == 2:
                new_input = split(move)
                if moves[new_input[0]][int(new_input[1]) - 1] == " ":
                    moves[new_input[0]][int(new_input[1]) - 1] = "X"
                    move_made = True
                else:
                    move = input("Invalid move, please choose a coordinate that is empty (X, Y): ")
                    new_input = split(move)
            else:
                move = input("Invalid move, please choose a valid coordinate (X, Y): ")

    move_made = False
    index += 1
    check_if_winner()
