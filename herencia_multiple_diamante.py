"""
En este script, se tiene un codigo aparentemente sencillo, pero que al haber tantas herencias, puede resultar una tarea difícil,
saber como se asignan los distintos valores a los atributos en cada clase.
"""

"""
Esta es la clase A, cuyo método constructor, inicializa la variable a
"""
class A:
    def __init__(self, a):
        self.a = a

"""
Esta es la clase B que herda de la clase A. El constructor de la clase B se encarga de iniciar la variable b, y se llama al constructor 
de la clase A para inicializar sus atributos en esta clase también.
"""
class B(A):
    def __init__(self, b):
        super().__init__(b) 
        self.b = b

"""
Esta es la clase C que hereda de la clase A. En el constructor de la clase C, se inicia la variable c y se llama al constructor de la clase A
para, al igual que en la clase B, inicializar los atributos de la clase A, en esta clase C.
"""
class C(A):
    def __init__(self, c):
        super().__init__(c)
        self.c = c
""" 
Es imortante destacar el hecho de que tanto en la clase B como en la clase C, ya que ambas heredan de A, se pasa como argumento al llamar al
constructor de la clase A, los parámetros b y c, respectivamente. Esto es, debido a que cuando se llama al super().__init__(b), se está
llamando al constructor de la clase A y pasándole b como el valor para inicializar su atributo a. Esto asegura que el atributo a de la clase A 
se inicialice correctamente con el valor de b. Ocurre lo mismo en la clase C, con su parámetro c.
"""

"""
En esta última clase D que hereda de las clases B y C (que estas a su vez heredan de la clase A), se están inicializando en el constructor,
las variables a b y c. 
Primero con el  super().__init__(b), se inician los atributos de la clase B. 
Después C.__init__(self, c) llama directamente al constructor de la clase C con el parámetro c, que inicializa el atributo c de la clase C. 
De esta forma se llama al constructor específico de la clase C, en lugar de utilizar el super().
Por último se inicia el atributo a de la clase D, cuyo valor asignado es a
"""
class D(B, C):

    def __init__(self, a, b, c):
        super().__init__(b)  
        C.__init__(self, c)  
        self.a = a  

# Se crea el obejeto d, con los valores de los distintos atributos propuestos
d = D(1, 2, 3)

# Se comprueban las instancias/objetos y los valores de los atributos (muestra el booleano True)
print(isinstance(d, A), isinstance(d, B), isinstance(d, C))
# Muesra los valores de los atributos del objeto d
print(d.a, d.b, d.c)    