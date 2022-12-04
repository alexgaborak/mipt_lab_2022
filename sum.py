k = 0
for i in range(1000, 10000):
    s = 0
    n = i
    for j in range(1, 5):
        s+= n % 10
        n  = n // 10
    if s <10:
        k+=1

print(k)

