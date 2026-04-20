class BinarySearchTree: 
    def _init_(self, raiz, nodo): #constructor de la clase
        self.raiz = raiz
        self.nodo = nodo
        
        #metodos de la clase

        def insertar(self, valor):
            if self.raiz is None:
                self.raiz = Nodo(valor, None)
            else:
                self._insertar_recursivo(self.raiz, valor)

        def eliminar(self, valor):
            self.raiz = self._eliminar_recursivo(self.raiz, valor)