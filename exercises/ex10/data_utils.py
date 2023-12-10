"""Dictionary related utility functions."""
__author__ = "730656379"
from csv import DictReader


# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
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
    """Make a table."""
    result: dict[str, list[str]] = {}
    for column_name in table[0]:
        values = column_values(table, column_name)
        result[column_name] = values
    return result


def head(table: dict[str, list[str]], rows_shown: int) -> dict[str, list[str]]:
    """Only shows some rows of the table."""
    if rows_shown >= len(table):
        return table
    result: dict[str, list[str]] = {}
    for i in table:
        n = []
        x = 0
        while x < rows_shown:
            n.append(table[i][x])
            x += 1
        result[i] = n
    return result


def select(table: dict[str, list[str]], name: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only some columns."""
    result: dict[str, list[str]] = {}
    for i in name:
        result[i] = table[i]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine tables."""
    result: dict[str, list[str]] = {}
    for i in table1:
        result[i] = table1[i]
    for j in table2:
        if j in result:
            for k in table2[j]:
                result[j].append(k)
        else:
            result[j] = table2[j]
    return result