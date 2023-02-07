import time
def space_1 (text_1: str) -> int:
    n = 0
    for i in text_1:
        if i == ' ':
            n +=1
    return n

def space_2 (text_1: str) -> int:
    n = 0
    if text_1 == '':
        return n
    if text_1[0] == ' ':
        n +=1
    return n + space_2(text_1[1:])

def space_3 (text_1: str, n = 0) -> int:
    if text_1 =='':
        return n
    i = 0
    if text_1[0] == ' ':
        i +=1
    return space_3 (text_1[1:], n+i)

    

text_1 = input()

start_time = time.perf_counter()
print(space_1(text_1))
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")

start_time = time.perf_counter()
print(space_2(text_1))
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")

start_time = time.perf_counter()
print(space_3(text_1))
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")