import sqlite3

# Create a connection to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('test.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a simple table with some columns
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Insert some data into the table
cursor.execute('''
INSERT INTO users (name, email, age) VALUES
('Alice', 'alice@example.com', 25),
('Bob', 'bob@example.com', 30),
('Charlie', 'charlie@example.com', 35)
''')

# Commit changes and close the connection
conn.commit()
conn.close()
