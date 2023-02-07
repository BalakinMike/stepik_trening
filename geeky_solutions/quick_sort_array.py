def f(a):
    if len (a) <= 1:
        return a
    o1 = [a[len(a)//2]]
    o_b = []
    o_l = []
    
    for i in range (len(a)//2):
        if a[i] > o1[0]:
            o_b.append(a[i])
        else:
            o_l.append(a[i])
    
    for i in range ((len(a)//2)+1,len(a)):
        if a[i] > o1[0]:
            o_b.append(a[i])
        else:
            o_l.append(a[i])
    
    a = f(o_l) + o1 + f(o_b)
    return (a)

a = [12, 13, 13, 1, 13, 3, 19, 8, 4]
print(f(a))