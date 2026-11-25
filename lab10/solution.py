import numpy as np



def make_table(rows: int, columns: int) -> list[list[int]]:
    arr = np.arange(rows * columns)
    return arr.reshape(rows, columns).tolist()

def rectangle(matrix: list[list[float]], row_start: int, row_stop: int, column_start: int, column_stop: int) -> list[list[float]]:
    arr = np.asarray(matrix)
    return arr[row_start:row_stop, column_start:column_stop].tolist()

def replace_rectangle(matrix: list[list[float]], row_start: int, row_stop: int, column_start: int, column_stop: int, value: float) -> list[list[float]]:
    arr = np.asarray(matrix, dtype = float).copy()
    arr[row_start:row_stop, column_start:column_stop]= value
    return arr.tolist()

def matrix_vector_product(matrix: list[list[float]], vector: list[float]) -> list[float]:
    arr = np.asarray(matrix)
    mult = np.asarray(vector)
    return (arr @ mult).tolist()



