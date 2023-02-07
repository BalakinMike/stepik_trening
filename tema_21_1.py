def flatten_dict(nes: dict, rez = None):
    '''Имеется вложенный словарь, уровень вложенности произвольный и заранее неизвестен. 
    Ключами словаря на любом уровне могут быть только строки, значения - только числа.
    Задача состоит в том, чтобы преобразовать этот вложенный словарь в плоский 
    (состоящий только из одного уровня), где ключи формируются конкатенацией вложенных ключей,
     соединенных знаком _'''
    if rez == None:
        rez = {}
    for key,value in nes.items():
        if type(value) == int:
            rez[key] = value

    for key in rez:        
            nes.pop(key)
    
    for key, value in nes.items():
        if type(value) == int:
            return nes
        else:
            for k, v in (flatten_dict(nes[key]).items()):
                rez[key +'_'+k] = v
 
    return rez

nes = {"a": 1,"b": {"c": 2,"d": 3,"e": {"f": 4,'6': 100,'5': {"g": 6},"l": 1,}}}

print(flatten_dict(nes))

