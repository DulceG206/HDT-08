# Splay.py
from Nodo import Nodo

class SplayTree:
    def __init__(self):
        self.raiz = None

    def _rotar_derecha(self, x):
        y = x.izq
        x.izq = y.der
        if y.der:
            y.der.padre = x

        y.padre = x.padre

        if not x.padre:
            self.raiz = y
        elif x == x.padre.der:
            x.padre.der = y
        else:
            x.padre.izq = y

        y.der = x
        x.padre = y

    def _rotar_izquierda(self, x):
        y = x.der
        x.der = y.izq
        if y.izq:
            y.izq.padre = x

        y.padre = x.padre

        if not x.padre:
            self.raiz = y
        elif x == x.padre.izq:
            x.padre.izq = y
        else:
            x.padre.der = y

        y.izq = x
        x.padre = y

    def _splay(self, x):
        while x.padre:
            p = x.padre
            g = p.padre

            if not g:
                if x == p.izq:
                    self._rotar_derecha(p)
                else:
                    self._rotar_izquierda(p)

            elif x == p.izq and p == g.izq:
                self._rotar_derecha(g)
                self._rotar_derecha(p)

            elif x == p.der and p == g.der:
                self._rotar_izquierda(g)
                self._rotar_izquierda(p)

            elif x == p.der and p == g.izq:
                self._rotar_izquierda(p)
                self._rotar_derecha(g)

            else:
                self._rotar_derecha(p)
                self._rotar_izquierda(g)

    def insertar(self, valor):
        nuevo = Nodo(valor)

        if not self.raiz:
            self.raiz = nuevo
            return

        actual = self.raiz
        while True:
            if valor < actual.valor:
                if not actual.izq:
                    actual.izq = nuevo
                    break
                actual = actual.izq
            else:
                if not actual.der:
                    actual.der = nuevo
                    break
                actual = actual.der

        nuevo.padre = actual
        self._splay(nuevo)

    def buscar(self, valor):
        iteraciones = 0
        actual = self.raiz
        ultimo = None

        while actual:
            iteraciones += 1
            ultimo = actual
            if valor == actual.valor:
                self._splay(actual)
                return actual, iteraciones
            elif valor < actual.valor:
                actual = actual.izq
            else:
                actual = actual.der

        if ultimo:
            self._splay(ultimo)

        return None, iteraciones
 
