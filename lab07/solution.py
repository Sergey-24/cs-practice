def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []
    arr = np.asarray(values, dtype = float)
    arr = arr.reshape(-1, width)
    return arr.tolist()




def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    arr = np.asarray(matrix, dtype = float)
    result = arr[np.ix_(rows, columns)]
    return result.tolist()




def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype=float)
    result = np.mean(arr, axis = 0)
    return np.round(result, 6).tolist()




def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix:
        return 0.0
    arr = np.asarray(matrix, dtype=float)
    result = np.max(arr[:, column]) - np.min(arr[:, column])
    return round (float(result), 6)
