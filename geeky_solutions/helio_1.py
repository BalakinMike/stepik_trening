n, m = int(input()), 1
a = [[ 0 for j in range(n)] for i in range(n)]

s1 = 0
s2 = 2
s3 = -1
while m:
    for j in range(s1,n-s1):#верх
        a[s1][j] = m
        m +=1
        if m > n**2:
            break
    if m > n**2:
            break        
    for i in range(s1+1,n-s1):#право
        a[i][n-(s1+1)] = m
        m +=1
        if m > n**2:
            break
    if m > n**2:
        break        

    for j in range(n-s2,s3,-1):#низ
        a[n-(s1+1)][j] = m
        m +=1
        if m > n**2:
            break
    if m > n**2:
        break
    for i in range(n-s2,s3+1,-1):#лево
        a[i][s1] = m
        m +=1
        if m > n**2:
            break
    if m > n**2:
        break
    s1 +=1
    s2 +=1
    s3 +=1

for i in range (n):
    print(*a[i])