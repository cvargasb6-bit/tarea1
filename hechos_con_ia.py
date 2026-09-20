# soluciones de los ejercicios de clases

# ---------- 1. Persona ----------
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print("Hola, me llamo " + self.nombre + " y tengo " + str(self.edad) + " años")

p1 = Persona("Carlos", 20)
p1.presentarse()


# ---------- 2. Perro ----------
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(self.nombre + " dice: Guau!")

perro1 = Perro("Firulais", "criollo")
perro1.ladrar()


# ---------- 3. Rectangulo ----------
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

r = Rectangulo(5, 3)
print("Area:", r.area())
print("Perimetro:", r.perimetro())


# ---------- 4. Circulo ----------
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio * self.radio

c = Circulo(4)
print("Area del circulo:", c.area())


# ---------- 5. Cuenta bancaria ----------
class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo = self.saldo + monto
        print("Deposito hecho. Saldo:", self.saldo)

    def retirar(self, monto):
        if monto > self.saldo:
            print("No tienes saldo suficiente")
        else:
            self.saldo = self.saldo - monto
            print("Retiro hecho. Saldo:", self.saldo)

cuenta1 = Cuenta("Ana", 100)
cuenta1.depositar(50)
cuenta1.retirar(30)
cuenta1.retirar(500)


# ---------- 6. Estudiante ----------
class Estudiante:
    def __init__(self, nombre, nota1, nota2, nota3):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    def aprobo(self):
        if self.promedio() >= 7:
            print(self.nombre + " aprobó")
        else:
            print(self.nombre + " reprobó")

e1 = Estudiante("Luis", 8, 6, 9)
print("Promedio:", e1.promedio())
e1.aprobo()


# ---------- 7. Contador ----------
class Contador:
    def __init__(self):
        self.valor = 0

    def sumar(self):
        self.valor += 1

    def restar(self):
        self.valor -= 1

    def mostrar(self):
        print("El contador va en:", self.valor)

cont = Contador()
cont.sumar()
cont.sumar()
cont.sumar()
cont.restar()
cont.mostrar()


# ---------- 8. Libro ----------
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_info(self):
        print("Titulo:", self.titulo)
        print("Autor:", self.autor)
        print("Paginas:", self.paginas)

libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", 471)
libro1.mostrar_info()


# ---------- 9. Carro ----------
class Carro:
    def __init__(self, marca):
        self.marca = marca
        self.velocidad = 0

    def acelerar(self):
        self.velocidad = self.velocidad + 10
        print("Velocidad:", self.velocidad)

    def frenar(self):
        self.velocidad = self.velocidad - 10
        if self.velocidad < 0:
            self.velocidad = 0
        print("Velocidad:", self.velocidad)

carro1 = Carro("Chevrolet")
carro1.acelerar()
carro1.acelerar()
carro1.frenar()
carro1.frenar()
carro1.frenar()


# ---------- 10. Calculadora ----------
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            print("No se puede dividir entre 0")
            return None
        return a / b

calc = Calculadora()
print(calc.sumar(4, 2))
print(calc.restar(4, 2))
print(calc.multiplicar(4, 2))
print(calc.dividir(4, 2))
print(calc.dividir(4, 0))


# ---------- 11. Producto ----------
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * porcentaje / 100
        return self.precio - descuento

prod1 = Producto("Zapatos", 40)
print("Precio con descuento:", prod1.aplicar_descuento(10))


# ---------- 12. Empleado ----------
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def dar_aumento(self, porcentaje):
        self.salario = self.salario + (self.salario * porcentaje / 100)
        print("Nuevo salario de " + self.nombre + ":", self.salario)

emp1 = Empleado("Pedro", 500)
emp1.dar_aumento(10)


# ---------- 13. Temperatura ----------
class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def a_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def a_kelvin(self):
        return self.celsius + 273.15

temp = Temperatura(30)
print("Fahrenheit:", temp.a_fahrenheit())
print("Kelvin:", temp.a_kelvin())


# ---------- 14. Lista de compras ----------
class ListaCompras:
    def __init__(self):
        self.items = []

    def agregar(self, item):
        self.items.append(item)

    def quitar(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Ese item no esta en la lista")

    def mostrar(self):
        print("Lista de compras:")
        for item in self.items:
            print("-", item)

lista = ListaCompras()
lista.agregar("arroz")
lista.agregar("leche")
lista.agregar("huevos")
lista.quitar("leche")
lista.quitar("pan")
lista.mostrar()


# ---------- 15. Jugador ----------
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
            print(self.nombre + " tiene " + str(self.vida) + " de vida")

j1 = Jugador("Zeta")
j1.recibir_dano(40)
j1.recibir_dano(70)


# ---------- 16. Lampara ----------
class Lampara:
    def __init__(self):
        self.encendida = False

    def encender(self):
        self.encendida = True

    def apagar(self):
        self.encendida = False

    def estado(self):
        if self.encendida:
            print("La lampara esta encendida")
        else:
            print("La lampara esta apagada")

lamp = Lampara()
lamp.estado()
lamp.encender()
lamp.estado()
lamp.apagar()
lamp.estado()


# ---------- 17. Animal y Gato ----------
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("El animal hace un sonido")

class Gato(Animal):
    def hacer_sonido(self):
        print(self.nombre + " dice: Miau")

animal1 = Animal("Animal generico")
animal1.hacer_sonido()
gato1 = Gato("Michi")
gato1.hacer_sonido()


# ---------- 18. Persona y Profesor ----------
# uso otra clase para no pisar la del ejercicio 1
class Persona2:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Profesor(Persona2):
    def __init__(self, nombre, edad, materia):
        Persona2.__init__(self, nombre, edad)
        self.materia = materia

    def mostrar(self):
        print(self.nombre + ", " + str(self.edad) + " años, da " + self.materia)

prof = Profesor("Marcela", 35, "Matematicas")
prof.mostrar()


# ---------- 19. Mascota con __str__ ----------
class Mascota:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def __str__(self):
        return self.nombre + " (" + self.tipo + ")"

m = Mascota("Firulais", "perro")
print(m)


# ---------- 20. Tienda ----------
class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def total(self):
        suma = 0
        for p in self.productos:
            suma = suma + p.precio
        return suma

tienda = Tienda()
tienda.agregar_producto(Producto("Camisa", 15))
tienda.agregar_producto(Producto("Pantalon", 25))
tienda.agregar_producto(Producto("Gorra", 8))
print("Total de la tienda:", tienda.total())
