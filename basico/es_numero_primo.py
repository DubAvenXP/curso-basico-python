def es_primo(numero):
    contador = 1

    if numero == 1 or numero == 0:
        return False

    for i in range(2, numero + 1):
        if numero % i == 0:
            contador += 1

    if contador == 2:
        return False
    else:
        return True


def es_primo_v2(numero):
    factorial = 1

    for i in range(1, numero):
        factorial = factorial * i

    print(f'El factorial de {numero} es {factorial}')
    if (factorial + 1) % numero == 0:
        return True
    else:
        return False


def run():
    numero = int(input('Ingrese un número: '))
    if es_primo_v2(numero):
        print(f'{numero} es primo')
    else:
        print(f'{numero} no es primo')


if __name__ == '__main__':
    run()