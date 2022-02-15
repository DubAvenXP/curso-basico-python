import random


MAYUS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z')
MINUS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
NUMS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
CHARS = ('*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#')


def generar_contrasena(largo = 8):
    """
        Genera una contraseña de un largo especificado

        largo int cualquier entero mayor a 8
        
        returns password str
    """
    caracteress = MAYUS + MINUS + NUMS + CHARS
    constrasena = []
    for i in range(largo):
        constrasena.append(random.choice(caracteress))
    return ''.join(constrasena)


def run():
    contrasena = generar_contrasena(9)
    print(f'La contraseña generada es: {contrasena}')


if __name__ == '__main__':
    run()