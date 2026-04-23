import random
import time 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches 
import numpy as np 

from SplayTree import SplayTree
#llegada aleatoria - escenario A

def escenario_A():
    print("\n" + "="*50)
    print(" Escenario A, Llegada aleatoria")
    print("="*50)

    N = 1000
    Busquedas = 100
    #numeros aleatorios unicos 
    vruntimes = random.sample(range (1, 1_000_000), N)
    pids = list(range (1, N + 1))

    splay = SplayTree()
    #se insertan lso 1000 procesos 
    for pid, vr in zip(pids, vruntimes):
        splay.insertar(pid, vr)
    