nombre = 'alejandro          '
nombre = nombre.capitalize()
nombre = nombre.strip() # quita espacios en blanco parecido a trim()
nombre = nombre.lower()
nombre = nombre.replace('a', 'o')
nombre = nombre[::-1] # invertir cadena
nombre = nombre[0]
nombre = nombre[-1]
len(nombre) # longitud de la cadena

# Slice

nombre_izquierda = nombre[:5]
nombre_derecha = nombre[-5:]
nombre_centro = nombre[5:6]
vocales = nombre[1:8:2] # salta de 2 en 2
consonantes = nombre[1::2] # salta de 2 en 2 