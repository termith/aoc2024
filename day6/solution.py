def get_rotation(direction):
    match direction:
        case 'up':
            return 'right'
        case 'down':
            return 'left'
        case 'left':
            return 'up'
        case 'right':
            return 'down'

def get_current_position(m):
    for i in range(0, len(m)):
        if (j := m[i].find('^')) != -1:
            return i, j


def part_one():
    with open('day6/input.txt') as f:
        lab_map = f.readlines()
    i, j = get_current_position(lab_map)
    current_direction = 'up'
    visited = set([(i, j)])
    while True:
        # step
        next_i = i
        next_j = j
        match current_direction:
            case 'up':
                next_i -= 1
            case 'down':
                next_i += 1
            case 'left':
                next_j -= 1
            case 'right':
                next_j += 1
        if next_i < 0 or next_i > len(lab_map) - 1 or next_j < 0 or next_j > len(lab_map) - 1:
            return len(visited)
        if lab_map[next_i][next_j] == '#':
            current_direction = get_rotation(current_direction)
        else:
            i = next_i
            j = next_j
            visited.add((next_i, next_j))

def has_loop(lab_map, start_position):
    i, j = start_position
    current_direction = 'up'
    visited = set([(i, j, 'up')])
    while True:
        # step
        next_i = i
        next_j = j
        match current_direction:
            case 'up':
                next_i -= 1
            case 'down':
                next_i += 1
            case 'left':
                next_j -= 1
            case 'right':
                next_j += 1
        if next_i < 0 or next_i > len(lab_map) - 1 or next_j < 0 or next_j > len(lab_map) - 1:
            return False
        elif (next_i, next_j, current_direction) in visited:
            return True
        if lab_map[next_i][next_j] == '#':
            current_direction = get_rotation(current_direction)
        else:
            i = next_i
            j = next_j
            visited.add((i, j, current_direction))
            
def part_two():
    with open('day6/input.txt') as f:
        lab_map = f.readlines()
    start = get_current_position(lab_map)
    count = 0
    for i in range(0, len(lab_map)):
        for j in range(0, len(lab_map[i])):
            if lab_map[i][j] == '.':
                patched_map = lab_map[:]
                line = list(patched_map[i])
                line[j] = '#'
                patched_map[i] = ''.join(line)
                if has_loop(patched_map, start):
                    count += 1
    return count


if __name__ == '__main__':
    print(part_one())
    print(part_two())
        
        
    