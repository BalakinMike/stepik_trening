import time
def brecket(bl = str):
    s = bl
    if len(s) % 2 != 0:
        print('NO')
    else:
        for i in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        print('NO' if s else 'YES')

# def brecket_1(bl):
#     s = bl
#     while '()' in s:
#         s = s.replace('()', '')
#     print('NO' if s else 'YES')

def brecket_2(bl):
    s, match, stack = bl, {'[]', '{}', '()'}, ['-']
    if len(s) % 2 != 0:
        print('NO')
    else:    
        for c in s:
            if c in '[({':
                stack.append(c)
            elif (stack.pop() + c) not in match:
                print('NO')
                break
        else:
            print(('NO', 'YES')[stack[-1] == '-'])


start_time = time.perf_counter()
brecket('(((({{{{[[[[]]]]}}}})))))')
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")

# start_time = time.perf_counter()
# brecket_1('()()')
# end_time = time.perf_counter()
# print(f"The execution time: {end_time - start_time:.8f} seconds")

start_time = time.perf_counter()
brecket_2('(((({{{{[[[[]]]]}}}})))))')
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")