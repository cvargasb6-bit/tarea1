# Ej1
class Calificador:
    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if nota >= 0 and nota <= 100:
            return True
        else:
            return False

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        total = 0
        for n in self.notas:
            total += n
        return total / len(self.notas)


# Ej2
class AnalizadorTexto:
    def __init__(self):
        self.unicas = set()
        self.orden = []

    def agregar_palabra(self, palabra):
        self.unicas.add(palabra)
        self.orden.append(palabra)

    def contar_palabras(self):
        return len(self.unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


# Ej3
class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        total = 0
        for nombre in self.articulos:
            total += self.articulos[nombre]
        return total

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []
        for nombre in self.articulos:
            precio = self.articulos[nombre]
            if precio >= precio_min and precio <= precio_max:
                resultado.append(nombre)
        return resultado


# Ej4
class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        i = len(lista) - 1
        while i >= 0:
            invertida.append(lista[i])
            i = i - 1
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            invertida = self.invertir_lista(lista)
            resultado[tuple(lista)] = invertida
        return resultado


# Ej5
class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        self.pares = []
        self.impares = []
        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)
        return {"pares": self.pares, "impares": self.impares}

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))


# Ej6
class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        menor = self.temperaturas[0]
        for t in self.temperaturas:
            if t < menor:
                menor = t
        return menor

    def maxima(self):
        mayor = self.temperaturas[0]
        for t in self.temperaturas:
            if t > mayor:
                mayor = t
        return mayor

    def promedio(self):
        total = 0
        for t in self.temperaturas:
            total += t
        return total / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)


# Ej7
class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        resultado = []
        for nombre in self.personas:
            if self.personas[nombre] >= edad_minima:
                resultado.append(nombre)
        return resultado

    def edad_promedio(self):
        total = 0
        for nombre in self.personas:
            total += self.personas[nombre]
        return total / len(self.personas)


# Ej8
class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor = None
        cantidad_mayor = -1
        for nombre in self.equipos:
            cantidad = len(self.equipos[nombre])
            if cantidad > cantidad_mayor:
                cantidad_mayor = cantidad
                mayor = nombre
        return mayor


# Ej9
class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        vocales = "aeiouAEIOU"
        if letra in vocales:
            return True
        else:
            return False

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        digitos_str = "0123456789"
        letras_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        vocales = 0
        consonantes = 0
        digitos = 0

        for c in texto:
            if self.solo_vocales(c):
                vocales += 1
            elif c in digitos_str:
                digitos += 1
            elif c in letras_str:
                consonantes += 1

        return {"vocales": vocales, "consonantes": consonantes, "digitos": digitos}


# Ej10
class Tareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        resultado = []
        for tarea in self.tareas:
            if tarea[1] == "alta":
                resultado.append(tarea)
        return resultado

    def eliminar_completada(self, descripcion):
        nueva_lista = []
        for tarea in self.tareas:
            if tarea[0] != descripcion:
                nueva_lista.append(tarea)
        self.tareas = nueva_lista


# Ej11
class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] = self.frecuencias[elemento] + 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        mayor = None
        frecuencia_mayor = -1
        for elemento in self.frecuencias:
            if self.frecuencias[elemento] > frecuencia_mayor:
                frecuencia_mayor = self.frecuencias[elemento]
                mayor = elemento
        return mayor

    def frecuencia_elemento(self, elemento):
        if elemento in self.frecuencias:
            return self.frecuencias[elemento]
        else:
            return 0


# Ej12
class SelectorRango:
    def crear_rango(self, inicio, fin):
        numeros = []
        numero = inicio
        while numero <= fin:
            numeros.append(numero)
            numero = numero + 1
        return tuple(numeros)

    def elementos_en_multiples_rangos(self, *rangos):
        conjunto = set()
        for rango in rangos:
            for numero in self.crear_rango(rango[0], rango[1]):
                conjunto.add(numero)

        lista = []
        for numero in conjunto:
            posicion = 0
            while posicion < len(lista) and lista[posicion] < numero:
                posicion = posicion + 1
            lista.insert(posicion, numero)
        return lista


# Ej13
class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        largo_mayor = len(lista1)
        if len(lista2) > largo_mayor:
            largo_mayor = len(lista2)
        i = 0
        while i < largo_mayor:
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
            i = i + 1
        return resultado

    def intercalar_multiples(self, *listas):
        if len(listas) == 0:
            return []
        resultado = listas[0]
        i = 1
        while i < len(listas):
            resultado = self.intercalar(resultado, listas[i])
            i = i + 1
        return resultado


# Ej14
class RegistroNotas:
    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        resultado = []
        for estudiante in self.notas:
            if self.notas[estudiante] >= nota_minima:
                resultado.append(estudiante)
        return resultado

    def mejor_estudiante(self):
        mejor_nombre = None
        mejor_nota = -1
        for estudiante in self.notas:
            nota = self.notas[estudiante]
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante
        return (mejor_nombre, mejor_nota)


# Ej15
class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []
        i = 1
        while i <= numero:
            if numero % i == 0:
                divisores.append(i)
            i = i + 1
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = 0
        for divisor in divisores:
            if divisor != numero:
                suma = suma + divisor
        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        return resultado


