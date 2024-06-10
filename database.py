import sqlite3

# Create a new SQLite database (or connect to an existing one)
conn = sqlite3.connect('iot_dashboard.db')
c = conn.cursor()

# Create a table device_info
c.execute('''
CREATE TABLE IF NOT EXISTS device_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    battery INTEGER,
    name TEXT,
    model TEXT,
    serial_num TEXT,
    hardware_revision TEXT,
    software_revision TEXT
)
''')

# Insert some sample data
c.execute('''
INSERT INTO device_info (battery, name, model, serial_num, hardware_revision, software_revision) 
VALUES (85, 'VOYD', 'White Mini', '000000000001', 'Rev A', 'Rev 1.00')
''')

# Create a table notes
c.execute('''
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    note TEXT
)
''')

# Insert some sample data to notes
c.execute('''
INSERT INTO notes (note) 
VALUES ('Go to the bank 1')
''')

# Insert some sample data to notes
c.execute('''
INSERT INTO notes (note) 
VALUES ('Go to the bank 2')
''')

# Insert some sample data to notes
c.execute('''
INSERT INTO notes (note) 
VALUES ('Go to the bank 3')
''')

# Insert some sample data to notes
c.execute('''
INSERT INTO notes (note) 
VALUES ('Go to the bank 4')
''')

# Create a table shedules
c.execute('''
CREATE TABLE IF NOT EXISTS shedules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shedule TEXT,
    date TEXT,
    start_time TEXT,
    end_time TEXT
)
''')

# Insert some sample data to shedules
c.execute('''
INSERT INTO shedules (shedule, date, start_time, end_time) VALUES ('Meeting with Lisa_2', '05/06/2024', '14:00', '14:00')
''')

# Create a table media
c.execute('''
CREATE TABLE IF NOT EXISTS media (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    media_type TEXT,
    media_data TEXT
)
''')

# Insert some sample data to media
c.execute('''
INSERT INTO media (media_type, media_data) 
VALUES ('image', '/home/chinhbui/Documents/voyd/web_flask/images/void_logo.png')
''')

# Create a table weathers
c.execute('''
CREATE TABLE IF NOT EXISTS weathers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature INTEGER,
    humidity INTEGER,
    weather TEXT,
    time TEXT,
    location TEXT,
    link TEXT
)
''')

# Insert some sample data to weathers
c.execute('''
INSERT INTO weathers (temperature, humidity, weather, time, location, link) 
VALUES ( 35, 85 , 'Sunny', '04/01/2024 17:04:22', 'New York, USA', 'https://voydofficial.com/')
''')

conn.commit()
conn.close()
