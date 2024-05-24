from flask import Flask, render_template,  jsonify
import sqlite3

app = Flask(__name__)

def get_device_info():
    conn = sqlite3.connect('iot_dashboard.db')
    c = conn.cursor()
    c.execute('SELECT * FROM device_info ORDER BY id DESC LIMIT 1')
    device_info = c.fetchone()
    conn.close()
    return device_info

def get_notes():
    conn = sqlite3.connect('iot_dashboard.db')
    c = conn.cursor()
    c.execute('SELECT note FROM notes ORDER BY id DESC LIMIT 3')
    notes = c.fetchall()
    conn.close()
    return notes

# def get_schedules():
#     conn = sqlite3.connect('iot_dashboard.db')
#     c = conn.cursor()
#     c.execute('SELECT * FROM shedules ORDER BY id DESC LIMIT 1')
#     schedules = c.fetchall()
#     conn.close()
#     return schedules
def get_schedules():
    conn = sqlite3.connect('iot_dashboard.db')
    c = conn.cursor()
    c.execute('SELECT * FROM shedules ORDER BY id DESC LIMIT 1')
    schedules = c.fetchall()
    conn.close()
    return schedules

def get_media():
    conn = sqlite3.connect('iot_dashboard.db')
    c = conn.cursor()
    c.execute('SELECT * FROM media ORDER BY id DESC LIMIT 1')
    media = c.fetchall()
    conn.close()
    return media

def get_weather():
    conn = sqlite3.connect('iot_dashboard.db')
    c = conn.cursor()
    c.execute('SELECT * FROM weathers ORDER BY id DESC LIMIT 1')
    weather = c.fetchone()
    conn.close()
    return weather

@app.route('/')
def dashboard():
    device_info = get_device_info()
    notes = get_notes()
    schedules = get_schedules()
    media = get_media()
    weather = get_weather()

    context = {
        'device_info': device_info,
        'notes': [note[0] for note in notes],
        'schedules': schedules,
        'media': media,
        'weather': weather
    }
    return render_template('dashboard.html', **context)

@app.route('/api/schedules')
def api_schedules():
    schedules = get_schedules()
    schedule_list = []
    for schedule in schedules:
        schedule_dict = {
            'title': schedule[1],
            'start': f"{schedule[2]}T{schedule[3]}",
            'end': f"{schedule[2]}T{schedule[4]}"
        }
        schedule_list.append(schedule_dict)
    return jsonify(schedule_list)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
