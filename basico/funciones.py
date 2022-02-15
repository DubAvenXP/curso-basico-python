def imprimir_mensaje(mensaje):
    print('Mensaje especial: ')
    print(f'Mensaje especial = {mensaje}')

def mensaje_menu(opcion):
    print('Hola')
    print('Cómo estás')
    print(f'Elegiste la opción {opcion}')
    print('Adios')

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

opcion = int(input("Ingrese una opción  (1, 2, 3): "))
if opcion == 1:
    mensaje_menu(opcion)
if opcion == 2:
    mensaje_menu(opcion)
if opcion == 3:
    mensaje_menu(opcion)