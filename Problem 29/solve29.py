distinct = set()
for a in range(2, 101):
    for b in range(2, 101):
        val = a**b
        distinct.add(val)
print(sorted(distinct))
print("Solution: " + str(len(distinct)))