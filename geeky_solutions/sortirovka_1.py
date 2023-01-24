n, m = map(int, input().split())
list_fin = []
list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))

while len(list_1) !=0 and len(list_2) !=0:
    if min(list_1) < min(list_2):
        list_fin.append(min(list_1))
        list_1.remove(min(list_1))
    elif min(list_2) < min(list_1):
        list_fin.append(min(list_2))
        list_2.remove(min(list_2))
    else:
        list_fin.append(min(list_1))
        list_1.remove(min(list_1))
        list_fin.append(min(list_2))
        list_2.remove(min(list_2))

for k in range(0,len(list_2)):
    list_fin.append(list_2[k])
for k in range(0,len(list_1)):
    list_fin.append(list_1[k])
print(*list_fin)

#alternative solution
n, m = map(int,input().split())
s = list(map(int,input().split())) + list(map(int,input().split()))
c = []
while len(s) > 0:
    c.append(min(s))
    s.remove(min(s))
print(*c)