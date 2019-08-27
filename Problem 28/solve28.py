sum = 1
start = 2
width = 1001
spiral = {1:1}
for i in range(3, width + 1, 2):
    end = (i-2)*4+4+start-1
    spiral[i] = start
    start = end+1
for key, val in spiral.items():
    if key == 1:
        continue
    x = val - 1
    for i in range(4):
        x = x + key - 1
        sum += x
    #     print(x)
    # print()
print("Solution: " + str(sum))