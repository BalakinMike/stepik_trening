def gen_fibonacci_numbers(n):
    n1 = 0
    n2 = 1
    print(1)
    for j in range(2,n+1):
        n3 = (n2+n1)
        yield n3
        n1 = n2
        n2 = n3
        
for i in gen_fibonacci_numbers(10):
    print(i)




