from    Figuras.Circulo import Circulo
from    Figuras.Cuadrado import Cuadrado
from    Figuras.Rectangulo import Rectangulo

def main():
    circulo = Circulo(radio = 5)
    cuadrado = Cuadrado(lado = 5)
    rectangulo = Rectangulo(base = 5, altura = 10)

    print("Circulo: Area = ", circulo.area(), " Perimetro = ", circulo.perimetro())
    print("Cuadrado: Area = ", cuadrado.area(), " Perimetro = ", cuadrado.perimetro())
    print("Rectangulo: Area = ", rectangulo.area(), " Perimetro = ", rectangulo.perimetro())

if __name__ == '__main__':
    main()