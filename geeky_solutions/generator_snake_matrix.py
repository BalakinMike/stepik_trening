#My solution
n, m = map(int, input().split())
d = -1
def d_p():
    global d
    d +=1
    return d
a = [[ d_p() for j in range(m)] for i in range(n)]
for i in range(n):
    if i%2 !=0:
        a[i].reverse()
for i in range(n):
    print(*a[i])

#Alternative solution
n, m = map(int, input().split())

for i in range(n):
    if i % 2 == 0:
        print(*list(range(i * m, i * m + m)))
    else:
        print(*list(range(i * m, i * m + m))[::-1])