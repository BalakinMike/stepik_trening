def flatten_dict(nes: dict):
    rez = {}
    for key, value in nes.items():
        if type(value) == int:
            return nes
        else:
            for k, v in (flatten_dict(nes[key]).items()):
                rez[key +'_'+k] = v
 #           rez = rez|{key+'_'+i, j for key, value in flatten_dict(nes[key]).items()}
    return rez

nes = {'Geeks': {'for': {'for': 1, 'geeks': 4}}, 'for': {'geeks': {'Geeks': 3}}, 'geeks': {'Geeks': {'for': 7}}}

print(flatten_dict(nes))

# def f(nes: dict):
#     rez = {}
#     for key, value in nes.items():
#         if type(value) == int:
#             return nes
#         else:
#             rez[key +'_'+ list(f(nes[key]).keys())[0]] = list(f(nes[key]).values())[0]
#     return rez
# nes = {'washington': 1, 'New York': 4}

# print(f(nes))