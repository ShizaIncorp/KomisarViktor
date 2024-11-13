import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f:
        lines = [line for line in csv.DictReader(f)]

    with open(OUTPUT_FILENAME, 'w') as output_f:
        json.dump(lines, output_f, indent=4)

    with open(OUTPUT_FILENAME, 'r') as output_f:
        for line in output_f:
            print(line, end="")
    return None


if __name__ == '__main__':
    # Нужно для проверки
    task()
