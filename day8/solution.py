from collections import defaultdict

def get_map():
    a_map = defaultdict(list)
    with open('day8/input.txt') as f:
        raw_data = f.readlines()
    for i in range(0, len(raw_data)):
        for j in range(0, len(raw_data[i])):
            if (point := raw_data[i][j]) not in ['\n', '.']:
                a_map[point].append((j, i))  # x, y
    return a_map, raw_data


def part_one():
    antinodes = set()
    a_map, raw_data = get_map()
    max_x = len(raw_data[0].strip())
    max_y = len(raw_data)
    for a in a_map.values():
        i = 0
        while i != len(a):
            j = i + 1
            while j != len(a):
                x_1, y_1 = a[i]
                x_2, y_2 = a[j]
                dx = x_2 - x_1
                dy = y_2 - y_1

                a_x_1 = x_2 + dx
                a_y_1 = y_2 + dy

                if a_x_1 > -1 and a_x_1 < max_x and a_y_1 > -1 and a_y_1 < max_y:
                    antinodes.add((a_x_1, a_y_1))

                a_x_2 = x_1 - dx
                a_y_2 = y_1 - dy

                if a_x_2 > -1 and a_x_2 < max_x and a_y_2 > -1 and a_y_2 < max_y:
                    antinodes.add((a_x_2, a_y_2))

                j += 1
            i += 1

    return len(antinodes)

def part_two():
    antinodes = set()
    a_map, raw_data = get_map()
    max_x = len(raw_data[0].strip())
    max_y = len(raw_data)
    for a in a_map.values():
        i = 0
        while i != len(a):
            antinodes.add(a[i])
            j = i + 1
            while j != len(a):
                x_1, y_1 = a[i]
                x_2, y_2 = a[j]
                dx = x_2 - x_1
                dy = y_2 - y_1

                while (-1 < (a_x := x_2 + dx) < max_x) and (-1 < (a_y := y_2 + dy) < max_y):
                    antinodes.add((a_x, a_y))
                    x_2 = a_x
                    y_2 = a_y
                
                while (-1 < (a_x := x_1 - dx) < max_x) and (-1 < (a_y := y_1 - dy) < max_y):
                    antinodes.add((a_x, a_y))
                    x_1 = a_x
                    y_1 = a_y  

                j += 1
            i += 1

    return len(antinodes)

if __name__ == '__main__':
    print(part_one())
    print(part_two())