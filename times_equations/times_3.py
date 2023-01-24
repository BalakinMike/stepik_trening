import time
def brecket(bl):
    n = bl
    count = 0
    for i in range (n+1,n*2):
        if i%2 != 0:
            for j in range(3, i+1, 2):
                if i%j == 0: 
                    if j != i:
                        break
                    else:
                        count +=1
    print(count)
# def brecket_1(bl):
#     s = bl
#     while '()' in s:
#         s = s.replace('()', '')
#     print('NO' if s else 'YES')

def brecket_2(bl):
    r, n = 0, bl
    for i in range(n + 1, 2 * n):
        r += (0, 1)[len([j for j in range(2, int(i ** 0.5) + 1) if i % j == 0]) == 0]
    print(r)


start_time = time.perf_counter()
brecket(50000)
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")

# start_time = time.perf_counter()
# brecket_1('()()')
# end_time = time.perf_counter()
# print(f"The execution time: {end_time - start_time:.8f} seconds")

start_time = time.perf_counter()
brecket_2(50000)
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")