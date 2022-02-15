def palindrome(string):
    try:
        if string == '':
            raise ValueError('Empty string')
        return string.replace(' ', '').lower() == string[::-1].replace(' ', '').lower()
    except Exception as e:
    # except AttributeError or TypeError:
        print(e)
        return False
    finally:
        # no es muy usual pero puede darse para cerrar 
        # archivos, conexiones a BBDD o liberar recursos
        print('Finally')


def run():
    print(palindrome(''))


if __name__ == '__main__':
    run()