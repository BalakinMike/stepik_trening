def shift_letter(letter: str, shift: int) -> str:
    'Функция сдвигает символ letter на shift позиций'
    alf = ['a','b','c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_index = alf.index(letter) + shift
    while new_index > 26:
        new_index = new_index-26
    return alf[new_index]

shift_letter(letter: str, shift: int)