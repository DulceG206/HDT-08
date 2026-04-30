from Nodo import Nodo

class Bst:
        # creo el constructor del bst 
    def __init__(self):
        self.raiz = None

    #creo los métodos del bst
    def insert(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
            return

        current = self.raiz
        while True:
            if valor < current.valor:
                if current.izq:
                    current = current.izq
                else:
                    current.izq = Nodo(valor)
                    return
            else:
                if current.der:
                    current = current.der
                else:
                    current.der = Nodo(valor)
                    return

    def search(self, valor):
        current = self.raiz
        iterations = 0

        while current:
            iterations += 1

            if valor == current.valor:
                return current, iterations
            elif valor < current.valor:
                current = current.izq
            else:
                current = current.der

        return None, iterations


    

