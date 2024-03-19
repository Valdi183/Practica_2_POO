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
devuelve la superficie de la pared cortina.
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
La clase Casa, contiene un constructor, donde se inicia el atributo paredes. Además contiene también un método 
que almacena el total de superficies acristaladas, sumando las superficies acristaladas de cada pared.
"""
class Casa:
    # Inicializa una Casa con una lista de paredes.
    def __init__(self, paredes):
        self.paredes = paredes

    # Calcula y devuelve la superficie acristalada total de la casa sumando las superficies acristaladas de todas sus paredes
    def superficie_acristalada(self):
        return sum(pared.superficie_acristalada() for pared in self.paredes)

"""
La función main, es en la que se crean los distintos objetos en función de los atributos iniciados previamente en cada clase.
En el caso de las paredes, se crean 4 distintas para cada orientación. Después se crean las ventanas en función de la orientación
de la pared en la que se encuentran, la superficie de las ventanas (superficie acristalada en m^2) y por último la protección
de estas (persianas, estor) dode además, en una de las instancias se puede probar la excepcion con el None como protección.
Posteriormente, se crean las casas con las 4 paredes, y se muestra en pantalla la superficie acritalada (inicial). Ya por último,
se  modifica la casa, reemplazando una de las paredes (la que está orienmtada hacia el sur), por una pared cortina donde además,
cambia también la superficie acristalada. Al haberse modificado la pared (ahora es una pared cortina por tanto otro objeto), se 
hace un print para mostrar en pantalla la superficie acristalada total (final) tras haber modificado la pared.
"""
def main():
    # Se crean las paredes (objeto) en función de la orientación
    pared_norte = Pared("NORTE")
    pared_oeste = Pared("OESTE")
    pared_sur = Pared("SUR")
    pared_este = Pared("ESTE")

    # Se crean las ventanas (objeto) en función de la orientación de la pared
    ventana_norte = Ventana(pared_norte, 0.5, "Persiana")
  # ventana_norte = Ventana(pared_norte, 0.5, None) # Si se quitase el asterisco de esta instancia, se puede comprobar la excepción
    ventana_oeste = Ventana(pared_oeste, 1, "Persiana")
    ventana_sur = Ventana(pared_sur, 2, "Estor")
    ventana_este = Ventana(pared_este, 1, "Estor")

    # Instanciación de la casa (objeto) con las 4 paredes y la superficie acrsitalada
    casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
    print("Superficie acristalada inicial:", casa.superficie_acristalada())

    # Reemplazo de una pared por una pared cortina
    casa.paredes[2] = ParedCortina("SUR", 10)
    print("Superficie acristalada final:", casa.superficie_acristalada())

""" 
Para ejecutar la función main a la que denominaré función de creación de objetos, solo en estre script, se pone la condición que se
observa aquí abajo. De esta forma, los objetos se crearan solo si se ejecuta el código desde este archivo. Esto también nos permite
importar el código a otro archivo, para crear otros objetos con otros valores para los parametros.
"""
if __name__ == "__main__":
    main()
