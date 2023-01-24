print(*range(1, int(input()) + 1), sep = '\n')
[print(i) for i in range(1, int(input()) + 1)]
print(*[i for i in range(1, int(input()) + 1)], sep = '\n')
print('\n'.join(map(str, [i for i in range(1, int(input()) + 1)])))