import math


def count_least_possible_nodes_left(current_path, x_dest, y_dest):
    x_src = current_path[-1][0]
    y_src = current_path[-1][1]
    moves_list = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
    min_steps_needed = 100
    if len(current_path) < 8:
        for move in moves_list:
            x = move[0]
            y = move[1]
            x_pos = x_src + x
            y_pos = y_src + y
            pos_d = math.sqrt((x_dest - x_pos) * (x_dest - x_pos) + (y_dest - y_pos) * (y_dest - y_pos))
            src_d = math.sqrt((x_dest - x_src) * (x_dest - x_src) + (y_dest - y_src) * (y_dest - y_src))
            if (pos_d < src_d and src_d > 2) or src_d <= 2:
                if x_pos == x_dest and y_pos == y_dest:
                    return 1
                elif [x_pos, y_pos] in current_path:
                    continue
                elif 0 <= x_pos < 8 and 0 <= y_pos < 8:
                    current_path.append([x_pos, y_pos])
                    res = count_least_possible_nodes_left(current_path, x_dest, y_dest) + 1
                    if res < min_steps_needed:
                        min_steps_needed = res
    current_path.pop()
    return min_steps_needed


def solution(src, dest):
    x_src, y_src = src % 8, src // 8
    x_dest, y_dest = dest % 8, dest // 8
    if x_src == x_dest and y_src == y_dest:
        return 0
    else:
        return count_least_possible_nodes_left([[-1, -1], [x_src, y_src]], x_dest, y_dest)


print(solution(0, 0))
