#Summa diagonal elements
n, a, sum = int(input()), [], 0
for i in range(n):
    a.append(list(map(int, input().split(' '))))
    sum += a[i][i]
print(sum) 

# Output overwrite matrix
n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        print(a[j][i], end=" ")
    print()

#rectangle matrix overwrite
n,m = map(int, input().split(' '))
a = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(m-1, -1, -1):
        print(a[i][j], end=" ")
    print()