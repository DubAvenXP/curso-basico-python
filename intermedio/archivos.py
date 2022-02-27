def read():
    numbers = []
    with open("intermedio/archivos/numbers.txt", 'r', encoding="utf-8") as file:
        for line in file:
            numbers.append(int(line))
        file.close()
    print(numbers)
        


def write():
    names = ["Juan", "Pedro", "María", "Ana"]
    with open("intermedio/archivos/names.txt", 'w', encoding="utf-8") as file:
        for name in names:
            file.write(f"{name}\n")
        file.close()


def run():
    write()


if __name__ == '__main__':
    run()