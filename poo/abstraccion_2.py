
class Desayuno:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes

    def desayunar(self):
        print("Ingredientes seleccionados:")
        for key, value in self.ingredientes.items():
            print(f'{key} - {value}')
        print('')
        self._preparar_ingredientes()
        self._limpiar_ingredientes()
        self._cociar_ingredientes()
        self._servir_desayuno()
        self._limpiar_desayuno()

    def _preparar_ingredientes(self):
        print('Preparando los ingredientes')

    def _limpiar_ingredientes(self):
        print('Limpiando los ingredientes')

    def _cociar_ingredientes(self):
        print('Cociando los ingredientes')

    def _servir_desayuno(self):
        print('Serviendo el desayuno')

    def _limpiar_desayuno(self):
        print('Limpiando el desayuno')


def run():
    ingredientes = {
        'alimentos': ['pan', 'huevos', 'carne', 'frijoles'],
        'bebidas': ['agua', 'leche', 'jugo'],
        'otros': ['aceite', 'sal']
    }
    desayuno = Desayuno(ingredientes)
    desayuno.desayunar()


if __name__ == '__main__':
    run()