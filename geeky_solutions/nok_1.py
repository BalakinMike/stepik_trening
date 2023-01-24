a,b = map(int, input().split(' '))
m = a*b
if a <b:
    a,b = b,a
while b > 0:
    a,b = b, a%b
print(int(m/a))