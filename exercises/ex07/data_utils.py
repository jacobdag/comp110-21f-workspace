"""Some helpful utility functions for working with CSV files."""


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read rows of csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = dict()
    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column)
    return result


def head(columns: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce first columns."""
    final_dict: dict[str, list[str]] = dict()
    for item in columns:
        final_list = []
        final_list.append(columns[item][n])
        final_dict[item] = final_list
    return(final_dict)
        

def select(first_dict: dict[str, list[str]], first_list: list[str]) -> dict[str, list[str]]:
    """Produces specific set of columns."""
    final_dict: dict[str, list[str]] = dict()
    for item in first_list:
        final_dict[item] = first_dict[item]
    return(final_dict)
        