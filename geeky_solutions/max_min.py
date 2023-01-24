s1 = int(input())
s2 = int(input())
maximum = s1 if s1>s2 else s2
minimum = s2 if s1>s2 else s1
print(maximum, minimum)

# alternative solution
a, b = int(input()), int(input())
print(minimum := a if a < b else b, maximum := a if a > b else b)