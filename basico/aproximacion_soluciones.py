from time import time


def main():
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    tiempo_inicio = time()

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    tiempo_final = time() - tiempo_inicio
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {objetivo}')
        print(f'El tiempo de ejecucion fue de {tiempo_final}')
    else:
        print(f'la raiz cuadrada de {objetivo} es {respuesta}')
        print(f'El tiempo de ejecucion fue de {tiempo_final}')

if __name__ == '__main__':
    main()