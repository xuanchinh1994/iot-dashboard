from flask import Flask, render_template,  jsonify
import sqlite3
from datetime import datetime

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

def get_schedules():
    conn = sqlite3.connect('iot_dashboard.db')
    c = conn.cursor()
    
    # Fetch all schedules
    c.execute('SELECT * FROM shedules')
    all_schedules = c.fetchall()
    conn.close()
    
    # Convert current date to datetime object
    current_date = datetime.now().strftime('%d/%m/%Y')
    current_date = datetime.strptime(current_date, '%d/%m/%Y')
    
    # Initialize variables to track the nearest schedules
    future_schedules = []
    nearest_past_schedule = None
    min_past_diff = None
    
    for schedule in all_schedules:
        schedule_date = datetime.strptime(schedule[2], '%d/%m/%Y')
        diff = (schedule_date - current_date).days
        
        # Check if the schedule is on or after the current date
        if diff >= 0:
            future_schedules.append((diff, schedule))
        else:
            # Check if the schedule is before the current date
            diff = abs(diff)
            if min_past_diff is None or diff < min_past_diff:
                nearest_past_schedule = schedule
                min_past_diff = diff
    
    # Sort the future schedules by date difference
    future_schedules.sort()
    
    # Get 5 nearest future schedules, if available
    nearest_future_schedules = [fs[1] for fs in future_schedules[:5]]
    
    # Prefer future schedules, but fallback to past if no future found
    if nearest_future_schedules:
        return nearest_future_schedules
    elif nearest_past_schedule:
        return [nearest_past_schedule]
    else:
        return []

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

    now = datetime.now()
    time_str = now.strftime("%I:%M %p")
    date_str = now.strftime("%A, %d %B %Y")

    return render_template('dashboard.html', **context, time_str=time_str, date_str=date_str)

@app.route('/api/latest-schedules')
def api_latest_schedules():
    schedules = get_schedules()
    schedule_list = []
    for schedule in schedules:
        schedule_dict = {
            'id': schedule[0],
            'shedule': schedule[1],
            'date': schedule[2],
            'start_time': schedule[3],
            'end_time': schedule[4]
        }
        schedule_list.append(schedule_dict)
    return jsonify(schedule_list)

@app.route('/api/latest-weather')
def api_latest_weather():
    weathers = get_weather()
    weather_list = []
    for weather in weathers:
        weather_dict = {
            'id': weather[0],
            'temperature': weather[1],
            'humidity': weather[2],
            'weather': weather[3],
            'time': weather[4],
            'city': weather[5]
        }
        weather_list.append(weather_dict)
    return jsonify(weather_list)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
