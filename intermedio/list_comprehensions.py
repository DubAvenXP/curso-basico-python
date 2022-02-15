def run():
    # list comprehension
    # output expression - input sequence - codition
    my_list = [i**2 for i in range(1,101) if i % 3 != 0]
    reto = [i for i in range(1, 99999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(reto)


if __name__ == '__main__':
    run()