class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        filas = len(points)
        columnas = len(points[0])

        for i in range(1, filas):
            
            izquierda = [0] * columnas
            derecha = [0] * columnas

            izquierda[0] = points[i-1][0]
            for j in range(1, columnas):
                izquierda[j] = max(izquierda[j-1] - 1, points[i-1][j])

            derecha[columnas-1] = points[i-1][columnas-1]
            for j in range(columnas-2, -1, -1):
                derecha[j] = max(derecha[j+1] - 1, points[i-1][j])

            for j in range(columnas):
                points[i][j] += max(izquierda[j], derecha[j])

        return max(points[-1])
