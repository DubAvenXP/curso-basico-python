def ciclo_while():
    contador = 0
    while contador < 10:
        print(f"2 elevado a {contador} es {2 ** contador}")
        contador += 1

def ciclo_for():
    # for i in range(1, 10):
    for i in range(10):
        print(f"2 elevado a {i} es {2 ** i}")


def run():
    ciclo_for()


if __name__ == '__main__':
    run()