# Argparse lets your tool work across multiple files
from pathlib import Path 
import argparse

def main(): 
    parser = argparse.ArgumentParser(description = "Analyze a CSV file")
    parser.add_argument('file', help = "Path to the CSV file")
    args = parser.parse_args() ## Actually reads what the user typed in the terminal

    path = Path(args.file)
    if not path.exists():
        print(f"Error: file '{args.file}' not found ")
        return
    print (f"File found: {path}")

if __name__ == "__main__":
    main()
