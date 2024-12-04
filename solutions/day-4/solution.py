import sys

def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def matches(x, y, dx, dy):
        for k in range(word_length):
            nx, ny = x + k * dx, y + k * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
                return False
        return True

    count = 0

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if matches(i, j, dx, dy):
                    count += 1

    return count

def part1(file_path: str) -> int:
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]

    return count_word_occurrences(grid, "XMAS")

if __name__ == "__main__":
    file_path = sys.argv[1]
    print(part1(file_path))