n, m = int(input()), int(input())
day = 0
ch = m
while n > 0:
    n  -=1
    day +=1
    if day == ch:
        n +=1
        ch +=m
    print(day,n,m)
print(day)

#Альтернатива :)
print((lambda n, m: (m * n - 1) // (m - 1))(*map(int, input().split())))