#Задана система уравнений:
#a^2+b = n; a+b^2 = m
#Нужно посчитать количество пар целых чисел (a, b) (0 ≤ a, b), которые удовлетворяют системе.

#My solution:
n,m = map(int, input().split(' '))
count = 0
for a in range(int(n**0.5)+1):
    for b in range (int(m**0.5)+1):
        if a**2 + b == n:
            if a + b**2 == m:
                count +=1
                print(a,b, count)

# Alex Glozman - analutic solution
n, m = map(int, input().split())
print(int(n > m ** 0.5))

#Alex Glozman solution with binary serch:
(n, m), cnt = map(int, input().split()), 0
if n > m ** 0.5:
    s, e = 0, m
    while e - s > 1:
        x = s + (e - s) // 2
        f1, f2 = n - x ** 2, (m - x) ** .5
        if f1  > f2:
            s = x
        elif f1 < f2:
            e = x
        else:
            cnt = 1
            break
    else:        
        cnt = int(n - e ** 2  == (m - e) ** .5)
print(cnt)   