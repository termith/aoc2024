def is_increasing(sequence, tolerate=False):
    i = 1
    while i < len(sequence):
        diff = sequence[i] - sequence[i-1]
        if diff <= 0 or diff > 3:
            if tolerate:
                return is_increasing(sequence[:i-1] + sequence[i:], False) or is_increasing(sequence[:i] + sequence[i+1:], False)
            else:
                return False
        i += 1
    return True

def part_one():
    safe_levels_count = 0
    with open('day2/input.txt') as f:
        for line in f: 
            levels = list(map(int, line.split()))
            if is_increasing(levels) or is_increasing(list(reversed(levels))):
                safe_levels_count += 1
    return safe_levels_count

def part_two():
    safe_levels_count = 0
    with open('day2/input.txt') as f:
        for line in f: 
            levels = list(map(int, line.split()))
            if is_increasing(levels, True) or is_increasing(list(reversed(levels)), True):
                safe_levels_count += 1
    return safe_levels_count

if __name__ == '__main__':
    print(part_one())
    print(part_two())