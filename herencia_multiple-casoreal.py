"""
Este script, contiene un código, donde se aplican los conceptos de la herencia (explicados en el ejercicio
de herencia multiple-diamante). Las distintas clases de este código, heredan unas de otras, para poder utilizar
los atributos de una clase, en las clases que la hereden.
"""

"""
La clase Pared, contiene un constructor, donde se inician los atributos, un método que se encarga
de añadir ventanas a la lista, y un último método que calcula la superficie total acristalada de la
pared sumando las superficies de todas sus ventanas y devuelve el resultado.     
"""
class Pared:
    # El constructor, contiene los atributos necesarios para crear la pared
    def __init__(self, orientacion):
        self.orientacion = orientacion
        self.ventanas = []

    def agregar_ventana(self, ventana):
        self.ventanas.append(ventana)

    def superficie_acristalada(self):
        return sum(ventana.superficie for ventana in self.ventanas)

"""
La Clase ParedCortina, hereda de la clase Pared, es por tanto una subclase de Pared. Esta clase 
contiene un constructor, donde se inicializan los atributos de su propia clase, y además inicia 
además de la orientación (llamando al constructor de la clase Pared). El otro método de la clase,
devuelve la superficie de la pared cortina
"""
class ParedCortina(Pared):
    def __init__(self, orientacion, superficie):
        super().__init__(orientacion)
        self.superficie_cortina = superficie

    def superficie_acristalada(self):
        return self.superficie_cortina

"""
La clase Ventana solo contiene el método constructor, donde se inician los atributos necesarios para
construir la ventana (pared, superficie, protección). Además, se impone que haya protección en la ventana
con una excepción, donde si detecta que no hay protección, lanza un mensaje para evitar el error. Por 
último, añade la ventana a la lista de ventanas de la pared.

"""
class Ventana:
    def __init__(self, pared, superficie, proteccion):
        if proteccion is None:
            raise Exception("Protección obligatoria")
        self.pared = pared
        self.superficie = superficie
        self.proteccion = proteccion
        pared.agregar_ventana(self)

"""

"""
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
