import time
def brecket(bl):
    s = bl
    s.lower()
    print(max([s.count(i) for i in s]))  


def brecket_2(bl):
    s = bl
    s.lower()
    a,r = [], 1
    for x in s: 
        if x not in a:
            a.append(x)
            r =max(r,s.count(x))
    print(r)


start_time = time.perf_counter()
brecket('sdfjhkjhewiuhлоыврацущгурдоатдйууйдардыовытдугрцдфлыыотарцгуарfmnscaskajhfkakfeuqhkjbnvdsm')
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")



start_time = time.perf_counter()
brecket_2('sdfjhkjhewiuhлоыврацущгурдоатдйууйдардыовытдугрцдфлыыотарцгуарfmnscaskajhfkakfeuqhkjbnvdsm')
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")