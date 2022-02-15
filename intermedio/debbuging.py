def divisors(num):
    try:
        if num < 1:
            raise ValueError("Number must be greater than 0")
        return [i for i in range(1, num + 1) if num % i == 0]
    except Exception as e:
        print(e)
        return []


def run():
    try:
        num = int(input('Ingresa un numero: '))
        print(divisors(num))
    except Exception as e:
        print(e)
        print('Debes ingresar un numero')


if __name__ == '__main__':
    run()