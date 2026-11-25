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

def matrix_multiply(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    arr1 = np.asarray(left)
    arr2 = np.asarray(right)
    return (arr1 @ arr2).tolist()

def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    arr = np.asarray(matrix)
    return arr.T.tolist()

def solve_system(matrix: list[list[float]], vector: list[float]) -> list[float]:
    arr = np.asarray(matrix)
    mult = np.asarray(vector)
    x = np.linalg.solve(arr, mult)
    return np.round(x, 6).tolist()

def tensor_channel_mean(tensor: list) -> list:
    arr = np.asarray(tensor)
    return arr.mean(axis=-1).tolist()

def point_distance(first: list[float], second: list[float]) -> float:
    point1 = np.asarray(first, dtype=float)
    point2 = np.asarray(second, dtype=float)
    dist = np.linalg.norm(point1 - point2)
    return round(float(dist), 6)


