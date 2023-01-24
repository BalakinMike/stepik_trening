import time
def brecket(n,a):
    
    a,n = map(int, input().split())
    flag = False
    m =[i for i in range(1, n+1) if n%i==0]
    for i in range(len(m)):
        if max(m) > a:
            m.pop()
            flag = True
    if flag:
        m.pop(0)
    print(len(m))


def brecket_2(n,a):
    
    fl = 0
    for i in range(len(a)):
        flag = 0
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                flag +=1
                a.insert(j+1,a.pop(j))
        fl +=flag
        if flag == 0:
            break
    print(*a)
    print(fl)


start_time = time.perf_counter()
brecket(7, [7,13,-18,10,-14,4,-6])
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")



start_time = time.perf_counter()
brecket_2(7, [7,13,-18,10,-14,4,-6])
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")