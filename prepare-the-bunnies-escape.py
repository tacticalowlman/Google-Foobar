import time

def print_map(map, x, y):
    for i in range(len(map)):
        map_str = ""
        for k in range(len(map[0])):
            if k == x and i == y:
                map_str += f"@ "
            elif k == len(map[0]) and i == len(map):
                map_str += f"X "
            else:
                map_str += f"{map[i][k]} "
        print(map_str)


def min_path_len(map, x_pos, y_pos):
    return abs(len(map[0]) - x_pos) + abs(len(map) - y_pos) - 1


def path_finder(map, path):
    x_pos = path[-1][0]
    y_pos = path[-1][1]
    print_map(map, x_pos, y_pos)
    possible_moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    unsorted_moves = []
    moves = []
    min_path_size = 100
    for move in possible_moves:
        x_nbr = x_pos + move[0]
        y_nbr = y_pos + move[1]
        if 0 <= x_nbr <= len(map[0]) - 1 and 0 <= y_nbr <= len(map) - 1 and map[y_nbr][x_nbr] == 0 and [x_nbr, y_nbr] not in path:
            unsorted_moves.append([x_nbr, y_nbr])
    print(unsorted_moves)
    while unsorted_moves:
        min_path = 100
        min_path_i = 0
        for i, move in enumerate(unsorted_moves):
            path_len = min_path_len(map, move[0], move[1])
            print("path size", move[0], move[1], path_len, i)
            if path_len < min_path:
                min_path_i = i
                min_path = path_len
        print("min is", min_path_i)
        moves.append(unsorted_moves.pop(min_path_i))
    print(moves)
    time.sleep(0.25)
    for move in moves:
        if move[0] == len(map[0]) - 1 and move[1] == len(map) - 1:
            print("STOP!")
            return 2
        else:
            path.append([move[0], move[1]])
            path_size = path_finder(map, path)
            if path_size != 0:
                return path_size + 1
            else:
                continue
    return 0


def solution(map):
    min_path_size = min_path_len(map, 0, 0)
    path_size = path_finder(map, [[0, 0]])
    print("COUNTER PATH SIZE", path_size)
    if path_size <= min_path_size:
        return path_size
    else:
        current_min_path_size = 100
        for i in range(len(map)):
            for k in range(len(map[0])):
                if map[i][k] == 1:
                    map[i][k] = 0
                    path_size = path_finder(map, [[0, 0]])
                    if path_size <= min_path_size:
                        return path_size
                    elif path_size < current_min_path_size:
                        current_min_path_size = path_size
                    map[i][k] = 1
    return current_min_path_size


mx = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


print(solution(mx))
