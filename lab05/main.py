from tablestats import *
def main():
    name = input()
    with open(name, encoding="utf-8") as file:
        rows = read_rows(file)
    counts = count_types(rows)
    print(len(rows))
    print(len(counts))
    print(total_minutes(rows, "ошибка"))
    with open("summary.csv", "w", encoding="utf-8") as file:
        file.write(to_csv(counts))

if __name__ == "__main__":
    main()