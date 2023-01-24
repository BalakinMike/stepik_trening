#В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Побеждает спортсмен, у которого максимален наилучший бросок. 
# Если таких несколько, то из них побеждает тот, у которого наилучшая сумма результатов по всем попыткам. 
# Если и таких несколько, победителем считается спортсмен с минимальным номером. Определите номер победителя соревнований.

#My solution
n, m = map(int,input().split())
a = [list(map(int, input().split())) for i in range(n)]
s_max, i_max, a_max = [], [], 0
for i in range(n):
    i_max.append(max(a[i]))
    s_max.append(sum(a[i]))
a_max = i_max.index(max(i_max))    
for i in range(n):
    if i_max[i] == max(i_max) and i != i_max.index(max(i_max)):
        if s_max[i] > s_max[a_max]:
            a_max = i
print(a_max)

#Alternative solution

#Получилось так: сначала создается список b, элементами которого тоже являются списки: максимальное число в строке и сумма всех чисел в строке. 
# При расчете функции max(b) сначала сравниваются числа в строке, если они равны, то суммы. 
# А index(max(b)) находит первое вхождение данного элемента
a = []
b = []
n, m = map(int, input().split())
for i in range(n):
  a.append(list(map(int, input().split())))
for i in range(n):
  b.append([max(a[i]), sum(a[i])])

print(b.index(max(b)))