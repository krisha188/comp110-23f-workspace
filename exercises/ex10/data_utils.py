"""Dictionary related utility functions."""
__author__ = "730656379"
from csv import DictReader


# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific number."""
    result: list[str] = []
    for row in table: 
        # save every value under key header
        result.append(row[header])
    return result

def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for column_name in table[0]:
        values = column_values(table, column_name)
        result[column_name] = values
    return result

def head(table: dict[str, list[str]], rows_shown: int) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    column_names = []
    for i in table:
        column_names.append(i)
    for column in column_names:
        new: list() = []
        for n in range(0, rows_shown):
            new.append(n)
        result[column] = new
    return result