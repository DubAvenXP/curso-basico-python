def palindrome(word):
    assert len(word) > 0, 'The word must have at least one character'
    word = word.replace(' ', '').lower()
    return word == word[::-1]


def sumar():
    num = input('Ingresa un numero: ')
    assert num.isnumeric() and int(num) > 0, 'Debes ingresar un numero postivo'

    return num

def run():
    # word = input('Ingresa una palabra: ')
    # print(f'La palabra {word} es palindromo: {palindrome(word)}')
    print(sumar())


if __name__ == '__main__':
    run()