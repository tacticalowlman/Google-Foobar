def increment_series_count(base, increment, n):
    for i in range(n - 1):
        base += increment
        increment += 1
    return base


def solution(x, y):
    column_base = increment_series_count(1, 2, x)
    return str(increment_series_count(column_base, x, y))

