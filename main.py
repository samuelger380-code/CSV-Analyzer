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
        row_count = sum(1 for row in reader)

    print(f"Columns: {headers}")
    print(f"Rows: {row_count}")



if __name__ == "__main__":
    main()
