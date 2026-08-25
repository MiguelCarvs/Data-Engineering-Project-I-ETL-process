import sqlite3
from extract import extract_weather
from transform import transform_weather

def load_weather(weather):
    connection = sqlite3.connect("weather.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather(
        time TEXT,
        temperature REAL,
        humidity INTEGER,
        wind_direction INTEGER,
        wind_speed REAL
        )
    """)

    cursor.execute("""
        INSERT INTO weather(
            time,
            temperature,
            humidity,
            wind_direction,
            wind_speed
        )
        VALUES(?,?,?,?,?)
    """,(
            weather["time"],
            weather["temperature"],
            weather["humidity"],
            weather["wind_direction"],
            weather["wind_speed"]
    ))

    connection.commit()

    cursor.execute("SELECT * FROM weather")

    print(cursor.fetchall())

    connection.close()

if __name__ == "__main__":
    api_response = extract_weather()
    weather = transform_weather(api_response)
    load_weather(weather)