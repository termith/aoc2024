import itertools

def get_data():
    data = []
    with open('day7/input.txt') as f:
        for line in f:
            result, values = line.split(': ')
            data.append((int(result),list(map(int, values.split()))))
    return data

def apply_operators_to_values(order, values):
    i = 0
    result = values[0]
    for i in range(len(order)):
        if order[i] == '+':
            result += values[i + 1]
        elif order[i] == '*':
            result *= values[i + 1]
        elif order[i] == '&':
            result = int(str(result)+str(values[i+1]))
    return result

def check_equal(test, values, operators):
    for order in itertools.product(operators, repeat=len(values) - 1):
        result = apply_operators_to_values(order, values)
        if result == test:
            return True
    return False

def part_one():
    result = 0
    data = get_data()
    for test, values in data:
        if check_equal(test, values, ('+','*')):
            result += test
    return result

def part_two():
    result = 0
    data = get_data()
    for test, values in data:
        if check_equal(test, values, ('+','*', '&')):
            result += test
    return result


if __name__ == '__main__':
    print(part_one())
    print(part_two())
