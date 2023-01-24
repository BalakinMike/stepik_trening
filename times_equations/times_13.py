s = list(map(int, input().split()))
a = {s[-2]:s[-1]}
print(a)
for i in range (len(s)-2,0,-1):
    a={s[i]:a}
print (a)

