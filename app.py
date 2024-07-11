from flask import Flask, jsonify, render_template
import sqlite3
import requests

app = Flask(__name__)

DATABASE = 'weather.db'

CAPITALS = {
    "Africa": ["Cairo", "Nairobi", "Pretoria", "Accra"],
    "Asia": ["Tokyo", "Beijing", "Delhi", "Seoul"],
    "Europe": ["London", "Paris", "Berlin", "Madrid"],
    "North America": ["Washington, D.C.", "Ottawa", "Mexico City", "Havana"],
    "South America": ["Brasilia", "Buenos Aires", "Santiago", "Lima"],
    "Oceania": ["Canberra", "Wellington", "Suva", "Port Moresby"]
}

COORDINATES = {
    "Cairo": (30.0444, 31.2357),
    "Nairobi": (-1.286389, 36.817223),
    "Pretoria": (-25.747868, 28.229271),
    "Accra": (5.603717, -0.186964),
    "Tokyo": (35.689487, 139.691711),
    "Beijing": (39.904202, 116.407394),
    "Delhi": (28.613939, 77.209023),
    "Seoul": (37.566536, 126.977966),
    "London": (51.507351, -0.127758),
    "Paris": (48.856613, 2.352222),
    "Berlin": (52.520008, 13.404954),
    "Madrid": (40.416775, -3.703790),
    "Washington, D.C.": (38.907192, -77.036873),
    "Ottawa": (45.421530, -75.697193),
    "Mexico City": (19.432608, -99.133209),
    "Havana": (23.113592, -82.366596),
    "Brasilia": (-15.826691, -47.921820),
    "Buenos Aires": (-34.603722, -58.381592),
    "Santiago": (-33.448891, -70.669266),
    "Lima": (-12.046374, -77.042793),
    "Canberra": (-35.280937, 149.130009),
    "Wellington": (-41.286461, 174.776230),
    "Suva": (-18.124809, 178.450079),
    "Port Moresby": (-9.443800, 147.180267)
}

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def init_db():
    conn = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        conn.cursor().executescript(f.read())
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    weather_data = {}
    for continent, cities in CAPITALS.items():
        for city in cities:
            latitude, longitude = COORDINATES[city]
            data = fetch_weather(latitude, longitude)
            if data:
                weather_data[city] = data
    return jsonify(weather_data)

def fetch_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('current_weather')
    else:
        return None

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
