"""
Este script contiene el código de una especie de puzzle.
La intención con los comentarios del código, es hacer que se entienda cada método, y sobre todo, como se crean los objetos
que se muestra en pantalla  y el porqué.
"""

"""
Esta clase Base contiene los atributos y métodos que se usan en todas las clases derivadas. Además, contiene métodos sencillos
que se encargar de mostrar los valores de los atributos.
 """
class Base:
    # Constructor de la clase
    def __init__(self):
        self.a = "a"  
        self.b = "b" 
        self.c = "c"  

    # Este método imprime el valor del atributo a
    def A (self):
        print(self.a)
    
    # Este método imprime el valor del atributo b
    def B(self): 
        print(self.b) 
 
    # Este método imprime el valor del atributo c
    def C(self): 
        print(self.c) 
 
"""
Esta nueva clase "Derivada", hereda de la clase Base. De esta forma, se juega con la asignación de valores a estos atributos.
Por tanto, en función de la instancia que se cree, se llamarán, a los atributos de una clase u otra, pudiendo tener distintos
valores.
"""
class Derivada(Base): 
    def __init__(self): 
        # Constructor de la clase Derivada
        self.a = "aa"  # Cambio del valor del atributo 'a' a "aa"
        super().__init__()  # Llamada al constructor de la clase Base para inicializar los atributos de esta
        self.c = "cc"  # Cambio del valor del atributo 'c' a "cc"

    """
    Es importante darse cuenta, que al llamar al constructor de la clase Base con el super().__init__(), se están reinicializando
    todos los atributos de la clase Base. Al hacerse después de asignarle el valor aa, al atributo a. El valor del atributo a se
    sobreescribirá por a trás llamar al super init. En cambio esto no afecta a c, ya que se reasigna un valor a c (cc en este caso)
    depués de haber inicializado a los atributos de la clase Base, por tanto tenga el valor que tenga c, su nuevo valor será cc.
    """
    def A(self): 
        # Método que imprime el valor del atributo a
        print(self.a) 

    # Este método cambia el valor del atributo b, y además imprime su valor (bb) dos veces
    def B(self): 
        self.b = "bb" 
        super().B() 
        print(self.b) 
 
# Creación de los objetos, con los atributos de la clase base, y la clase derivada respectivamente
base = Base() 
derivada = Derivada() 
 
# Llamadas a los métodos de las instancias
base.A()  # Imprime el valor de a según se haya asignado en la clase base (en este caso, su valor es a)
derivada.A()  # Imprime el valor de a asignado en la clase Derivada (en este caso, nuevamente a)
print() # Imprime un espacio 
base.B()  # Imprime el valor de b
derivada.B()  # Imprime bb dos veces
base.C()  # Imprime c
derivada.C()  # Imprime cc
derivada = base  # Se asigna la instancia base a la variable derivada
derivada.C()  # Imprime c