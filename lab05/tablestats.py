def read_rows(lines: list[str]) -> list[dict]:
    rows = []
    header = []
    for line in lines:
        line = line.strip()

        if not line:
            continue

        values = line.split(",")
        values = [x.strip() for x in values]

        if not header:
            header = values
            continue

        if len(values) == len(header):
            rows.append(dict(zip(header, values)))
    return rows


def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row["тип"]

        if kind not in counts:
            counts[kind] = 0

        counts[kind] += 1
    return counts



def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0
    for row in rows:
        if row["тип"] == kind:
            try:
                minutes = float(row["минуты"].replace(",", "."))
                total += minutes
            except ValueError:
                continue
    return round(total, 1)



def to_csv(counts: dict) -> str:
    result = "тип,количество\n"
    for kind in sorted(counts):
        result += kind + "," + str(counts[kind]) + "\n"
    return result