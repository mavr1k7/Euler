total = 0
# paths = set()
def path(i, j, p, n):
    global total
    if i == n and j == n:
        # paths.add(p)
        total += 1
        # print(total)
        return
    if i != n:
        path(i + 1, j, p + "r", n)
    if j != n:
        path(i, j + 1, p + "d", n)
    return

n = 0
while(n != -1):
    n = int(input("Lattice size: "))
    path(0, 0, "", n)
    print("Solution: " + str(total))
    total = 0
    # print(paths)
    # print("Solution: " + str(len(paths)))
