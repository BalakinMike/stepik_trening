def my_range_gen(*args):
    if len (args) == 1:
        start = 0
        step = 1
        stop = args[0]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif len (args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        return
    if step == 0 or (stop - start)%step != 0 or (stop - start)*step < 0:
        return
    k = start
    while abs(k) != abs(stop):
        yield  k
        k = k + step
    pass
for i in my_range_gen(4,8,0):
    print(i)
#tests = [(5,), (10,), (-5, 10), (30, 300, 1), (0, -10, -2), (0, -10, 5), (20, 10, 3), (1, 10, -2), (4, 8, 2), (8, 5, -1), (100, 300, 13), (10, 30, 3)]
