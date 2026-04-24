import Nodo as Nodo
class SplayTree:
    def __init__(self):
        self.raiz = None

    #rotaciones
    def _rotar_derecha(self, x):
        y = x.nodoI
        x.nodoI = y.nodoD

        if y.nodoD is not None:
            y.nodoD.padre = x

        y.padre = x.padre

        if x.padre is None:
            self.raiz = y
        elif x == x.padre.nodoD:
            x.padre.nodoD = y
        else:
            x.padre.nodoI = y

        y.nodoD = x
        x.padre = y

    def _rotar_izquierda(self, x):
        y = x.nodoD
        x.nodoD = y.nodoI

        if y.nodoI is not None:
            y.nodoI.padre = x

        y.padre = x.padre

        if x.padre is None:
            self.raiz = y
        elif x == x.padre.nodoI:
            x.padre.nodoI = y
        else:
            x.padre.nodoD = y

        y.nodoI = x
        x.padre = y
    def _splay(self, x):
        while x.padre is not None:
            padre = x.padre
            abuelo = padre.padre

            if abuelo is None:
                # Zig
                if x == padre.nodoI:
                    self._rotar_derecha(padre)
                else:
                    self._rotar_izquierda(padre)
            
            elif x == padre.nodoI and padre == abuelo.nodoI:
                # Zig-Zig Izquierdo
                self._rotar_derecha(abuelo)
                self._rotar_derecha(padre)
            
            elif x == padre.nodoD and padre == abuelo.nodoD:
                # Zig-Zig Derecho
                self._rotar_izquierda(abuelo)
                self._rotar_izquierda(padre)
            
            elif x == padre.nodoD and padre == abuelo.nodoI:
                # Zig-Zag (Izquierda-Derecha)
                self._rotar_izquierda(padre)
                self._rotar_derecha(abuelo)
            
            else:
                # Zig-Zag (Derecha-Izquierda)
                self._rotar_derecha(padre)
                self._rotar_izquierda(abuelo)
    
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo
            return
        
        actual = self.raiz
        while True:
            if valor < actual.valor:
                if actual.nodoI is None:
                    actual.nodoI = nuevo
                    nuevo.padre = actual
                    break
                actual = actual.nodoI
            else:
                if actual.nodoD is None:
                    actual.nodoD = nuevo
                    nuevo.padre = actual
                    break
                actual = actual.nodoD
        
        self._splay(nuevo) 
 
    def buscar(self, valor):
        iteraciones = 0
        actual = self.raiz
        ultimo = None
 
        while actual is not None:
            iteraciones += 1
            ultimo = actual
            if valor == actual.valor:
                self._splay(actual)
                return actual, iteraciones
            elif valor < actual.valor:
                actual = actual.nodoI
            else:
                actual = actual.nodoD
 
        if ultimo:
            self._splay(ultimo)
        return None, iteraciones
