from Bst import Bst
from Nodo import Nodo
from Splay import SplayTree
import random 
import time 
import matplotlib.pyply as plt


def medir(tree, valores):
    inicio = time.time()

    for v in valores:
        tree.insert(v) if hasattr(tree, "insert") else tree.insertar(v)

    total_iter = 0

    for v in random.sample(valores, 100):
        if hasattr(tree, "search"):
            _, it = tree.search(v)
        else:
            _, it = tree.buscar(v)
        total_iter += it

    fin = time.time()

    return fin - inicio, total_iter / 100


def main():
    sizes = [100, 500, 1000, 2000]

    bst_times = []
    splay_times = []

    bst_iters = []
    splay_iters = []

    for n in sizes:
        valores = random.sample(range(1, 10000), n)

        bst = Bst()
        splay = SplayTree()

        t1, it1 = medir(bst, valores)
        t2, it2 = medir(splay, valores)

        bst_times.append(t1)
        splay_times.append(t2)

        bst_iters.append(it1)
        splay_iters.append(it2)

    # Gráfica tiempo
    plt.figure()
    plt.plot(sizes, bst_times, label="BST")
    plt.plot(sizes, splay_times, label="Splay")
    plt.legend()
    plt.title("Tiempo de ejecución")
    plt.xlabel("N procesos")
    plt.ylabel("Tiempo (s)")
    plt.show()

    # Gráfica iteraciones
    plt.figure()
    plt.plot(sizes, bst_iters, label="BST")
    plt.plot(sizes, splay_iters, label="Splay")
    plt.legend()
    plt.title("Iteraciones promedio")
    plt.xlabel("N procesos")
    plt.ylabel("Iteraciones")
    plt.show()


if __name__ == "__main__":
    main()