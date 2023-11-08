def solution(l):
    ct = 0
    ct_l = [0] * len(l)
    for i in range(len(l)):
        for k in range(i):
            if l[i] % l[k] == 0:
                ct_l[i] += 1
                ct += ct_l[k]
    return ct

