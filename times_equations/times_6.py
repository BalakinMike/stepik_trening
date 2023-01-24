import time
d = -1
def brecket(n,m):
    
    
    def d_p():
        global d
        d +=1
        return d
    a = [[ d_p() for j in range(m)] for i in range(n)]
    for i in range(n):
        if i%2 !=0:
            a[i].reverse()
    for i in range(n):
        print(*a[i])

def brecket_2(N,M):
    
    for n in range(N):
        line = [i for i in range(n * M, (n + 1) * M)][::(-1) ** n]
        print(*line)


start_time = time.perf_counter()
brecket(10,10)
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")


start_time = time.perf_counter()
brecket_2(10,10)
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")