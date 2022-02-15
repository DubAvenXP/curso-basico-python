def for_continue():
    for contador in range(100):
        if contador % 2 != 0:
            continue
        print(contador)

def for_break():
    for i in range(100):
        if i % 5 == 0:
            break
        print(i)

def while_continue():
    contador = 0
    while contador < 10:
        if contador % 2 != 0:
            contador += 1
            continue
        print(contador)
        contador += 1

def while_break():
    contador = 1
    while contador < 10:
        if contador % 7 == 0:
            print(f'{contador} es divisible en 7')
            contador += 1
            break
        print(contador)
        contador += 1


def run():
    print("Running")
    while_break()

if __name__ == '__main__':
    run()