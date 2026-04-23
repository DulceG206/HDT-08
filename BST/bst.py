import random

class Nodo: 
    #creo el constructor de nodo 
    def _init_(self, valor):
        self.valor = valor
        self.nodoD = None 
        self.nodoI = None 

    #creo los métodos de nodo (si es necesario)
     


class BST:
        # creo el constructor del bst 
    def __init__(self):
        self.raiz = None

    #creo los métodos del bst
    def insert(self, valor):
        if not self.raiz:
            self.raiz = Node(valor)
            return

        current = self.raiz
        while True:
            if valor < current.valor:
                if current.NodoI:
                    current = current.NodoI
                else:
                    current.NodoI = Node(valor)
                    return
            else:
                if current.NodoD:
                    current = current.NodoD
                else:
                    current.NodoD = Node(valor)
                    return

    def search(self, valor):
        current = self.raiz
        iterations = 0

        while current:
            iterations += 1

            if valor == current.valor:
                return current, iterations
            elif valor < current.valor:
                current = current.NodoI
            else:
                current = current.NodoD

        return None, iterations


    #Escenario A (Llegada Aleatoria)

    def escenario_A():
    print("\n Escenario A: Aleatorio")

    bst = BST()

    values = random.sample(range(1, 5000), 1000)

    for v in values:
        bst.insert(v)

    total_iterations = 0
    search_values = random.sample(values, 100)

    for v in search_values:
        _, it = bst.search(v)
        total_iterations += it

    avg = total_iterations / 100
    print("Promedio de iteraciones:", avg)

    #Escenario B (Llegada Secuencial)

    def escenario_B():
    print("\n Escenario B: Peor caso (ordenado)")

    bst = BST()

    for i in range(1, 1001):
        bst.insert(i)

    _, iterations = bst.search(1000)

    print("Iteraciones para encontrar 1000:", iterations)

    #Escenario C (Proceso Frecuente)

    def escenario_C():
    print("\n Escenario C: Búsqueda repetida")

    bst = BST()

    values = random.sample(range(1, 5000), 1000)

    for v in values:
        bst.insert(v)

    target = random.choice(values)

    print(f"Buscando repetidamente el valor: {target}")

    for i in range(50):
        _, iterations = bst.search(target)
        print(f"Búsqueda {i+1}: {iterations} iteraciones")















