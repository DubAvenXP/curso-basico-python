def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {
        "first_name": "John",
        "last_name": "Doe",
    }

    super_list = [{
        "first_name": "John",
        "last_name": "Doe",
    }, {
        "first_name": "Jane",
        "last_name": "Doe",
    }, {
        "first_name": "Jack",
        "last_name": "Doe",
    }, {
        "first_name": "Jill",
        "last_name": "Doe",
    }]

    super_dict = {
        "natural_number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "even_number": [2, 4, 6, 8, 10],
        "odd_number": [1, 3, 5, 7, 9],
        "prime_number": [2, 3, 5, 7],
        "square_number": [1, 4, 9, 16, 25],
        "floating_point_number": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    }

    # for key, value in super_dict.items():
    #     print(key, "-", value)

    # for element in super_list:
    #     for key, value in element.items():
    #         print(key, "-", value)

    numbers_list =  [ i**2 for i in range(1,11) ]
    print(numbers_list)


if __name__ == '__main__':
    run()