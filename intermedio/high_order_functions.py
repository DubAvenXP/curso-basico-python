from functools import reduce


def run():
    numbers = list(range(1, 21))
    odd = list(filter(lambda x: x % 2 != 0, numbers))

    # squares = [i**2 for i in range(1,6) ]
    my_list = list(range(1, 6))
    squares = list(map(lambda x: x**2, my_list))

    my_other_list = [2, 2, 2, 2, 2]
    all_multiplied = reduce(lambda x, y: x * y, my_other_list)
    print(all_multiplied)


if __name__ == "__main__":
    run()