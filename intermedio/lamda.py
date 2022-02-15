def run():
    # saludo = lambda nombre: "Hola {}".format(nombre)
    saludo = lambda nombre: f"Hola {nombre}"
    print(saludo("Juan"))


if __name__ == "__main__":
    run()