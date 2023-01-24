n, m = int(input()), 1
a = [[ 0 for j in range(n)] for i in range(n)]
# первый квадрат

s1 = 0
s2 = 2
s3 = -1
for j in range(s1,n-s1):#верх
    a[s1][j] = m
    m +=1

for i in range(s1+1,n-s1):#право
    a[i][n-(s1+1)] = m
    m +=1

for j in range(n-s2,s3,-1):#низ
    a[n-(s1+1)][j] = m
    m +=1

for i in range(n-s2,s3+1,-1):#лево
    a[i][s1] = m
    m +=1

# второй квадрат
s1 +=1
s2 +=1
s3 +=1
for j in range(s1,n-s1):
    a[s1][j] = m
    m +=1

for i in range(s1+1,n-s1):
    a[i][n-(s1+1)] = m
    m +=1

for j in range (n-s2,s3,-1):
    a[n-(s1+1)][j] = m
    m +=1

for i in range (n-s2,s3+1,-1):
    a[i][s1] = m
    m +=1

# третий квадрат
s1 +=1
for j in range (s1,n-s1):
    a[s1][j] = m
    m +=1

for i in range (n):
    print(*a[i])