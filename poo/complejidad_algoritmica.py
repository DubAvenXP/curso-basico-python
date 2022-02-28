import time
import sys


def factorial(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado


def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial_r(n - 1)


if __name__ == '__main__':
    # print(sys.getrecursionlimit())
    # sys.setrecursionlimit(1000)

    n = 800
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(f'Tiempo de ejecucion factorial: {final - comienzo}')

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(f'Tiempo de ejecucion factorial recursivo: {final - comienzo}')