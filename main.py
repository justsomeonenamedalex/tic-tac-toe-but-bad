from copy import deepcopy

base_grid = ([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])

lines = ([
    [(0, 0), (0, 1), (0, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 1), (2, 0)],
    [(0, 2), (1, 2), (2, 2)],
    [(1, 2), (1, 1), (1, 0)],
    [(2, 2), (2, 1), (2, 0)]
])


# 0 is an empty space, 1 is x, 2 is o

def humanize_grid(grid: list) -> list:
    replace = {0: "#", 1: "x", 2: "o"}
    copy = deepcopy(grid)
    for row_num, row in enumerate(copy):
        for column_num, item in enumerate(row):
            copy[row_num][column_num] = replace[item]

    out = [" ".join(line) for line in copy]
    return "\n".join(out)


def check_win(grid: list) -> [bool, int]:
    for line in lines:
        a = grid[line[0][0]][line[0][1]]
        b = grid[line[1][0]][line[1][1]]
        c = grid[line[2][0]][line[2][1]]
        if a == b == c:
            if a == 0:
                pass
            elif a == 1:
                return True, 1
            elif a == 2:
                return True, 2
    return False, ""


def best_move(grid: list, player: int):
    empty = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 0:
                empty.append([y, x])

    for empty_coords in empty:
        new_grid = deepcopy(grid)
        new_grid[empty_coords[0]][empty_coords[1]] = player
        is_win = check_win(new_grid)
        if is_win[0] and is_win[1] == player:
            # print(empty_coords)
            return empty_coords

    for empty_coords in empty:
        # print("No immediate win")
        new_grid = deepcopy(grid)
        new_grid[empty_coords[0]][empty_coords[1]] = player
        return best_move(new_grid, player)


# grid_a = ([
#     [2, 1, 1],
#     [0, 2, 2],
#     [0, 1, 1]
# ])
#
# best_move(grid_a, 2)
# for l in humanize_grid(grid_a):
#     print(l)

def cli():
    grid = deepcopy(base_grid)
    play_to_coords = {
        "1": [0, 0],
        "2": [0, 1],
        "3": [0, 2],
        "4": [1, 0],
        "5": [1, 1],
        "6": [1, 2],
        "7": [2, 0],
        "8": [2, 1],
        "9": [2, 2]
    }
    print(humanize_grid(grid))

    while True:

        while True:
            print("\nYour turn!")
            play = input("Where do you want to play to?(1-9) ")
            try:
                coords = play_to_coords[play]
                break
            except KeyError:
                print("That isnt a valid square")

        grid[coords[0]][coords[1]] = 1

        print(humanize_grid(grid))
        is_win = check_win(grid)
        if is_win[0]:
            print(f"{is_win[1]} wins!")
            break

        print("\nAI's turn!")

        ai_coords = best_move(grid, 2)
        grid[ai_coords[0]][ai_coords[1]] = 2

        print(humanize_grid(grid))
        is_win = check_win(grid)
        if is_win[0]:
            print(f"{is_win[1]} wins!")
            break


cli()