# Ej16
class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        minusculas = "abcdefghijklmnopqrstuvwxyz"
        mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if letra in minusculas:
            base = ord('a')
        elif letra in mayusculas:
            base = ord('A')
        else:
            return letra

        posicion = ord(letra) - base
        nueva_posicion = (posicion + desplazamiento) % 26
        return chr(base + nueva_posicion)

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            resultado = resultado + self.codificar_letra(letra, desplazamiento)
        self.historial[palabra] = resultado
        return resultado


# Ej17
class AgrupadorEdades:
    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.grupos = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            if categoria in self.grupos:
                self.grupos[categoria].append(edad)
            else:
                self.grupos[categoria] = [edad]
        return self.grupos

    def edad_promedio_categoria(self, categoria):
        if categoria not in self.grupos:
            return 0
        edades = self.grupos[categoria]
        total = 0
        for e in edades:
            total += e
        return total / len(edades)


# Ej18
class CalculadorDistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        self.distancias.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        punto_cercano = None
        distancia_menor = None
        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)
            if distancia_menor is None or distancia < distancia_menor:
                distancia_menor = distancia
                punto_cercano = punto
        return punto_cercano


# Ej19
class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] = self.stock[producto] + cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] = self.stock[producto] - cantidad
            return True
        else:
            return False

    def productos_bajo_stock(self, minimo):
        resultado = []
        for producto in self.stock:
            if self.stock[producto] < minimo:
                resultado.append(producto)
        return resultado


# Ej20
class AnalizadorPatrones:
    def __init__(self):
        self.todas_palabras = set()

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        resultado = []
        for palabra in palabras:
            self.todas_palabras.add(palabra)
            if palabra.startswith(patron):
                resultado.append(palabra)
        return resultado

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        resultado = {}
        for palabra in palabras:
            self.todas_palabras.add(palabra)
            longitud = len(palabra)
            if longitud in resultado:
                resultado[longitud].append(palabra)
            else:
                resultado[longitud] = [palabra]
        return resultado

    def palabras_unicas(self):
        return self.todas_palabras


if __name__ == "__main__":

    print("Ej1")
    c = Calificador()
    print(c.cargar_notas(85, 92, 110, 78, -5, 88))
    print(c.promedio())

    print("Ej2")
    at = AnalizadorTexto()
    at.agregar_multiples("hola", "mundo", "hola")
    print(at.contar_palabras())

    print("Ej3")
    cc = CarroCompras()
    cc.agregar_articulo("pan", 2.50)
    cc.agregar_articulo("leche", 3.00)
    print(cc.total_carrito())
    print(cc.articulos_por_rango(2, 3))

    print("Ej4")
    inv = InversorSecuencia()
    print(inv.invertir_lista([1, 2, 3]))
    print(inv.invertir_multiples([1, 2, 3], [4, 5, 6]))

    print("Ej5")
    an = AnalizadorNumeros()
    print(an.separar(1, 2, 3, 4, 5))
    print(an.cantidad_pares_impares())

    print("Ej6")
    gt = GestorTemperatura()
    gt.registrar_multiples(20, 25, 18, 30)
    print(gt.promedio())
    print(gt.minima(), gt.maxima())

    print("Ej7")
    gp = GestorPersonas()
    gp.agregar_persona("Ana", 28)
    gp.agregar_persona("Bob", 17)
    print(gp.personas_mayores(18))
    print(gp.edad_promedio())

    print("Ej8")
    eq = Equipos()
    eq.crear_equipo("A")
    eq.agregar_jugador("A", "Juan")
    eq.agregar_jugador("A", "Pedro")
    eq.crear_equipo("B")
    eq.agregar_jugador("B", "Luis")
    print(eq.equipo_mayor_integrantes())

    print("Ej9")
    astr = AnalizadorString()
    print(astr.contar_por_tipo("Hola123"))

    print("Ej10")
    t = Tareas()
    t.agregar_tarea("Estudiar", "alta")
    t.agregar_tarea("Leer", "baja")
    print(t.tareas_prioritarias())
    t.eliminar_completada("Leer")
    print(t.tareas)

    print("Ej11")
    cf = ContadorFrecuencia()
    cf.agregar_elemento("a")
    cf.agregar_elemento("b")
    cf.agregar_elemento("a")
    print(cf.elemento_mas_frecuente())
    print(cf.frecuencia_elemento("a"))

    print("Ej12")
    sr = SelectorRango()
    print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))

    print("Ej13")
    cl = CombinadorListas()
    print(cl.intercalar([1, 2], [3, 4]))

    print("Ej14")
    rn = RegistroNotas()
    rn.registrar("Ana", 95)
    rn.registrar("Bob", 70)
    print(rn.mejor_estudiante())

    print("Ej15")
    df = DivisorFinder()
    print(df.encontrar_divisores(12))
    print(df.es_perfecto(6))

    print("Ej16")
    cod = CodificadorCesar()
    print(cod.codificar_palabra("hola", 3))
    print(cod.historial)

    print("Ej17")
    ae = AgrupadorEdades()
    print(ae.agrupar_por_categoria(5, 15, 30, 70))

    print("Ej18")
    cd = CalculadorDistancia()
    print(cd.distancia_euclidiana((0, 0), (3, 4)))

    print("Ej19")
    invn = Inventario()
    invn.agregar_stock("pan", 50)
    print(invn.restar_stock("pan", 30))
    print(invn.productos_bajo_stock(15))

    print("Ej20")
    ap = AnalizadorPatrones()
    print(ap.agrupar_por_longitud("el gato esta aqui"))
