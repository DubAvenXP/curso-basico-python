EUROS_DOLARES = 1.15
QUETZALES_DOLARES = 7.5
YENES_DOLARES = 115.28

menu = """
Bievenido al conversor de monedas

1. Convertir euros a dolares
2. Convertir quetzales a dolares
3. Convertir yenes a dolares

Elige una opción: """

def conversor(moneda, valor_conversion):
    cantidad = float(input(f"Ingrese la cantidad de {moneda}: "))
    if (moneda == 'euros'):
        dolares = round(cantidad * valor_conversion, 2)
    else:
        dolares = round(cantidad / valor_conversion, 2)
    print(f"{cantidad} {moneda} son {dolares} dolares")


opcion = input("Ingrese una opción: ")

if opcion == "1":
    conversor('euros', EUROS_DOLARES)
elif opcion == "2":
    conversor('quetzales', QUETZALES_DOLARES)
elif opcion == "3":
    conversor('yenes', YENES_DOLARES)
else:
    print("Moneda no válida")

