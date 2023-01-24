#На вход программе поступает список из целых чисел. Ваша задача найти в данном списке наименьшее положительное значение. 
# В случае, если положительных значений нет, выведите строку "Empty"

n_list = list(map(int, input().split(' ')))
mi = []
for i in n_list:
    if i > 0:
        mi.append(i)
if len(mi):
    print(min(mi))
else:
    print('Empty')


#Alternative solution
print((sorted([i for i in map(int, input().split()) if i > 0]) + ['Empty'])[0])