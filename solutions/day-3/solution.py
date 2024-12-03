import re

def part1(file_path: str) -> int:
    operations = []
    result = []

    with open(file_path, 'r') as file:
        for line in file:
            operations.append(re.findall(r'mul\(\d{0,999},\d{0,999}\)', line))

    for i in operations:
        for j in i:
            result.append(int(j[4:-1].split(',')[0]) * int(j[4:-1].split(',')[1]))

    return sum(result)

def part2(file_path: str) -> int:
    operations = []
    result = []
    status = 1

    with open(file_path, 'r') as file:
        for line in file:
            operations.append(re.findall(r"mul\(\d{0,999},\d{0,999}\)|do\(\)|don't\(\)", line))

    for i in operations:
        for j in i:
            if j == 'do()':
                status = 1
            elif j == "don't()":
                status = 0
            else:
                if status == 1:
                    result.append(int(j[4:-1].split(',')[0]) * int(j[4:-1].split(',')[1]))

    return sum(result)

if __name__ == "__main__":
    print(part2('./input.txt'))