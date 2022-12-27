import sqlite3
import datetime
import csv


def create_table_and_insert_records(file_paths):
    # Connecting to the database
    conn = sqlite3.connect("lake_project.db")
    cursor = conn.cursor()

    # Creating the table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS lake_data (application text, date text, amount real, load_date text)"
    )
    # picking up the file from a list in file_paths
    for file_path in file_paths:
        try:
            # Read the data from the file
            with open(file_path, "r") as f:
                reader = csv.reader(f)
                next(reader)  # Skip the header row
                for row in reader:
                    application, date, amount, load_date = row
                    date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
                    # Insert the record into the table if it meets the required criteria
                    if (
                            (file_path == "Lake_20201001.txt" and date >= datetime.datetime(2005, 1, 1))
                            or (file_path == "Lake_20201002.txt" and datetime.datetime(2004, 1, 1) <= date < datetime.datetime(2005, 1, 1))
                            or (file_path == "Lake_20201003.txt" and datetime.datetime(2003, 1, 1) <= date < datetime.datetime(2004, 1, 1))
                            or (file_path == "Lake_20201004.txt" and datetime.datetime(2002, 1, 1) <= date < datetime.datetime(2003, 1, 1))
                            or (file_path == "Lake_20201005.txt" and datetime.datetime(2001, 1, 1) <= date < datetime.datetime(2002, 1, 1))
                    ):
                        cursor.execute(
                            "INSERT INTO lake_data (application, date, amount, load_date) VALUES (?, ?, ?, ?)",
                            (application, date, amount, load_date),
                        )
        except Exception as e:
            print(f"Error while reading file {file_path}: {e}")
            continue

    # Close the cursor and commit
    cursor.close()
    conn.commit()


# list of files want to check and insertion into database
file_paths = ["Lake_20201001.txt", "Lake_20201002.txt", "Lake_20201003.txt", "Lake_20201004.txt", "Lake_20201005.txt"]
# calling the function
create_table_and_insert_records(file_paths)
