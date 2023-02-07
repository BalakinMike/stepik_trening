def flatten(spisok):
    '''Представьте, что у нас есть список целых чисел неограниченной вложенности. 
    То есть наш список может состоять из списков, внутри которых также могут быть списки. 
    Ваша задача превратить все это в линейный список при помощи функции flatten'''
    if type(spisok)==int:
        return [spisok]
    elif len(spisok)==1:
        return flatten(spisok[0])
    else:
        return flatten(spisok[0])+flatten(spisok[1:])

