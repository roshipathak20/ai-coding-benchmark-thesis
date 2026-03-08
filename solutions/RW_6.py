# Task: CSV column averages
# Write a Python function csv_column_averages(file_path)
#
# The function should:
# - read a CSV file
# - calculate the average of numeric columns
# - return a dictionary with column averages
#
# Example output:
# {"a": 2.0, "b": 3.0}

def csv_column_averages(file_path):
    import csv

    sums = {}
    counts = {}

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for column, value in row.items():
                try:
                    num_value = float(value)
                    sums[column] = sums.get(column, 0) + num_value
                    counts[column] = counts.get(column, 0) + 1
                except ValueError:
                    continue

    averages = {column: sums[column] / counts[column] for column in sums}
    return averages