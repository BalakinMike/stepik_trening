# My solution
def get_word_indices(strings) -> dict:
    'Функция возвращает словарь с местоположением вхождения слов'
    b_dict = {}
    b_list = set(i.lower() for j in strings for i in j.split())
    for k in b_list:
        b_dict[k] = [l for l in range(len(strings)) if k in strings[l].lower()]
            
    return b_dict

# Alternatieve solution with function setdefault and enumerate
def get_word_indices(strings: list[str]) -> dict:
    d = {}
    for i, k in enumerate(strings):
        for j in k.lower().split():
            d.setdefault(j, []).append(i)
    return d