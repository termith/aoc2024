def get_data():
    left = []
    right = []
    with open('day1/input.txt') as f:
        for line in f:
            ids = list(map(int, line.split()))
            left.append(ids[0])
            right.append(ids[1])
    return left, right

def part_one():
    left, right = get_data()
    left.sort()
    right.sort()
    result = 0
    for (l, r) in zip(left, right):
        result += abs(l-r)
    return result

def part_two():
    left, right = get_data()
    result = 0
    for el in left:
        c = right.count(el)
        result += c * el
    return result


if __name__ == '__main__':
    print(part_one())
    print(part_two())
