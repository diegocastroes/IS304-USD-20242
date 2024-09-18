class Triangulo:
    def __init__(self, a, b, c):
        self.__a = a  # Atributo privado, encapsulamiento (lado a)
        self.__b = b  # Atributo privado, encapsulamiento (lado b)
        self.__c = c  # Atributo privado, encapsulamiento (lado c)

    def es_valido(self):
        # Verifica la desigualdad triangular
        return (self.__a + self.__b > self.__c and
                self.__a + self.__c > self.__b and
                self.__b + self.__c > self.__a)

    def clasificar(self):
        if not self.es_valido():
            return None  # No es un triángulo
        if self.__a == self.__b == self.__c:
            return "Equilátero"
        elif self.__a == self.__b or self.__b == self.__c or self.__c == self.__a:
            return "Isósceles"
        else:
            return "Escaleno"

    # Métodos para acceder a los lados (encapsulamiento)
    def get_a(self):
        return self.__a  # Permite acceder al lado a sin exponer el atributo directamente

    def get_b(self):
        return self.__b  # Permite acceder al lado b sin exponer el atributo directamente

    def get_c(self):
        return self.__c  # Permite acceder al lado c sin exponer el atributo directamente

class TrianguloRectangulo(Triangulo):  # Línea de herencia
    # Se utiliza la herencia para extender la funcionalidad de la clase Triangulo
    # Esto permite reutilizar métodos existentes (como clasificar y es_valido)
    def es_rectangulo(self):
        lados = sorted([self.get_a(), self.get_b(), self.get_c()])  # Usando métodos para acceder a atributos
        return lados[0]**2 + lados[1]**2 == lados[2]**2  # Verifica si es un triángulo rectángulo

def main():
    while True:
        try:
            a = float(input("Ingrese el primer lado: "))
            b = float(input("Ingrese el segundo lado: "))
            c = float(input("Ingrese el tercer lado: "))

            tri = TrianguloRectangulo(a, b, c)  # Se crea un objeto de TrianguloRectangulo
            tipo = tri.clasificar()  # Se clasifica el triángulo

            if tipo is None:
                print("Los valores ingresados no forman un triángulo. Fin del programa.")
                break  # Termina el programa si no es un triángulo

            print(f"Tipo de triángulo: {tipo}")

            if tri.es_rectangulo():
                print("Además, es un triángulo rectángulo.")

        except ValueError:
            print("Por favor, ingresa números válidos.")

if __name__ == "__main__":
    main()


