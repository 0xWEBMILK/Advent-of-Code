import re

def part1(file_path: str) -> int:
    result = 0

    with open(file_path, 'r') as file:
        for i in re.findall(r'mul\(\d+,\d+\)', file.read()):
            x, y = i[4:-1].split(',')
            result += int(x) * int(y)

    return result
def part2(file_path: str) -> int:
    result = 0
    status = True

    with open(file_path, 'r') as file:
        for i in re.findall(r"mul\(\d{0,999},\d{0,999}\)|do\(\)|don't\(\)", file.read()):
            if i == "do()":
                status = True
            elif i == "don't()":
                status = False
            else:
                if status:
                    x, y = i[4:-1].split(',')
                    result += int(x) * int(y)

    return result

if __name__ == "__main__":
    part1('./input.txt')
    part2('./input.txt')