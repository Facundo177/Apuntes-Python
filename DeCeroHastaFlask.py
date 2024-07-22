'''
Descargar PyCharm Community

Para comentar (shift + alt + A)

'''

print("Hola Mundo!")

miVariable = "Python"
miVariable = 10


x = 10
y = 2
z = x + y


id(x)           # Dirección de memoria de esa variable
print(id(x))




'''
Tipos de datos

Numeric:- integer
        - float
        - complex
Dictionary
Boolean
Set
Sequence:   - String
            - List
            - Tuple

'''


type(x)

x: str = "Hola Mundo"       # No jace nada, solo es un comentario (puede seguir asignandosele cualquier tipo de dato)

x = True


miGrupoFavorito = "Aerosmith"

print("Mi grupo favorito es:", miGrupoFavorito)             # Se agrega automáticamente el espacio
print("Mi grupo favorito es:" + " " + miGrupoFavorito)

numero1 = "1"
numero1 = int(numero1)




miVariable = 1 > 0

if miVariable:
    
else:
    




dato = input("Escribe algo: ")

numero = int(input("Escribe un numero: "))




# Operadores

""" 
+
-
*
/
//
**
%


Se pueden usar con un = para hacerlos de asignación
Ej: +=, /=, *=, -=


Comparación
==
!=
<
<=
>
>=


Lógicos
and
or
not

"""


suma = 3 + 2

# Otra mejor forma para imprimir
print(f"Resultado suma: {suma}")



if a % 2 == 0:
        print("Par")
else:
        print("Impar")


dentroRango = (valor <= Max) and (valor >= Min)





print("Dentro de los 20\'s")            # \ para caracteres especiales que podrían interferir en el string



if condicion == True:
        print("Verdadero")
elif condicion == False:
        print("Falso")
else:
        print("No reconocido")


# Si no hacemos eso, cualquier valor no vacío se tomaría como verdadero ("Hola" sería verdadero por ejemplo, y "" falso)


# Simplificación (Operador ternario)

print("Condicion Verdadera") if condicion else print("Condicion Falsa")


# Rangos

if 0 <= edad < 10:
        mensaje = "Infancia"





# Ciclos

while condicion:
        
else:
        


contador = 0

while contador < 3:
        print(contador)
        contador += 1
else:
        print("Fin")




cadena = "Hola"

for letra in cadena:
        print(letra)
        
        if letra == 'z':
                break
else:
        print("Fin")



for i in range(6):
        if i % 2 != 0:
                continue
        print(f"Valor: {i}")






# Uso de listas

array = [1, 2, 3, 4]

print(array[0:2])     # [1, 2]        (es el primero inclusive hasta el después de : sin incluir, por ej, [3:8] es del índice 3 al 7)

array[:3]     # Desde el inicio hasta el índice 2 (3 no incluido)

array[2:]     # Desde el índice 2 hasta el final



for numero in array:
        print(array[numero])



len(array)      # Cantidad de elementos

array.append(5)         # Agrega el valor indicado como último elemento

array.insert(0, "Cero")      # Inserta en el índice 0 el valor Cero, todos los elementos se mueven un lugar (ahora el índice y valor coinciden)

array.remove("Cero")    # Elimina el valor del array (no importa el índice)

array.pop()     # Por default elimina el último elemento (aunque se puede indicar el índice)

del array[3]    # Elimina el elemento en el índice 3 (2)

array.clear()   # Vacía la lista

del array       # Elimina completamente la lista de memoria






# Tuplas (lista inmutable)

frutas = ("Naranja", "Banana", "Frutilla")      # Ya no se puede modificar (si solo va a tener un valor hay que poner la coma igualmente, por ej, ("Naranja",))       

len(frutas)

frutas[0]
frutas[1]
frutas[2]

frutas[-1]

frutas[0:2]

for fruta in frutas:
        print(fruta, end=" ")


# La única forma de modificar una tupla es convertirla en una lista y después volver a convertirla




# Set (lista desordenada, sin duplicados)

planetas = {"Marte", "Jupiter", "Venus"}

len(planetas)

print("Marte" in planetas)      # True

planetas.add("Tierra")

planetas.remove("Tierra")

planetas.discard("Tierrassss")  # No da error aunque no exista, remove sí daría error

planetas.clear()

del planetas




# Diccionario

diccio = {
        nombre: "Juan",
        apellido: "Perez"
} 

len(diccio)

