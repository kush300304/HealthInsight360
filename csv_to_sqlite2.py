import sqlite3
import pandas as pd
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Directory where CSV files are stored
csv_directory = r"C:\Users\kusha\Desktop\healthinsight\medicines"

# SQLite database file path
sqlite_db_file =  r"C:\Users\kusha\Desktop\healthinsight\db.sqlite3"

# Function to create SQLite dataabase from CSV files
def create_sqlite_db(csv_directory, sqlite_db_file):
    # Create SQLite connection and cursor
    conn = sqlite3.connect(sqlite_db_file)
    cursor = conn.cursor()

    # List of CSV files in the directory
    csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]

    # Iterate through each CSV file
    for csv_file in csv_files:
        # Read CSV file into DataFrame
        try:
            df = pd.read_csv(os.path.join(csv_directory, csv_file))

            # Add 'XID' column with incremental values
            # df['XID'] = range(1, len(df) + 1)

            # Table name (without file extension)
            table_name = os.path.splitext(csv_file)[0]

            # Create table in SQLite database
            df.to_sql(table_name, conn, if_exists='replace', index=False)
        except Exception as e:
            print(f"Error processing file '{csv_file}': {e}")

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Function to update SQLite database when CSV files change
def update_sqlite_db(event):
    # Check if the event is a file modification
    if event.event_type == 'modified' and event.src_path.endswith('.csv'):
        # Update SQLite database
        create_sqlite_db(csv_directory, sqlite_db_file)
        print("SQLite database updated.")

# Watchdog event handler class
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        update_sqlite_db(event)

# Create SQLite database from CSV files
create_sqlite_db(csv_directory, sqlite_db_file)

# Create a watchdog observer
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path=csv_directory, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()