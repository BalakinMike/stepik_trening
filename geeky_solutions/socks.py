n = int(input())
def first_sym(n):
    while n // 10 != 0:
        n = n // 10
    return(n)
while (n !=1) or (n > 1000000000):
    n = n*first_sym(n)
print(n)
