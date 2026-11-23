import os


def insertion_sort(arr):
    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def main():
    file_path = "date.txt"

    if not os.path.exists(file_path):
        print(f"Eroare: Fișierul '{file_path}' nu există.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    if len(lines) < 2:
        print("Eroare: Fișierul trebuie să conțină cel puțin 2 linii (numerele și numele algoritmului).")
        return

    raw_numbers = lines[0].strip().split()
    if not raw_numbers:
        print("Eroare: Linia 1 nu conține numere.")
        return

    try:
        numbers = [int(x) for x in raw_numbers]
    except ValueError:
        print("Eroare: Linia 1 conține valori invalide (trebuie să fie doar numere întregi separate prin spații).")
        return

    algorithm = lines[1].strip()
    algorithms = {
        "Insertion": insertion_sort,
        "Merge": merge_sort,
    }

    if algorithm not in algorithms:
        print(f"Eroare: Algoritmul '{algorithm}' nu este implementat. Alege dintre: {', '.join(algorithms.keys())}.")
        return

    sorted_numbers = algorithms[algorithm](numbers)
    result_line = f"{algorithm}: {' '.join(map(str, sorted_numbers))}"

    with open(file_path, "a", encoding="utf-8") as f:
        if lines and lines[-1] != "":
            f.write("\n")
        f.write(result_line + "\n")

    print(f"Sortare reușită! Rezultat adăugat în {file_path}: {result_line}")


if __name__ == "__main__":
    main()