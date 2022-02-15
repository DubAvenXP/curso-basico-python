def run():
    persona = {
        'nombre': 'Juan',
        'apellido': 'Perez',
        'edad': 20,
    }
    print(persona)
    print(persona.get('nombre'))
    print(persona['apellido'])
    
    # for key in persona.keys():
    #     print(f'{key} : {persona[key]}')
    for key, value in persona.items():
        print(f'{key} : {value}')

if __name__ == '__main__':
    run()

# .keys() —> Retorna la clave de nuestro elemento
# .values()—> Retorna una lista de elementos (valores del diccionario)
# .items() —> Devuelve lista de tuplas (primero la clave y luego el valor)
# .clear() —> Elimina todos los items del diccionario
# .pop(“n”) —> Elimina el elemento ingresado
# .get('term', false) —> Retorna el valor del elemento ingresado, si no existe retorna false
# del diccionario['item'] —> Elimina el elemento ingresado
# nombre in diccionario —> Retorna true si el elemento existe en el diccionario