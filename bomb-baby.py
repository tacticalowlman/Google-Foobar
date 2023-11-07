def solution(m, f):
    m = int(m)
    f = int(f)
    ct = 0
    while m != 1 or f != 1:
        if (m == f or m % f == 0 or f % m == 0) and m != 1 and f != 1:
            return 'impossible'
        elif m > f:
            if m // f > 1 and m % f != 0:
                ct += m // f
                m = m % f
            else:
                m = m - f
                ct += 1
        else:
            if f // m > 1 and f % m != 0:
                ct += f // m
                f = f % m
            else:
                f = f - m
                ct += 1
    return str(ct)