diccio["nombre"]

diccio.get("apellido")

diccio["edad"] = 19

for key, value in diccio.items():
        print(key, value)


for key in diccio.keys():
        print(key)


for value in diccio.values():
        print(value)


print("nombre" in diccio)       # True


diccionario.pop("edad")





# Funciones

def mi_funcion(nombre, apellido):
        print(f"Saludos {nombre} {apellido}")

mi_funcion("Juan", "Perez")



# Valores default

def sumar(a = 0, b = 0):
        return a + b

sumar()         # 0
sumar(10, 2)    # 12



# Cantidad desconocida de argumentos

def listarNombres(*nombres):
        for nombre in nombres:
                print(nombre)

listarNombres("Juan", "Carlos", "Maria")



# Diccionario como argumento

def listarTerminos(**terminos):
        for llave, valor in terminos.items():
                print(f"{llave}: {valor}")




# Función recursiva

def factorial(numero):
        if numero == 1:
                return 1
        else:
                return numero * factorial(numero-1)

print(f"El factorial de 5 es {factorial(5)}")




# Clases

class Persona:
        def __init__(self, nombre, apellido, edad):             # __ = dunder
                self.nombre = nombre
                self.apellido = apellido
                self.edad = edad
        
        def mostrar_detalle(self):
                print(f"Persona: {self.nombre} {self.apellido}, {self.edad}")

persona1 = Persona("Juan", "Perez", 28)
print(persona1.nombre)
persona1.mostrar_detalle()

persona2 = Persona("Karla", "Gomez", 30)
persona2.mostrar_detalle()


Persona.mostrar_detalle(persona1)       # Usar método desde la clase (en este caso hay que indicar qué instancia va a tomar el parámetro self)




class Aritmetica:
        def __init__(self, operandoA, operandoB):
                self.operandoA = operandoA
                self.operandoB = operandoB
        
        def sumar(self):
                return self.operandoA + self.operandoB
        
        def restar(self):
                return self.operandoA - self.operandoB
        
        def multiplicar(self):
                return self.operandoA * self.operandoB
        
        def dividir(self):
                return self.operandoA / self.operandoB



class Rectangulo:
        def __init__(self, base, altura):
                self.base = base
                self.altura = altura
        
        def area(self):
                return self.base * self.altura 



# Encapsulamiento

# En el init se puede poner _ antes del nombre del atributo para que otros sepan que no se debe acceder, aunque no cambia nada del funcionamiento

# self._nombre = nombre


# Métodos get y set

@property
def nombre(self):
        return self._nombre

persona1.nombre         # Por el decorador @property, el método get del nombre ahora se accede como un atributo común
                        # De esta forma, al atributo no se accede directamente (aunque se sigue pudiendo hacer persona1._nombre, pero no es lo correcto)


@nombre.setter
def nombre(self, nombre):
        self._nombre = nombre

persona1.nombre = "Carlos"


# Como el método get (nombre) y el atributo (_nombre) tienen nombres distintos, si no ponemos un set se transforma en un valor de solo lectura





# Clase bien definida

class Persona:
        def __init__(self, nombre, apellido, edad):
                self._nombre = nombre
                self._apellido = apellido
                self._edad = edad
        
        @property
        def nombre(self):
                return self._nombre
        
        @nombre.setter
        def nombre(self, nombre):
                self._nombre = nombre
        
        @property
        def apellido(self):
                return self._apellido
        
        @apellido.setter
        def apellido(self, apellido):
                self._apellido = apellido
        
        @property
        def edad(self):
                return self._edad
        
        @edad.setter
        def edad(self, edad):
                self._edad = edad
        
        def mostrar_detalle(self):
                print(f"Persona: {self._nombre} {self._apellido}, {self._edad}")



""" 
Guardar definición de clase en un archivo Persona.py

En otro archivo en el que queramos utilizarla solo hace falta importarla 

"""

from Persona import Persona
from Persona import *           # Importa todo


# Código de prueba

# Para que solo se ejecute en caso de ser nuestro archivo principal pero no al ser importado se puede hacer esto:

if __name__ == "__main__":
        # Código

# Esto verifica si nuestro archivo se está ejecutando como el principal
# Todo lo que esté fuera del if sí se va a ejecutar aunque no sea el principal
# Esto se puede usar para hacer pruebas que después no tengan que ejecutarse al ser importado el archivo




# Parámetro de print (centrar y caracteres extra)

