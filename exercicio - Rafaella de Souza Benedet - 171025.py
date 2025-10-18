
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvorebinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Node(valor)
        else:
            self._insert_recursive(self.raiz, valor) 
        
    def _insert_recursive(self, node, valor):
        if valor < node.valor:
            if node.esquerda is None:
                 node.esquerda = Node(valor)   
            else:
                self._insert_recursive(node.esquerda, valor)
        elif valor > node.valor:
            if node.direita is None:
                node.direita = Node(valor)
            else: 
                self._insert_recursive(node.direita, valor)

    def  em_ordem(self):
        self._em_ordem_recursivo(self.raiz)
        print()

    def _em_ordem_recursivo(self, node):
        if node: 
            self._em_ordem_recursivo(node.esquerda)
            print(node.valor, end=' ')
            self._em_ordem_recursivo(node.direita)

    def pre_ordem(self):
        print("Em pré-ordem: ", end="")
        self._pre_ordem_recursivo(self.raiz)
        print()

    def _pre_ordem_recursivo(self, node):
        if node:
            print(node.valor, end=' ')
            self._pre_ordem_recursivo(node.esquerda)
            self._pre_ordem_recursivo(node.direita)
    
    def pos_ordem(self, node):
        print("Pós ordem: ", end="")
        self.pos_ordem_recursivo(node.esquerda)
        self.pos_ordem_recursivo(node.direita)
        print(node.valor, end=' ')

    def pos_ordem_recursivo(self, node):
        if node:
            self.pos_ordem_recursivo(node.esquerda)
            self.pos_ordem_recursivo(node.direita)
            print(node.valor, end=' ')
    
    def remover(self, valor):
        print(f"Removendo o nó com valor {valor}")
        self.raiz = self.remover_recursivo(self.raiz, valor)

    def remover_recursivo(self, node, valor):
        if node is None:
            return node
        
        if valor < node.valor:
            node.esquerda = self.remover_recursivo(node.esquerda, valor)
        elif valor > node.valor:
            node.direita = self.remover_recursivo(node.direita, valor)
        else: 
            if node.esquerda is None:
                return node.direita
            elif node.direita is None:
                return node.esuqerda
            else: 
                sucessor = self._encontrar_minimo(node.direita)
                node.valor = sucessor.valor
                node.direita = self.remover_recursivo(node.direita, sucessor.valor)
        return node
    
    def _encontrar_minimo(self, node):
        current = node
        while current.esquerda is not None:
            current = current.esquerda
        return current


sequencia = [60, 50, 70, 40, 65, 55, 75]
arvore = Arvorebinaria()

for valor in sequencia:
     arvore.inserir(valor)

print("Árvore após a inserção (em ordem):")
arvore.em_ordem()

print("Sequência pré-ordem:")
arvore.pre_ordem()

print("Sequência pós-ordem:")
arvore.pos_ordem()

arvore.remover(50)
print("Sequência após remover o nó 50:")
arvore.em_ordem()

arvore.remover(60)
print("Sequência após remover o nó 60:")
arvore.em_ordem()