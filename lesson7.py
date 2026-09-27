import sqlite3

conn = sqlite3.connect("weather.db")   # creates the file if it doesn't exist
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS readings (
        id INTEGER PRIMARY KEY,
        city TEXT,
        temperature REAL
    )
""")

cur.execute("INSERT INTO readings (city, temperature) VALUES (?, ?)", ("Malmö", 14.2))
cur.execute("INSERT INTO readings (city, temperature) VALUES (?, ?)", ("Karachi", 29.5))
conn.commit()   # saves the changes

cur.execute("SELECT city, temperature FROM readings ORDER BY temperature")
for row in cur.fetchall():
    print(row)

conn.close()