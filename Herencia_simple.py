"""
Este script contiene un código sencillo donde se realiza una sola herencia, para crear un punto en 3d, en base a un punto
en 2d (iniciando la tercera coordenada en la subclase).
"""

"""
Esta clase, contiene un constructor donde se inicializan los atributos (coordenadas) necesarias para construir un punto en 2d.
El método traslación que se encarga de sumar la cantidad que se deben desplazar los puntos en el eje x y en el eje y (dx y dy
representan la cantidad que se debe desplazar el punto en ambos ejes. Después actualiza las coordenadas del punto sumando dx + x
y dy + y. Por último, el método str devuelve los valores de las coordenadas del punto.
"""
class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def traslacion(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return "X: {}; Y: {}".format(self.x, self.y)

"""
Esta clase, genera puntos en 3D. para ello, hereda de la clase anterior que es la que genera los puntos en 2D, de esta forma, 
se pueden reinicializar las coordenadas x e y en el constructor (llamando al constructor de la clase padre), además de la nueva 
coordenada z. Esta clase, realiza lo mismo que en la anterior, solo que esta vez, en translación, se añade la translación de z
(la de x e y, se hace previamente en la clse padre, y se hereda en esta subclase para no tener que repetir el proceso).
Por último, el método str devuelve la coordenada del punto con la nueva coordenada (en 3D).
"""
class Punto3D(Punto2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def traslacion(self, dx, dy, dz):
        super().traslacion(dx, dy)
        self.z += dz

    def __str__(self):
        return "X: {}; Y: {}; Z: {}".format(self.x, self.y, self.z)


# Se crean los objetos (puntos en 2D y 3D en este caso)
def main():
    a = Punto2D(1, 2)
    print("A = {}".format(a))
    a.traslacion(-1, -2)
    print("A = {}".format(a))

    b = Punto2D(-3, 0)
    b.traslacion(5, -1)
    print("B = {}".format(b))

    c = Punto3D(1, 5, -3)
    c.traslacion(0, -2, 1)
    print("C = {}".format(c))

# Se llama a la función en este script (si se importa el código a otro archivo, los objetos no se crearan en este nuevo archivo)
if __name__  == "__main__":
    main()