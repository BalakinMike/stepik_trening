#На вход программе поступает строка, состоящая из нескольких слов, знаком разделителем между словами будем считать символ пробела. 
# Ваша задача исключить из строки дублирующие слова: первое появление слова остается в строке, второе и все последующие появления исключаются. 
# При сравнении на дубли строк регистр букв не учитывать, это значит слова python и PyThOn считаются одинаковыми.

s = input()
s_s = list(s.split(' '))
s_l = list(s.lower().split(' '))
print(s_s)

count = []
final = []
for i in range(len(s_l)):
    if s_l[i] not in final:
        final.append(s_l[i])
    else:    
        count.append(i)
count.reverse()
for i in count:
    s_s.pop(i)
print(*s_s, sep = ' ')

#Alternative solution

s = set()
for i in input().split():
    if i.lower() not in s:
        s.add(i.lower())
        print(i, end=' ')  