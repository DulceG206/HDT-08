from Nodo import Nodo

class SplayTree:
    def __init__(self):
        self.raiz = None
       # rotación simple a la derecha
    
    def _rotar_derecha(self, x):
    #sube el hijo izquierdo o "y" de x
    y = x.izquierda
    x.izquierda = y.derecha
    if y.derecha:
        y.derecha.padre = x
    y.padre = x.padre
    if x.padre is None:
        self.raiz = y
    elif x == x.padre.derecha:
        x.padre.derecha = y
    else: 
        x.padre.izquierda = y 
        y.derecha = x
        x.padre = y
    
    def _rotar_izquierda (self, x):
        #sube el hijo derecho "y" de x
        y = x.derecha
        x.derecha = y.izquierda
        if y.izquierda:
            y.izquierda.padre = x
        y.padre = x.padre
        if x.padre is None:
            self.raiz = y
        elif  x == x.padre.izquierda:
            x.padre.izquierda = y
        else: 
            x.padre.derecha = y 
            y.izquierda = x 
            x.padre = y

        #sube x hasta la raizz
    def _splay(self, x):
        while x.padre is not None:
            padre = x.padre
            abuelo = padre.padre
 
            if abuelo is None:
                # zig, solo hay un nivel hasa llegar a la raiz
                if x == padre.izquierda:
                    self._rotar_derecha(padre)
                else:
                    self._rotar_izquierda(padre)
 
            elif x == padre.izquierda and padre == abuelo.izquierda:
                # zig zig izquierdo
                self._rotar_derecha(abuelo)
                self._rotar_derecha(padre)
 
            elif x == padre.derecha and padre == abuelo.derecha:
                # zig zig derecho
                self._rotar_izquierda(abuelo)
                self._rotar_izquierda(padre)
 
            elif x == padre.derecha and padre == abuelo.izquierda:
                #zig zag izquierda a derecha
                self._rotar_izquierda(padre)
                self._rotar_derecha(abuelo)
 
            else:
                #zig zag derecha a izquierda
                self._rotar_derecha(padre)
                self._rotar_izquierda(abuelo)
    
    def insertar(self, pid, vruntime):
        nuevo = Nodo(pid, vruntime)
        if self.raiz is None:
            self.raiz = nuevo
            return
        actual = self.raiz
        while True:
            if vruntime < actual.vruntime:
                if actual.izquierda is None:
                    actual.izquierda = nuevo
                    nuevo.padre = actual
                    break
                actual = actual.izquierda
            else:
                if actual.derecha is None:
                    actual.derecha = nuevo
                    nuevo.padre = actual
                    break
                actual = actual.derecha
        self._splay(nuevo)  # El nodo insertado sube a la raíz
        
    def insertar(self, pid, vruntime):
        nuevo = Nodo(pid, vruntime)
        if self.raiz is None:
            self.raiz = nuevo
            return
        actual = self.raiz
        while True:
            if vruntime < actual.vruntime:
                if actual.izquierda is None:
                    actual.izquierda = nuevo
                    nuevo.padre = actual
                    break
                actual = actual.izquierda
            else:
                if actual.derecha is None:
                    actual.derecha = nuevo
                    nuevo.padre = actual
                    break
                actual = actual.derecha
        self._splay(nuevo)  # El nodo insertado sube a la raíz
 
    # ── Búsqueda ────────────────────────────────
    def buscar(self, vruntime):
        iteraciones = 0
        actual = self.raiz
        ultimo = None
 
        while actual is not None:
            iteraciones += 1
            ultimo = actual
            if vruntime == actual.vruntime:
                self._splay(actual)     # Splay
                return actual, iteraciones
            elif vruntime < actual.vruntime:
                actual = actual.izquierda
            else:
                actual = actual.derecha
 
        # splayear el último visitado
        if ultimo:
            self._splay(ultimo)
        return None, iteraciones
 
    #Altura iterativa 
    def altura(self):
        if self.raiz is None:
            return 0
        from collections import deque
        cola = deque([(self.raiz, 1)])
        max_nivel = 0
        while cola:
            nodo, nivel = cola.popleft()
            max_nivel = max(max_nivel, nivel)
            if nodo.izquierda:
                cola.append((nodo.izquierda, nivel + 1))
            if nodo.derecha:
                cola.append((nodo.derecha, nivel + 1))
        return max_nivel
 