print("Hola".center(30, '-'))




# Método destructor

def __del__(self):
        print("Persona eliminada: {self._nombre} {self._apellido}")

del persona1    # Se va a imprimir el mensaje cuando se elimine




# Herencia

class Persona:
        def __init__(self, nombre, edad):
                self.nombre = nombre
                self.edad = edad

class Empleado(Persona):
        def __init__(self, nombre, edad, sueldo):
                super().__init__(nombre, edad)
                self.sueldo = sueldo

empleado1 = Empleado("Juan", 28, 200000)



# Método str

# Persona
def __str__(self):
        return f"Persona: {self.nombre} {self.edad}"

# Empleado
def __str__(self):
        return f"Empleado: {self.sueldo}, {super().__str__()}"





# Herencia múltiple

class FiguraGeometrica:
        def __init__(self, ancho, alto):
                self.ancho = ancho
                self.alto = alto

class Color:
        def __init__(self, color):
                self.color = color

class Cuadrado(FiguraGeometrica, Color):
        def __init__(self, lado, color):
                FiguraGeometrica.__init__(self, lado, lado)
                Color.__init__(self, color)
        
        def calcular_area(self):
                return self.ancho * self.alto





# MRO (Method resolution order)

print(Cuadrado.mro())

# Al heredar de clases padre, el órden en el que las escribamos en los () es la jerarquía que tendrán
# Por ejemplo: Cuadrado -> FiguraGeometrica -> Color -> object

# Sirve saberlo para cuando hay métodos iguales en varias clases (se toma el primero/de mayor jerarquía)




# Clases bien definidas + validaciones (init y setters)

class FiguraGeometrica:
        def __init__(self, ancho, alto):
                if self._validar_valor(ancho):
                        self._ancho = ancho
                else:
                        self._ancho = 0
                        print(f"Valor erroneo -> ancho: {ancho}")
                if self._validar_valor(alto):
                        self._alto = alto
                else:
                        self._alto = 0
                        print(f"Valor erroneo -> alto: {alto}")
        
        @property
        def ancho(self):
                return self._ancho
        
        @ancho.setter
        def ancho(self, ancho):
                if _validar_valor(ancho):
                        self._ancho = ancho
                else:
                        print(f"Valor erroneo -> ancho: {ancho}")
        
        @property
        def alto(self):
                return self._alto
        
        @alto.setter
        def alto(self, alto):
                if _validar_valor(alto):
                        self._alto = alto
                else:
                        print(f"Valor erroneo -> alto: {alto}")
        
        def __str__(self):
                return f"FiguraGeometrica[ancho: {self._ancho}, alto: {self._alto}]"
        
        def _validar_valor(self, valor):
                return True if 0 < valor else False


class Color:
        def __init__(self, color):
                self._color = color
        
        @property
        def color(self):
                return self._color
        
        @color.setter
        def color(self, color):
                self._color = color
        
        def __str__(self):
                return f"Color[color: {self._color}]"


class Cuadrado(FiguraGeometrica, Color):
        def __init__(self, lado, color):
                FiguraGeometrica.__init__(self, lado, lado)
                Color.__init__(self, color)
        
        def calcular_area(self):
                return self.ancho * self.alto
        
        def __str__(self):
                return f"{FiguraGeometrica.__str__(self)} {Color.__str__(self)}"


class Rectangulo(FiguraGeometrica, Color):
        def __init__(self, ancho, alto, color):
                FiguraGeometrica.__init__(self, ancho, alto)
                Color.__init__(self, color)
        
        def calcular_area(self):
                return self.ancho * self.alto
        
        def __str__(self):
                return f"{FiguraGeometrica.__str__(self)} {Color.__str__(self)}"



rectangulo1 = Rectangulo(ancho=9, alto=8, color="verde")        # __init__
print(rectangulo1)                                              # __str__
print(rectangulo1.alto)                                         # getter
rectangulo1.ancho = 6                                           # setter
print(rectangulo1)
print(rectangulo1.calcular_area())                              # método definido







# Clases abstractas (no se pueden instanciar)
# Métodos abstractos para obligar a las clases hijas a redefinirlos


from abc import ABC, abstractmethod     # Abstract Base Class

class FiguraGeometrica(ABC):
        
        # todo el código anterior
        
        @abstractmethod
        def calcular_area(self):
                pass








# Variables de clase (compartidas por todos los objetos)

