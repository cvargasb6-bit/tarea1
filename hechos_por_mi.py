#ejercicios de clases

#ejercicio 1
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola me llamo", self.nombre, "y tengo", self.edad, "años")

persona1 = Persona("Carlos", 20)
persona1.saludar()

#ejercicio 2
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print("Guau!")

perro1 = Perro("Max", "labrador")
print(perro1.nombre, perro1.raza)
perro1.ladrar()

#ejercicio 3
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        a = self.base * self.altura
        return a

    def perimetro(self):
        p = self.base * 2 + self.altura * 2
        return p

rect = Rectangulo(5, 3)
print("el area es", rect.area())
print("el perimetro es", rect.perimetro())

#ejercicio 4
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        pi = 3.1416
        resultado = pi * self.radio * self.radio
        return resultado

circ = Circulo(4)
print("area del circulo:", circ.area())

#ejercicio 5
class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo = self.saldo + monto
        print("nuevo saldo:", self.saldo)

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo = self.saldo - monto
            print("nuevo saldo:", self.saldo)
        else:
            print("no tienes suficiente plata")

cuenta1 = Cuenta("Ana", 100)
cuenta1.depositar(50)
cuenta1.retirar(30)
cuenta1.retirar(500)

#ejercicio 6
class Estudiante:
    def __init__(self, nombre, n1, n2, n3):
        self.nombre = nombre
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def promedio(self):
        suma = self.n1 + self.n2 + self.n3
        prom = suma / 3
        return prom

    def aprobo(self):
        if self.promedio() >= 7:
            print(self.nombre, "aprobo")
        else:
            print(self.nombre, "no aprobo")

est = Estudiante("Luis", 8, 6, 9)
print("promedio:", est.promedio())
est.aprobo()

#ejercicio 7
class Contador:
    def __init__(self):
        self.numero = 0

    def sumar(self):
        self.numero = self.numero + 1

    def restar(self):
        self.numero = self.numero - 1

    def mostrar(self):
        print("numero:", self.numero)

c = Contador()
c.sumar()
c.sumar()
c.sumar()
c.restar()
c.mostrar()

#ejercicio 8
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar(self):
        print("titulo:", self.titulo)
        print("autor:", self.autor)
        print("paginas:", self.paginas)

libro1 = Libro("El principito", "Antoine de Saint-Exupery", 96)
libro1.mostrar()

#ejercicio 9
class Carro:
    def __init__(self, marca):
        self.marca = marca
        self.velocidad = 0

    def acelerar(self):
        self.velocidad = self.velocidad + 10
        print("velocidad:", self.velocidad)

    def frenar(self):
        if self.velocidad > 0:
            self.velocidad = self.velocidad - 10
        print("velocidad:", self.velocidad)

carro1 = Carro("Chevrolet")
carro1.acelerar()
carro1.acelerar()
carro1.frenar()
carro1.frenar()
carro1.frenar()  #aqui ya no baja de 0

#ejercicio 10
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "no se puede dividir entre 0"
        else:
            return a / b

calc = Calculadora()
print(calc.sumar(10, 5))
print(calc.restar(10, 5))
print(calc.multiplicar(10, 5))
print(calc.dividir(10, 5))
print(calc.dividir(10, 0))

#ejercicio 11
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * porcentaje / 100
        nuevo = self.precio - descuento
        return nuevo

prod = Producto("Zapatos", 40)
print("precio con descuento:", prod.aplicar_descuento(10))

#ejercicio 12
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def dar_aumento(self, porcentaje):
        aumento = self.salario * porcentaje / 100
        self.salario = self.salario + aumento
        print("el salario de", self.nombre, "ahora es", self.salario)

emp = Empleado("Pedro", 500)
emp.dar_aumento(10)

#ejercicio 13
class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def fahrenheit(self):
        f = self.celsius * 9 / 5 + 32
        return f

    def kelvin(self):
        k = self.celsius + 273.15
        return k

temp = Temperatura(30)
print("fahrenheit:", temp.fahrenheit())
print("kelvin:", temp.kelvin())

#ejercicio 14
class ListaCompras:
    def __init__(self):
        self.lista = []

    def agregar(self, item):
        self.lista.append(item)

    def quitar(self, item):
        if item in self.lista:
            self.lista.remove(item)
        else:
            print("ese item no esta")

    def mostrar(self):
        for i in self.lista:
            print("-", i)

compras = ListaCompras()
compras.agregar("arroz")
compras.agregar("leche")
compras.agregar("huevos")
compras.quitar("leche")
compras.quitar("pan")
compras.mostrar()

#ejercicio 15
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100

    def recibir_dano(self, cantidad):
        self.vida = self.vida - cantidad
        if self.vida <= 0:
            self.vida = 0
            print("Game over")
        else:
            print("vida de", self.nombre, ":", self.vida)

jugador1 = Jugador("Zeta")
jugador1.recibir_dano(40)
jugador1.recibir_dano(70)

#ejercicio 16
class Lampara:
    def __init__(self):
        self.encendida = False

    def encender(self):
        self.encendida = True

    def apagar(self):
        self.encendida = False

    def estado(self):
        if self.encendida == True:
            print("esta encendida")
        else:
            print("esta apagada")

lampara = Lampara()
lampara.estado()
lampara.encender()
lampara.estado()
lampara.apagar()
lampara.estado()

#ejercicio 17
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("sonido de animal")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")

animal = Animal("animal")
animal.hacer_sonido()
gato = Gato("Michi")
print(gato.nombre)
gato.hacer_sonido()

#ejercicio 18
class Persona2:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Profesor(Persona2):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def mostrar(self):
        print(self.nombre, self.edad, self.materia)

profe = Profesor("Marcela", 35, "Matematicas")
profe.mostrar()

#ejercicio 19
class Mascota:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def __str__(self):
        return self.nombre + " (" + self.tipo + ")"

mascota = Mascota("Firulais", "perro")
print(mascota)

#ejercicio 20
class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def total(self):
        total = 0
        for p in self.productos:
            total = total + p.precio
        return total

tienda = Tienda()
tienda.agregar_producto(Producto("Camisa", 15))
tienda.agregar_producto(Producto("Pantalon", 25))
tienda.agregar_producto(Producto("Gorra", 8))
print("total:", tienda.total())
