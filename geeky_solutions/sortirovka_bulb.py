a = [34, 23, 12, 28, 23]
flag = 0
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            flag +=1
            a.insert(j+1,a.pop(j))
    if flag == 0:
        break
print(a)