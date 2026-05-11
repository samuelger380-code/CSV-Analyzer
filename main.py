# Argparse lets your tool work across multiple files
from pathlib import Path 
import argparse
import csv
import json

def main(): 
    parser = argparse.ArgumentParser(description = "Analyze a CSV file")
    parser.add_argument('file', help = "Path to the CSV file")
    parser.add_argument('--json', action = 'store_true', help = 'Output as json' )
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
    stats = {}
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

        if is_numeric:
            numeric_values = [float(v) for v in values if v != ""]
            col_min = min(numeric_values)
            col_max = max(numeric_values)
            col_mean = sum(numeric_values) / len(numeric_values)
            

            stats[header] = {
                'min': col_min,
                'max': col_max,
                'mean':  col_mean

            }
        



    if args.json:
        print(json.dumps({
        'headers': headers,
        'row count': len(rows),
        'column type': column_types,
        'stats': stats
    }))
    else:
        print(f"Columns: {headers}")
        print(f"Row count: {len(rows)}")
        for header, s in stats.items():
            print(f"{header}: min={s['min']}, max={s['max']}, mean={s['mean']:.2f}")
        print(f"\nColumn types: {column_types}") 


    


if __name__ == "__main__":
    main()
