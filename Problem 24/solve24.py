perms = set()

def swap(i, s):
    s = ''.join((s[:i-1], s[i], s[i:i], s[i-1], s[i+1:]))
    pre = len(perms)
    perms.add(s)
    post = len(perms)
    if post > pre:
        return len(s) - 1, s
    else:
        s = ''.join((s[:i-1], s[i], s[i:i], s[i-1], s[i+1:]))
        return i - 1, s

def perm(n):
    index = n
    next = "0123456789"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "1234567890"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "2345678901"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "3456789012"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "4567890123"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "5678901234"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "6789012345"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "7890123456"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "8901234567"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "9012345678"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
        index = n
    next = "9876543210"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "8765432109"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "7654321098"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "6543210987"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "5432109876"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "4321098765"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "3210987654"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "2109876543"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "1098765432"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]
    index = n
    next = "0987654321"
    while(index != 0):
        ret = swap(index, next)
        index = ret[0]
        next = ret[1]

perm(9)
print(sorted(perms))
print(len(perms))
i = 1
for x in sorted(perms):
    if i == 999999:
        print("Solution A: " + x)
        break
    elif i == 1000000:
        print("Solution B: " + x)
        break
    elif i == 1000001:
        print("Solution C: " + x)
        break
    i += 1