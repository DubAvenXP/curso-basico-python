lista = ['alejandro', 'dubon']
nombre, apellido = lista

producto = {'nombre': 'Monitor 20 pulgadas', 'precio': 300}
nombre, precio = producto.items()
print(nombre, precio)
print(type(nombre))

name, price = producto.values()
print(name, price)
print(type(name))
