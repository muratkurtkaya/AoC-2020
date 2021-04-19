with open("puzzle.txt", "r") as f:
    data = f.read().splitlines()


def solver(inData, xSlope=3, ySlope=1):
    count = 0
    col = 0
    for row in range(0, len(inData), ySlope):
        # if there is a three +1 count
        if (inData[row][col] == "#"):
            count += 1
        col = (col + xSlope) % 31  # 3 Right
    return count


ans1 = solver(data)

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] #part 2
ans2 = 1
for slope in slopes:
    ans2 *= solver(data,slope[0],slope[1])
print(ans1, ans2)
