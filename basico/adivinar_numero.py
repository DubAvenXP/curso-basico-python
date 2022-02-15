import random

def adivinar_numero():
    numero_aleatorio = random.randint(1, 100)
    while True:
        numero_elegido = int(input("Elige un número del 1 al 100: "))
        if numero_elegido == numero_aleatorio:
            print("¡Has acertado!")
            break
        else:
            if numero_elegido < numero_aleatorio:
                print("Busca un número más grande")
            else:
                print("Busca un número más pequeño")

def run():
    adivinar_numero()    

if __name__ == '__main__':
    run()