import sqlite3
import requests
from datetime import datetime

CITIES = {
    "Malmö": (55.6, 13.0),
    "Karachi": (24.86, 67.01),
    "Stockholm": (59.33, 18.07),
}

def get_temperature(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["current_weather"]["temperature"]


def save_reading(conn, city, temperature):
    cur = conn.cursor()
    cur.execute("INSERT INTO readings (city, temperature) VALUES (?, ?)", (city, temperature))
    # TODO: INSERT a row with city, temperature, and a timestamp
    # Timestamp: datetime.now().isoformat()

def print_summary(conn):
    cur = conn.cursor()
    cur.execute("SELECT city, COUNT(*), AVG(temperature) FROM readings GROUP BY city")
    #for row in cur.fetchall():
    #    print(row)
    for city, count, avg in cur.fetchall():
        print(f"{city}: {count} readings, average {avg:.1f}°C")
    # TODO: SELECT city, COUNT(*), AVG(temperature) ... GROUP BY city
    # and print one line per city

def main():
    conn = sqlite3.connect("weather.db")
    # TODO: CREATE TABLE IF NOT EXISTS readings
    #       (id, city, temperature, recorded_at)

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY,
            city TEXT,
            temperature REAL,
            recorded_at TEXT
        )
    """)

    for city, (lat, lon) in CITIES.items():
        temp = get_temperature(lat, lon)
        save_reading(conn, city, temp)
    conn.commit()
    print_summary(conn)
    conn.close()

main()