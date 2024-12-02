def part1(file_path: str) -> int:
    with open(file_path, 'r') as file:
        pairs = (map(int, line.split()) for line in file)
        a, b = zip(*pairs)

    left = sorted(a)
    right = sorted(b)

    return sum([abs(left[i] - right[i]) for i in range(len(left))])

def part2(file_path: str) -> int:
    with open(file_path, 'r') as file:
        for line in file:
            pairs = (map(int, line.split()) for line in file)

            a, b = zip(*pairs)

    left = sorted(a)
    right = sorted(b)

    return sum([left[i] * right.count(left[i]) for i in range(len(left))])


if __name__ == "__main__":
    part1('./input.txt')
    part2('./input.txt')