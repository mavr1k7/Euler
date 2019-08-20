# Parse triangle file
pyramid = []
lines = [line.rstrip('\n') for line in open('triangle.txt', 'r')]
for i, line in enumerate(lines):
    pyramid.append([])
    line = line.split(' ')
    for num in line:
        pyramid[i].append(int(num))

def sum(total, path, row, col, chunk):
    total += pyramid[row][col]
    path += str(row) + "," + str(col) + "\n"
    if row == chunk:
        return total, path
    a = sum(total, path, row + 1, col, chunk)
    b = sum(total, path, row + 1, col + 1, chunk)
    if a > b:
        return a
    else:
        return b

def loop(i):
    row = 0
    col = 0
    chunk = i
    solution = 0
    height = len(pyramid)
    while chunk < height - 1:
        # print(str(row) + "," + str(col))
        result = sum(0, "", row, col, chunk)
        val = result[1].split('\n')[0].split(',')
        row = int(val[0])
        col = int(val[1])
        solution += pyramid[row][col]
        next = result[1].split('\n')[1].split(',')
        row = int(next[0])
        col = int(next[1])
        chunk += 1

    result = sum(0, "", row, col, len(pyramid) - 1)
    solution += result[0]
    # print(result[1])

    print("Solution: " + str(solution))

i = 2
while i < 21:
    loop(i)
    i += 1