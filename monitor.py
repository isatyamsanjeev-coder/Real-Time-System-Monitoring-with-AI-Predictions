#2_monitor.py
import psutil
import time
from database import insert_data, create_table

create_table()   # Creating table first

def collect_metrics():
    return (
        psutil.cpu_percent(),
        psutil.virtual_memory().percent,
        psutil.disk_usage('/').percent
    )

while True:
    cpu, memory, disk = collect_metrics()
    insert_data(cpu, memory, disk)

    time.sleep(5)
