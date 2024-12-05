from collections import defaultdict

def get_data():
    rules = defaultdict(set)
    manuals = []
    with open('day5/input.txt') as f:
        while True:
            if (line := f.readline()) != '\n':
                first, second = tuple(map(int, line.split('|')))
                rules[first].add(second)
            else:
                break
        while (line := f.readline()):
            manuals.append(list(map(int, line.split(','))))
    return rules, manuals

def check_manual(manual, rules):
    for i in range(0, len(manual) - 1):
        if set(manual[i+1:]) - rules[manual[i]]:
            return False
    return True

def fix_manual(manual, rules):
    fixed_manual = []
    manual_copy = manual[:]
    for _ in range(0, len(manual)):
        for idx, page in enumerate(manual_copy):
            # Для каждой позиции ищем число, пересечение правил которого с остальным списком даёт 0
            if not set(manual_copy[0:idx] + manual_copy[idx+1:]) - rules[page]:
            # Это число записываем на текущую позицию и удаляем из исходного мануала
                fixed_manual.append(page)
                manual_copy.pop(idx)
                break
    return fixed_manual

def part_one():
    result = 0
    rules, manuals = get_data()
    for manual in manuals:
        if check_manual(manual, rules):
            result += manual[(len(manual) - 1)//2]
    return result

def part_two():
    result = 0
    rules, manuals = get_data()
    for manual in manuals:
        if not check_manual(manual, rules):
            fixed_manual = fix_manual(manual, rules)
            result += fixed_manual[(len(manual) - 1)//2]
    return result

if __name__ == '__main__':
    print(part_one())
    print(part_two())