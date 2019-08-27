p = 5
sum = 0
for i in range(0, 10):
    val = i**p
    if str(val) == str(i):
        print(val)
        sum += val
    for j in range(0, 10):
        val = i**p + j**p
        if str(val) == str(i)+str(j):
            print(val)
            sum += val
        for k in range(0, 10):
            val = i**p + j**p + k**p
            if str(val) == str(i)+str(j)+str(k):
                print(val)
                sum += val
            for l in range(0, 10):
                val = i**p + j**p + k**p + l**p
                if str(val) == str(i)+str(j)+str(k)+str(l):
                    print(val)
                    sum += val
                for m in range(0, 10):
                    val = i**p + j**p + k**p + l**p + m**p
                    if str(val) == str(i)+str(j)+str(k)+str(l)+str(m):
                        print(val)
                        sum += val
                    for n in range(0, 10):
                        val = i**p + j**p + k**p + l**p + m**p + n**p
                        if str(val) == str(i)+str(j)+str(k)+str(l)+str(m)+str(n):
                            print(val)
                            sum += val
                        for o in range(0, 10):
                            val = i**p + j**p + k**p + l**p + m**p + n**p + o**p
                            if str(val) == str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o):
                                print(val)
                                sum += val
print("Solution: " + str(sum))