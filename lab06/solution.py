def count_items(values:  list) -> dict:
    counts = {}
    for item in values:
        counts[item] = counts.get(item, 0) + 1
    return counts

def unique_sorted(values: list) -> list:
    result = set(values)
    return sorted(result)

def common(first: list, second: list) -> list:
    result = set(first) & set(second)
    return sorted(common)

def only_in_first(first: list, second: list) -> list:
    only_in_first = set(first) - set(second)
    return sorted(only_in_first)
