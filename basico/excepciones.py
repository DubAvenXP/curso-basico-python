def divide_elementos_de_lista(lista, divisor):
    try:
        return [elemento / divisor for elemento in lista]
    except ZeroDivisionError as e:
        return lista
    


lista = list(range(1, 11))
divisor = 2

print(divide_elementos_de_lista(lista, divisor))