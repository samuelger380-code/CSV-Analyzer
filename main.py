# Argparse lets your tool work across multiple files
from pathlib import Path 
import argparse
import csv

def main(): 
    parser = argparse.ArgumentParser(description = "Analyze a CSV file")
    parser.add_argument('file', help = "Path to the CSV file")
    args = parser.parse_args() ## Actually reads what the user typed in the terminal

    path = Path(args.file)
    if not path.exists():
        print(f"Error: file '{args.file}' not found ")
        return
    print (f"File found: {path}")

    with open(path, newline="") as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)

        column_types = {}

        for i, header in enumerate(headers):
            values = [row[i] for row in rows]
            is_numeric = True

            for value in values:
                try:
                    float(value)
                except ValueError:
                    is_numeric = False
                    break
            if is_numeric:
                numeric_values = [float(v) for v in values if v != ""]
                col_min = min(numeric_values)
                col_max = max(numeric_values)
                col_mean = sum(numeric_values) / len(numeric_values)

                print(f'{header}: min = {col_min}, max ={col_max}, mean = {col_mean}')


                column_types[header] = 'numeric' if is_numeric else 'text'

            
        print(column_types)

    print(f"Columns: {headers}")
    print(f"Row count: {len(rows)}")
    print(rows[0])



if __name__ == "__main__":
    main()
