# CSV-Analyzer

A command-line tool that analyzes any CSV file and returns column types and stats.

## Usage

Normal output:
python main.py data/file.csv

Json output:
python main.py data/file.csv --json

## Output 
- Column headers and row count
- Numeric vs text classification per column
- Min, max, mean for numeric columns