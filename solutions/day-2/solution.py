def part1(file_path: str) -> int:
    with open(file_path, 'r') as file:
        data = [map(int, line.split()) for line in file]
        result = len(data)

        for level in data:
            level = list(level)
            sorted_level = sorted(level)

            if level == sorted_level or level == sorted_level[::-1]:
                for i in range(1, len(level)):
                    calc = abs(level[i] - level[i-1])

                    if calc > 3 or calc == 0:
                        result -= 1
                        break
            else:
                result -= 1

    return result

def part2(file_path: str) -> int:
    with open(file_path, 'r') as file:
        data = [map(int, line.split()) for line in file]
        result = len(data)

        for level in data:
            level = list(level)
            sorted_level = sorted(level)

            if level == sorted_level or level == sorted_level[::-1]:
                for i in range(1, len(level)):
                    calc = abs(level[i] - level[i-1])

                    if calc > 3 or calc == 0:
                        result -= 1
                        break
                        

    return result


if __name__ == "__main__":
    print(part2('./input.txt'))