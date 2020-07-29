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
    copy = grid.copy()
    for row_num, row in enumerate(copy):
        for column_num, item in enumerate(row):
            copy[row_num][column_num] = replace[item]
    return copy

def check_win(grid: list) -> [bool, str]:
    for line in lines:
        a = grid[line[0][0]][line[0][1]]
        b = grid[line[1][0]][line[1][1]]
        c = grid[line[2][0]][line[2][1]]
        if a == b == c:
            if a == 0:
                pass
            elif a == 1:
                return True, "x"
            elif a == 2:
                return True, "o"
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
        if is_win[0]:
            print(empty_coords)
            return empty_coords

    for empty_coords in empty:
        print("No immediate win")
        new_grid = deepcopy(grid)
        new_grid[empty_coords[0]][empty_coords[1]] = player
        return best_move(new_grid, player)


grid_a = ([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])

best_move(grid_a, 1)
for l in humanize_grid(grid_a):
    print(l)
