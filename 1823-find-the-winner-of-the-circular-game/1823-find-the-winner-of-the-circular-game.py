class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        index = 0
        lista = [i for i in range(1,n + 1)]

        while len(lista) > 1:
            eliminar = (index + k - 1) % len(lista)
            lista.pop(eliminar)
            index = eliminar
            
        return lista[0]
        