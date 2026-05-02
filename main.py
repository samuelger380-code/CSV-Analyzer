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

            column_types[header] = 'numeric' if is_numeric else 'text'
        
        print(column_types)

    print(f"Columns: {headers}")
    print(f"Row count: {len(rows)}")
    print(rows[0])



if __name__ == "__main__":
    main()
