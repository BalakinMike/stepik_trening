#Check right location of breckets
s = list(input())
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

#Alternative solution
s = input()
while '()' in s:
    s = s.replace('()', '')
print('NO' if s else 'YES')

#from Alex Glozman
stack = ['-']
for c in input():
    if c == '(':
        stack.append(c)
    elif (stack.pop() + c) != '()':
        print('NO')
        break
else:
    print(('NO', 'YES')[stack[-1] == '-']) 