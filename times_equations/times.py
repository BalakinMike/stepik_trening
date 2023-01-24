import time
def brecket(bl = str):
    s = list(bl)
    sum = 0
    if s[0] == ')' or s[-1] == '(' or len(s)%2 != 0: # if first brecket ) or last brecket ( or quality brecket - odd
        print('NO')
    else:
        for i in range(int(len(s)/2)):
            if s[i] == '(':
                sum +=1
            else:
                sum +=-1
        if sum < 0:
            print('NO')
        else:
            for j in range(int(len(s)/2), len(s)):
                if s[j] == '(':
                    sum +=1
                else:
                    sum +=-1
        if sum == 0:
            print('YES')
        else:
            print('NO')

def brecket_1(bl):
    s = bl
    while '()' in s:
        s = s.replace('()', '')
    print('NO' if s else 'YES')

def brecket_2(bl):
    stack = ['-']
    for c in bl:
        if c == '(':
            stack.append(c)
        elif (stack.pop() + c) != '()':
            print('NO')
            break
    else:
        print(('NO', 'YES')[stack[-1] == '-'])


start_time = time.perf_counter()
brecket('()()')
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")

start_time = time.perf_counter()
brecket_1('()()')
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")

start_time = time.perf_counter()
brecket_2('()()')
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")