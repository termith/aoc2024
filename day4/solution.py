def part_one():
    with open('day4/input.txt') as f:
        data = f.readlines()
    i = 0
    result = 0
    while i < len(data):
        j = 0
        while j < len(data[i]):
            if data[i][j] == 'X':
                # right
                if j + 3 < len(data[i]) and data[i][j:j+4] == 'XMAS':
                    result += 1
                # left
                if j - 3 > -1 and data[i][j-3:j+1] == 'SAMX':
                    result += 1
                # up
                if i - 3 > -1:
                    string = data[i][j] + data[i-1][j] + data[i-2][j] + data[i-3][j]
                    if string == 'XMAS':
                        result += 1 
                    # up - left
                    if j - 3 > -1:
                        string = data[i][j] + data[i-1][j-1] + data[i-2][j-2] + data[i-3][j-3]
                        if string == 'XMAS':
                            result += 1
                    # up - right
                    if j + 3 < len(data[i]):
                       string = data[i][j] + data[i-1][j+1] + data[i-2][j+2] + data[i-3][j+3]
                       if string == 'XMAS':
                            result += 1
                # down
                if i + 3 < len(data):
                    string = data[i][j] + data[i+1][j] + data[i+2][j] + data[i+3][j]
                    if string == 'XMAS':
                        result += 1
                    # down - left
                    if j - 3 > -1:
                        string = data[i][j] + data[i+1][j-1] + data[i+2][j-2] + data[i+3][j-3]
                        if string == 'XMAS':
                            result += 1
                    # down - right
                    if j + 3 < len(data[i]):
                        string = data[i][j] + data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3]
                        if string == 'XMAS':
                            result += 1
            j += 1
        i += 1
    return result 

def part_two():
    with open('day4/input.txt') as f:
        data = f.readlines()
    i = 0
    result = 0
    while i < len(data):
        j = 0
        while j < len(data[i]):
            if data[i][j] == 'A':
                if (i - 1 > -1 and i + 1 < len(data)) and (j - 1 > -1 and j + 1 < len(data[i])):
                    left = data[i-1][j-1] + data[i][j] + data[i+1][j-1]
                    right = data[i-1][j+1] + data[i][j] + data[i+1][j+1]
                    up = data[i-1][j-1] + data[i][j] + data[i-1][j+1]
                    down = data[i+1][j-1] + data[i][j] + data[i+1][j+1]
                    if left == 'SAM' and right == 'SAM':
                        result += 1
                    elif left == 'MAS' and right == 'MAS':
                        result += 1
                    elif up == 'MAS' and down == 'MAS':
                        result += 1
                    elif up == 'SAM' and down == 'SAM':
                        result += 1
            j += 1
        i += 1
    return result 



if __name__ == '__main__':
    print(part_one())
    print(part_two())
    
    
    