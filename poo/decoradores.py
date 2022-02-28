

# def funcion_decoradora(funcion):
# 	def wrapper():
# 		print("Este es el último mensaje...")
# 		funcion()
# 		print("Este es el primer mensaje ;)")
# 	return wrapper

# def zumbido():
# 	print("Buzzzzzz")

# zumbido = funcion_decoradora(zumbido)


def chispas_de_chocolate(func):
	def wrapper():
		func()
		print("Añadiendo chispas de chocolate")
	return wrapper


def chispas_de_colores(func):
    def wrapper():
        func()
        print("Añadiendo chispas de colores")
    return wrapper

@chispas_de_chocolate
def helado():
	print("helado de vainilla")


def run():
    helado()


if __name__ == '__main__':
    run()