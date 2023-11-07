def solution(map):
    end = (len(map) - 1, len(map[0]) - 1)
    visited = set()
    buffer = [[True, 1, (0, 0)]]
    while buffer:
        e = buffer.pop(0)
        removal, step, node = e[0], e[1], e[2]
        if (removal, node) in visited:
            continue
        visited.add((removal, node))
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = node[0] + dy, node[1] + dx
            if 0 <= ny <= end[0] and 0 <= nx <= end[1]:
                if (ny, nx) == end:
                    return step + 1
                elif map[ny][nx] == 0:
                    buffer += [[removal, step + 1, (ny, nx)]]
                elif removal:
                    buffer += [[False, step + 1, (ny, nx)]]
        buffer = sorted(buffer, key=lambda x: x[1] + end[0] - x[2][0] + end[1] - x[2][1] + 1)




