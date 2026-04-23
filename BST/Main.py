import Bst as Bst
import Nodo as Nodo
import random 

class Main: 

    #Escenario A (Llegada Aleatoria)

    def escenario_A(): print("\n Escenario A: Aleatorio")

    bst = Bst()

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

    def escenario_B(): print("\n Escenario B: Peor caso (ordenado)")

    bst = Bst()

    for i in range(1, 1001):
        bst.insert(i)

    _, iterations = bst.search(1000)

    print("Iteraciones para encontrar 1000:", iterations)

    #Escenario C (Proceso Frecuente)

    def escenario_C(): print("\n Escenario C: Búsqueda repetida")

    bst = Bst()

    values = random.sample(range(1, 5000), 1000)

    for v in values:
        bst.insert(v)

    target = random.choice(values)

    print(f"Buscando repetidamente el valor: {target}")

    for i in range(50):
        _, iterations = bst.search(target)
        print(f"Búsqueda {i+1}: {iterations} iteraciones")
