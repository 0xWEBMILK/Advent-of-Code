def main(file_path: str) -> int:
    left = []
    right = []

    with open(file_path, 'r') as file:
        for line in file:
            numbers = line.split()
            
            left.append(int(numbers[0]))
            right.append(int(numbers[1]))

    left = sorted(left)
    right = sorted(right)

    return sum([abs(right[i] - left[i]) for i in range(len(left))])


if __name__ == "__main__":
    main('./input.txt')