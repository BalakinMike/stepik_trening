# My solution
s = list(map(int, input().split()))
a = {s[-2]:s[-1]}
print(a)
for i in range (len(s)-2,0,-1):
    a={s[i]:a}
print (a)

# Alternative solution from Glozman with recursion function
def nested_dict(lst):
    return {lst[0]: nested_dict(lst[1:])} if len(lst) > 2 else dict([lst])

lst = list(map(int, input().split()))    
print(nested_dict(lst))    