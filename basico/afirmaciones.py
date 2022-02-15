def primera_letra(lista_de_palabras):
    primeras_letras = []
    try:
        for palabra in lista_de_palabras:
            assert type(palabra) == str, f'{palabra} no es str'
            assert len(palabra) > 0, f'No se permiten str vacios'
            primeras_letras.append(palabra[0])
        return primeras_letras
    except AssertionError as e:
        print(e)
        return primeras_letras


def main():
    lista_de_palabras = [1, 'mundo', 'como', 'estas']
    print(primera_letra(lista_de_palabras))


if __name__ == '__main__':
    main()