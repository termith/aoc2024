import re 

MUL_REGEX = re.compile(r'mul\((\d+),(\d+)\)')
DO_REGEX = re.compile(r'do\(\)')
DONT_REGEX = re.compile(r'don\'t\(\)')
ADVANCDED_MUL_REGEX = re.compile(r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))')
        
def part_one():
    result = 0
    with open('day3/input.txt') as f:
        memory = f.read()
    for mul in re.finditer(MUL_REGEX, memory):
        result += int(mul.group(1)) * int(mul.group(2))
    return result

def part_two():
    result = 0
    active = True
    with open('day3/input.txt') as f:
        memory = f.read()
    for match in re.finditer(ADVANCDED_MUL_REGEX, memory):
        if match.group(4) is not None:
            active = False
        elif match.group(3) is not None:
            active = True
        elif active:
            result += int(match.group(1)) * int(match.group(2))
    return result

if __name__ == '__main__':
    print(part_one())
    print(part_two())