def solution(s):
    s_len = len(s)
    current_sq = ''
    max_parts_amount = 1
    for i in s:
        current_sq += i
        current_sq_len = len(current_sq)
        checked_parts = 1
        valid_part = True
        if s_len % current_sq_len == 0:
            while checked_parts < s_len // current_sq_len and valid_part:
                if current_sq != s[(current_sq_len * checked_parts):(current_sq_len * (checked_parts + 1))]:
                    valid_part = False
                else:
                    max_parts_amount += 1
                    checked_parts += 1
        else:
            valid_part = False
        if valid_part:
            return max_parts_amount
        else:
            max_parts_amount = 1