class MiClase:
        variable_clase = "Var clase"
        
        def __init__(self, variable_instancia):
                self.variable_instancia = variable_instancia


print(MiClase.variable_clase)

miClase = MiClase("Var instancia")
print(miClase.variable_instancia)
print(miClase.variable_clase)

miClase2 = MiClase("Var instancia 2")
print(miClase2.variable_instancia)      # Distinta al anterior
print(miClase2.variable_clase)          # Igual


MiClase.variable_clase2 = "Var clase 2"         # Crear variable de clase de forma dinámica, se puede hacer en cualquier momento
print(miClase.variable_clase2)
print(miClase2.variable_clase2)





# Métodos estáticos (no pueden acceder a variables de instancia, ya que la creación de la clase es anterior a poder instanciarla)
# Métodos de clase (sí recibe un contexto de clase)

class MiClase:
        variable_clase = "Var clase"
        
        def __init__(self, variable_instancia):
                self.variable_instancia = variable_instancia
        
        @staticmethod
        def metodo_estatico():          # no hay self porque no hay instancia
                print(MiClase.variable_clase)           # Hay que poner el nombre de la clase porque este método no tiene contexto
        
        @classmethod
        def metodo_clase(cls):          # toma como valor automáticamente la clase en la que se define el método (como sería el self para las instancias)
                print(cls.variable_clase)
        
        def metodo_instancia(self):
                self.metodo_clase()
                self.metodo_estatico()

MiClase.metodo_estatico()
MiClase.metodo_clase()

miObjeto1 = MiClase("variable instancia")
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()






# Constantes (como simularlas, en python no existen)

MI_CONSTANTE = "Var const"

class Matematicas:
        PI = 3.1416

# Crear archivo constantes.py

# from constantes import *
from constantes import MI_CONSTANTE
from constantes import Matematicas as Mate

print(MI_CONSTANTE)
print(Mate.PI)

# Aunque si hago MI_CONSTANTE = "Nuevo valor" sí se puede modificar igual







# Contador de objetos

class Persona:
        contador_personas = 0
        
        @classmethod
        def generar_siguiente_valor(cls):
                cls.contador_personas += 1
                return cls.contador_personas
        
        def __init__(self, nombre, edad):
                self.id_persona = Persona.generar_siguiente_valor()
                self.nombre = nombre
                self.edad = edad
        
        def __str__(self):
                return f"Persona[id_persona: {self.id_persona}, nombre: {self.nombre}, edad: {self.edad}]"

print(Persona.contador_personas)        # Para ver el total







# Manejo de clases (diseño)

# en un Producto.py:
class Producto:
        contador_productos = 0
        
        def __init__(self, nombre, precio):
                Producto.contador_productos += 1
                self._id_producto = Producto.contador_productos
                self._nombre = nombre
                self._precio = precio
        
        @property
        def precio(self):
                return self._precio
        
        def __str__(self):
                return f"Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}"

if __name__ == "__main__":
        producto1 = Producto("Camisa", 100.00)
        print(producto1)
        producto2 = Producto("Pantalon", 150.00)
        print(producto2)



# en un Orden.py
from Producto import Producto

class Orden:
        contador_ordenes = 0
        
        def __init__(self, productos):
                Orden.contador_ordenes += 1
                self._id_orden = Orden.contador_ordenes
                self._productos = list(productos)
        
        def agregar_producto(self, producto):
                self._productos.append(producto)
        
        def calcular_total(self):
                total = 0
                for producto in self._productos:
                        total += producto.precio
                return total
        
        def __str__(self):
                productos_str = ""
                for producto in self._productos:
                        productos_str += producto.__str__() + " | "
                return f"Orden: {self._id_orden} \nProductos: {productos_str}"

if __name__ == "__main__":
        producto1 = Producto("Camisa", 100.00)
        producto2 = Producto("Pantalon", 150.00)
        productos = [producto1, producto2]
        
        orden1 = Orden(productos)
        print(orden1)



# en un test.py
from Producto import Producto
from Orden import Orden

producto1 = Producto("Camisa", 100.00)
producto2 = Producto("Pantalon", 150.00)
producto3 = Producto("Medias", 50.00)
producto4 = Producto("Blusa", 70.00)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]

orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
print(orden1)
print(f"Total orden 1: {orden1.calcular_total()}")

orden2 = Orden(productos2)
print(orden2)
print(f"Total orden 2: {orden2.calcular_total()}")



# 16. Sobrecarga de operadores
