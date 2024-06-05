import sqlite3
from datetime import datetime

def get_nearest_schedule():
    conn = sqlite3.connect('iot_dashboard.db')
    c = conn.cursor()
    
    # Lấy tất cả dữ liệu từ bảng shedules
    c.execute('SELECT * FROM shedules')
    schedules = c.fetchall()
    conn.close()
    
    # Chuyển đổi ngày hiện tại thành dạng datetime
    today = datetime.today()
    
    # Chuyển đổi ngày trong cơ sở dữ liệu thành dạng datetime và tìm ngày gần nhất
    nearest_schedule = None
    nearest_date_diff = float('inf')
    
    for schedule in schedules:
        schedule_date = datetime.strptime(schedule[2], '%d/%m/%Y')
        date_diff = (schedule_date - today).days
        
        if date_diff >= 0 and date_diff < nearest_date_diff:
            nearest_date_diff = date_diff
            nearest_schedule = schedule
    
    return nearest_schedule

print(get_nearest_schedule())