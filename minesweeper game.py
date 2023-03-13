import random
import numpy as np


def game_end(game, row, column):
    gameend = np.empty_like(game, dtype='object')
    for i in range(row):
        for j in range(column):
            if game[i][j] == -1:
                gameend[i][j] = "Bomb"
            else:
                gameend[i][j] = str(game[i][j])
    return gameend


def gameboard(game_display, game, urow, ucolumn):
    if game[urow][ucolumn] != 0:
        game_display[urow][ucolumn] = game[urow][ucolumn]
        return game_display
    else:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                ni = urow + i
                nj = ucolumn + j
                if ni < 0 or ni >= game.shape[0] or nj < 0 or nj >= game.shape[1]:
                    continue
                else:
                    if str(game_display[ni][nj]) != " ":
                        continue
                    else:
                        game_display[ni][nj] = str(game[ni][nj])
                        if game[ni][nj] == 0 and (i != 0 or j != 0):
                            gameboard(game_display, game, ni, nj)
    return game_display


def set_numbers(game, row, column):
    for i in range(row):
        for j in range(column):
            if game[i][j] == 0:
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        new_i = i + di
                        new_j = j + dj
                        if new_i < 0 or new_i >= row or new_j < 0 or new_j >= column:
                            continue
                        if game[new_i][new_j] == -1:
                            game[i][j] += 1

    return game


def create_game(b, x, y):
    game = np.zeros(shape=(x * y), dtype=int)
    while True:
        game[random.randint(0, (x * y) - 1)] = -1
        if np.count_nonzero(game == -1) == b:
            break
    game = game.reshape(x, y)
    game = set_numbers(game, x, y)
    return game
def play_game():
    row = int(input("Enter row size:"))
    column = int(input("Enter column size:"))
    b = int(input("Enter number of bombs:"))
    while True:
        if b>row*column:
            print("Number of bombs exceed the limit ",row*column,". Enter another value: ")
            b = int(input("Enter number of bombs:"))
        else:
            break

    game = create_game(b, row, column)
    game_display = np.empty((row, column), dtype='<U5')
    game_display.fill(" ")
    gameend = game_end(game, row, column)
    print(game_display)
    while True:
        uinput = input("Enter row, column: ")
        urow, ucolumn = uinput.split(",")
        urow = int(urow) - 1
        ucolumn = int(ucolumn) - 1
        if game[urow][ucolumn] == -1:
            print("Game Over! Stepped on Bomb!")
            print(gameend)
            break
        else:
            game_display = gameboard(game_display, game, urow, ucolumn)
            print(game_display)
            if np.count_nonzero(game_display == " ") == b:
                print("Congratulations! You won!")
                break

while True:
    play_game()
    cont=input("Play another game? Press 'Y' to continue: ")
    if cont.lower() == 'y':
        continue
    else:
        break

