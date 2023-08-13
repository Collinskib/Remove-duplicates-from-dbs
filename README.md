# Remove-duplicates-from-dbs

# SQLite Database Operations

This project provides a Python solution for performing various operations on a SQLite database and CSV files. It offers functions to convert CSV files into SQLite tables, retrieve column names, check for duplicates, retrieve unique records, and create new tables with unique records.

## Features

- **CSV to SQL Conversion**: Convert a CSV file into a SQLite table with the `csv_to_sql` function.
- **Column Name Retrieval**: Retrieve the column names of a table using the `print_columns` function.
- **Duplicate Record Checking**: Identify and handle duplicate records with the `check_duplicates` function.
- **Unique Record Retrieval**: Retrieve all unique records from a table using the `get_unique_records` function.
- **Number of Rows**: Obtain the number of rows in a table with the `get_num_rows` function.
- **Unique Records Table Creation**: Create a new table with only unique records using the `create_unique_records_table` function.

## Getting Started

To use this project, follow these steps:

1. Clone the repository
1. Install the required dependencies: `pip install pandas sqlite`
1. Import the functions from `sql.py` into your code.
1. Use the functions according to your requirements.

## Usage

Here's an example of how to use the functions:

```python
# CSV file and table name
csv_file = 'Kilimall-phone.csv'
table_name = 'phones'

# SQL file for the database
sql_file = 'phone.db'
unique_sql = 'unique_records.db'

# Convert CSV to SQL
csv_to_sql(csv_file, table_name, sql_file)

# Print column names
columns = print_columns(table_name, sql_file)
print("Column Names:", columns)

# Check for duplicates
duplicates = check_duplicates(table_name, sql_file, columns)
print("Number of Duplicates:", len(duplicates))

# Retrieve unique records
unique_records = get_unique_records(table_name, sql_file)
print("Number of Unique Records:", len(unique_records))

# Create a new table with unique records
num_rows = get_num_rows(table_name)
create_unique_records_table(table_name, num_rows, unique_sql)
```

Make sure to replace the file names and table names with your own.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to use and modify the code as per your needs.

## Acknowledgements

- [pandas ↗](https://pandas.pydata.org/): A powerful data analysis library used for reading CSV files and working with DataFrames.
- [SQLite ↗](https://www.sqlite.org/): A lightweight, serverless database engine used for storing and managing the data.

## Contact

For any questions or inquiries, please reach out to me at collinskibowen@gmail.com.

**Happy coding!**
