import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              email TEXT UNIQUE NOT NULL,
              password TEXT NOT NULL)''')

# Insert a sample user
c.execute("INSERT INTO users (email, password) VALUES (?, ?)", ('admin@example.com', 'admin123'))

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()

print("Database and table created successfully with a sample user.")

