# Software-Developer-Entry-Level-ACGP
# Prueba Técnica - Software Developer Entry Level (Trainee)
# Autor: Arturo Cadenas
# Fecha: 09/09/2025

# Parte 1: Lógica de Programación

#Problema:
# Escribe una función que reciba una lista de números enteros y devuelva una nueva lista con los números ordenados, eliminando los duplicados.
# Ejemplo:
# entrada = [4, 2, 7, 2, 4, 9, 1]
# salida = [1, 2, 4, 7, 9]

def ordenar_y_eliminar_duplicados(lista):
    # Convertir la lista a un conjunto para eliminar duplicados
    lista_sin_duplicados = list(set(lista))
    # Ordenar la lista
    lista_ordenada = sorted(lista_sin_duplicados)
    # Retornar la lista ordenada sin duplicados
    return lista_ordenada

# Ejemplo de uso
# Defino la lista de entrada
entrada = [4, 2, 7, 2, 4, 9, 1, 1, 1, 1, 4, 6, 10, 12, 1 , 2]
# Llamo a la función y almaceno el resultado en salida
salida = ordenar_y_eliminar_duplicados(entrada)
# Imprimo la salida y su tipo
print(salida)
print(type(salida))
# Salida esperada: [1, 2, 4, 6, 7, 9, 10, 12]
# Tipo de salida: <class 'list'>

# --------------------------------------------------------------- #
 
# Parte 2: Estructuras de Datos (30 puntos)

# Problema:
# Implementa una clase “ColaMinimo” que funcione como una cola (FIFO), pero que además tenga un método “minimo()” que devuelva el valor mínimo actual en la cola.

# Métodos esperados:
# - encolar(valor)
# - desencolar()
# - minimo()

# Defino la clase ColaMinimo, FIFO -> First In First Out
class ColaMinimo:
    # Defino el constructor de la clase
    def __init__(self):
        # Inicializo la cola como una lista vacía
        self.cola = []

    # Defino el método encolar: requiere de un valor numérico a agregar
    def encolar(self, valor):
        # Agrego el valor al final de la cola
        self.cola.append(valor)
        return valor


    # Defino el método desencolar, desencola el primer valor agregado
    def desencolar(self):
        # Si la cola está vacía, retorno None
        if len(self.cola) == 0:
            print("La cola está vacía")
            return None
        # Remuevo y retorno el primer valor de la cola
        valor = self.cola.pop(0)
        return valor

    # Defino el método minimo, devuelve el valor mínimo actual en la cola
    def minimo(self):
        # Si la cola está vacía, retorno None
        if len(self.cola) == 0:
            print("La cola está vacía")
            return None
        # Retorno el valor mínimo de la cola
        return min(self.cola)
    
# Ejemplo de uso
# Creo una instancia de la clase ColaMinimo
cola = ColaMinimo()
# Realizo operaciones de encolar, desencolar y obtener el mínimo
cola.encolar(2)
cola.desencolar()
cola.encolar(15)
cola.encolar(4)
cola.encolar(10)
cola.encolar(6)
cola.desencolar()
cola.encolar(3)
# Imprimo el estado actual de la cola y el valor mínimo
print(cola.cola)
print("Mínimo:", cola.minimo())
# Salida esperada: [4, 10, 6, 3], Mínimo: 3

