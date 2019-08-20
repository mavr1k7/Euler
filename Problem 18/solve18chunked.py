pyramid = [
    [75],
    [95,64],
    [17,47,82],
    [18,35,87,10],
    [20,4,82,47,65],
    [19,1,23,75,3,34],
    [88,2,77,73,7,63,67],
    [99,65,4,28,6,16,70,92],
    [41,41,26,56,83,40,80,70,33],
    [41,48,72,33,47,32,37,16,94,29],
    [53,71,44,65,25,43,91,52,97,51,14],
    [70,11,33,28,77,73,17,78,39,68,17,57],
    [91,71,52,38,17,14,91,43,58,50,27,29,48],
    [63,66,4,68,89,53,67,30,73,16,69,87,40,31],
    [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23],
]

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

row = 0
col = 0
chunk = 3
solution = 0
height = len(pyramid)
while chunk < height - 1:
    print(str(row) + "," + str(col))
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
print(result[1])

print("Solution: " + str(solution))