n, m = map(int, input().split(' '))
a,b = [],[]
mult = 1
while n != 1:
    for j in range (2,9):
        if n%j == 0:
            a.append(j)
            n = n/j
            break
	
while m != 1:
    for j in range (2,9):
        if m%j == 0:
            b.append(j)
            m = m/j
            break
for k in range(0,len(a)):
    for i in range(0,len(b)):
        if a[k] == b[i]:
            b.pop(i)
            break
a = a + b
for i in range(0,len(a)):
    mult = mult*a[i]
print(mult)






