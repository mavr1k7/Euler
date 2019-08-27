from decimal import Decimal, getcontext

def check_repeat(n, s, i, j, x):
    if n == '':
        return
    if len(n) < 800:
        return "Too small"
    if j >= len(n) - s or x > 4:
        if x > 0: 
            return s
        else:
            return None
    # print("Test: size - " + str(s) + ", i - " + str(i) + ", j - " + str(j) + ", x - " + str(x))
    # print("A - " + n[i:i+s])
    # print("B - " + n[j:j+s])
    if n[i:i+s] == n[j:j+s]:
        i += s
        j += s
        x += 1
        return check_repeat(n, s, i, j, x)
    else:
        return "Repeat"

max = 0
dec = 5000
pos = 0
start = 0
solution = 1
getcontext().prec = dec
for i in range(1, 1001):
    print("Testing 1/" + str(i))
    val = Decimal(1) / Decimal(i)

    for j in range(0, dec):
        s = 0
        rep = "Repeat"
        while rep == "Repeat":
            s += 1
            rep = check_repeat(str(val)[2:-1], s, j, j + s, 0)
            if s >= len(str(val)) - 3:
                break
        if rep is not None:
            pos = j
            break
    if rep is not None and type(rep) is not str and rep > max:
        max = rep
        start = pos
        solution = i
print("Max Length: " + str(max))
print("Start  Pos: " + str(start))
print("Solution d: " + str(solution))
# print("Decimal: " + str(Decimal(1) / Decimal(solution)))