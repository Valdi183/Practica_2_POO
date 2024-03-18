class Pared:
    # Inicializa una Pared con una orientación dada y una lista vacía para las ventanas
    def __init__(self, orientacion):
        self.orientacion = orientacion
        self.ventanas = []

    def agregar_ventana(self, ventana):
        self.ventanas.append(ventana)

    # Calcula la superficie total acristalada de la pared sumando las superficies de todas sus ventanas
    def superficie_acristalada(self):
        return sum(ventana.superficie for ventana in self.ventanas)


class ParedCortina(Pared):
    # Inicializa una ParedCortina con una orientación y una superficie total, heredando de Pared
    def __init__(self, orientacion, superficie):
        super().__init__(orientacion)
        self.superficie_cortina = superficie

    # Devuelve la superficie acristalada total de la pared cortina
    def superficie_acristalada(self):
        return self.superficie_cortina


class Ventana:
    # Inicializa una Ventana asignándola a una pared, con una superficie dada y una protección. Si no hay protección, lanza una excepción
    def __init__(self, pared, superficie, proteccion):
        if proteccion is None:
            raise Exception("Protección obligatoria")
        self.pared = pared
        self.superficie = superficie
        self.proteccion = proteccion
        pared.agregar_ventana(self)


class Casa:
    # Inicializa una Casa con una lista de paredes.
    def __init__(self, paredes):
        self.paredes = paredes

    # Calcula y devuelve la superficie acristalada total de la casa sumando las superficies acristaladas de todas sus paredes
    def superficie_acristalada(self):
        return sum(pared.superficie_acristalada() for pared in self.paredes)


def main():
    # Instanciación de las paredes
    pared_norte = Pared("NORTE")
    pared_oeste = Pared("OESTE")
    pared_sur = Pared("SUR")
    pared_este = Pared("ESTE")

    # Instanciación de las ventanas con protección
    ventana_norte = Ventana(pared_norte, 0.5, "Persiana") # ¡IMPORTANTE! Para comprobar que se cumple la exception, sustituir el valor de protección por "None"
    ventana_oeste = Ventana(pared_oeste, 1, "Persiana")
    ventana_sur = Ventana(pared_sur, 2, "Estor")
    ventana_este = Ventana(pared_este, 1, "Estor")

    # Instanciación de la casa con las 4 paredes
    casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
    print("Superficie acristalada inicial:", casa.superficie_acristalada())

    # Reemplazo de una pared por una pared cortina
    casa.paredes[2] = ParedCortina("SUR", 10)
    print("Superficie acristalada final:", casa.superficie_acristalada())

if __name__ == "__main__":
    main()
