def run():
    my_dictionary = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    reto = {i: i**0.5 for i in range(1, 101)}
    print(reto)

if __name__ == '__main__':
    run()