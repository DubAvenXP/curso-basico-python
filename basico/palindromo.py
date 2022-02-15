def palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    if palabra == palabra[::-1]:
        return True
    else:
        return False


def run():
    palabra = input("Ingrese una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print("La palabra es un palindromo")
    else:
        print("La palabra no es un palindromo")


# entry point
if __name__ == '__main__':
    run()