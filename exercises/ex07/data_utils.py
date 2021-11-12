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
    final_dict = dict()
    for item in columns:
        final_list = []  
        for row in range(n):             
            final_list.append(columns[item][n])
        final_dict[item] = final_list        
    return(final_dict)
        

def select(first_dict: dict[str, list[str]], first_list: list[str]) -> dict[str, list[str]]:
    """Produces specific set of columns."""
    final_dict = dict()
    for item in first_list:
        final_dict[item] = first_dict[item]
    return(final_dict)
        

def concat(dict_one: dict[str, list[str]], dict_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine columns."""
    end_dict = dict()
    for item in dict_one:
        end_dict[item] = dict_one[item]
    for items in dict_two:
        if items in end_dict:
            for value in dict_two:
                end_dict[items] = dict_two[value]
        else: 
            end_dict[value] = dict_two[value]
    return(end_dict)


def count(listing: list[str]) -> dict[str, int]:
    """Simple Analysis."""
    result_dict: dict[str, int] = dict()
    for item in listing:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return(result_dict)