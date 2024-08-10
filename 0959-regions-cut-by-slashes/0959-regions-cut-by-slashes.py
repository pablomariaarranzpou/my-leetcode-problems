class Solution:

    DIRECTIONS = [
    (0, 1), 
    (0, -1),  
    (1, 0), 
    (-1, 0),  
    ]

    def regionsBySlashes(self, grid):
        tamaño_del_grid = len(grid)

        grid_expandido = [[0] * (tamaño_del_grid * 3) for _ in range(tamaño_del_grid * 3)]

        for i in range(tamaño_del_grid):
            for j in range(tamaño_del_grid):
                fila_base = i * 3
                columna_base = j * 3

                if grid[i][j] == "\\":

                    grid_expandido[fila_base][columna_base] = 1
                    grid_expandido[fila_base + 1][columna_base + 1] = 1
                    grid_expandido[fila_base + 2][columna_base + 2] = 1
                elif grid[i][j] == "/":

                    grid_expandido[fila_base][columna_base + 2] = 1
                    grid_expandido[fila_base + 1][columna_base + 1] = 1
                    grid_expandido[fila_base + 2][columna_base] = 1

        cuenta_de_regiones = 0

        for i in range(tamaño_del_grid * 3):
            for j in range(tamaño_del_grid * 3):

                if grid_expandido[i][j] == 0:

                    self._flood_fill(grid_expandido, i, j)
                    cuenta_de_regiones += 1

        return cuenta_de_regiones


    def _flood_fill(self, grid_expandido, fila, columna):
        cola = [(fila, columna)]
        grid_expandido[fila][columna] = 1

        while cola:
            celda_actual = cola.pop(0)

            for direccion in self.DIRECTIONS:
                nueva_fila = direccion[0] + celda_actual[0]
                nueva_columna = direccion[1] + celda_actual[1]

                if self._is_valid_cell(grid_expandido, nueva_fila, nueva_columna):
                    grid_expandido[nueva_fila][nueva_columna] = 1
                    cola.append((nueva_fila, nueva_columna))


    def _is_valid_cell(self, grid_expandido, fila, columna):
        n = len(grid_expandido)
        return (
            fila >= 0
            and columna >= 0
            and fila < n
            and columna < n
            and grid_expandido[fila][columna] == 0
        )
