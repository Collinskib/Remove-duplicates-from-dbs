import sqlite3
import pandas as pd

def csv_to_sql(csv_file, table_name, sql_file):
    # Create a new connection and cursor object
    conn = sqlite3.connect(sql_file)
    cursor = conn.cursor()

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Write the DataFrame to a SQL table
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Close the database connection
    conn.close()

def print_columns(table_name, sql_file):
    # Create a new connection and cursor object
    conn = sqlite3.connect(sql_file)
    cursor = conn.cursor()

    # Get the column names of the specified table
    cursor.execute("PRAGMA table_info({})".format(table_name))
    columns = [column[1] for column in cursor.fetchall()]

    # Close the database connection
    conn.close()

    return columns

def check_duplicates(table_name, sql_file, columns):
    # Create a new connection and cursor object
    conn = sqlite3.connect(sql_file)
    cursor = conn.cursor()

    # Construct the SQL query
    query = "SELECT COUNT(*) FROM phones WHERE Item IN (SELECT Item FROM phones GROUP BY Item HAVING COUNT(*) > 1)"
    # Execute the query
    cursor.execute(query)

    # Fetch all the duplicate records
    duplicates = cursor.fetchall()

    # Close the database connection
    conn.close()

    return duplicates

def get_unique_records(table_name, sql_file):
    # Create a connection to the database
    conn = sqlite3.connect(sql_file)
    cursor = conn.cursor()

    # Create a query to retrieve the unique records
    query = "SELECT DISTINCT * FROM {}".format(table_name)

    # Execute the query
    cursor.execute(query)

    # Fetch all the unique records
    unique_records = cursor.fetchall()

    # Close the database connection
    conn.close()

    return unique_records

def get_num_rows(table_name):
    conn = sqlite3.connect(sql_file)
    cursor = conn.cursor()
    cursor.execute(f'SELECT COUNT(*) FROM {table_name}')
    num_rows = cursor.fetchone()[0]
    conn.close()
    return num_rows



def create_unique_records_table(table_name, num_rows,unique):
    # Connect to the database
    conn = sqlite3.connect(unique)
    cursor = conn.cursor()
    
    # Create the table
    query = f'CREATE TABLE {table_name} (id INTEGER PRIMARY KEY, item TEXT NOT NULL);'
    cursor.execute(query)
    
    # Insert the data
    for i in range(num_rows):
        query = f'INSERT INTO {table_name} (item) VALUES (?)'
        cursor.execute(query, (f'Item {i+1}',))
    
    # Commit the changes
    conn.commit()
    
    # Close the connection
    cursor.close()
    conn.close()    


# Call the functions
csv_file = 'Kilimall-phone.csv'
table_name = 'phones'
sql_file = 'phone.db'
unique_sql ='unique_records.db'


# Create the table
csv_to_sql(csv_file, table_name, sql_file)

# Print the columns
columns = print_columns(table_name, sql_file)
print(columns)

# Check for duplicates
duplicates = check_duplicates(table_name, sql_file, columns)
count_duplicates =f'Found {len(duplicates)} duplicates'
print(count_duplicates)

# Remove duplicates
unique_records = None
unique_records = get_unique_records(table_name, sql_file)
unique = f' Found {len(unique_records)} unique records '
print(unique)

# Updated db
num_rows = get_num_rows(table_name)
print(num_rows)
create_unique_records_table(table_name, num_rows, unique_sql)

# Check new table
unique_records = None
unique_records = get_unique_records(table_name, unique_sql)
unique = f' Found {len(unique_records)} unique records '
print(unique)

