# My solution: don't work in case 'z,0'
def shift_letter(letter: str, shift: int) -> str:
    'Функция сдвигает символ letter на shift позиций'
    alf = ['a','b','c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_index = alf.index(letter) + shift
    while new_index > 26:
        new_index = new_index-26
    return alf[new_index]
# Working solution
def shift_letter(b: str, s: int) -> str:
    '''Функция сдвигает символ letter на shift позиций'''
    return chr((ord(b) - 97 + s) % 26 + 97)

def caesar_cipher(s: str, n: int) -> str:
    'Шифр цезаря'
    new_s = ''
    for i in s:
        if i.isalpha():
            i_n = shift_letter(i, n)
            new_s += i_n
        else:
            new_s += i
    return new_s
