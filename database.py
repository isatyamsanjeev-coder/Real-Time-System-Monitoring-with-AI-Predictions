#1_database.py
import sqlite3
from datetime import datetime
import os
os.makedirs("data", exist_ok=True)

def create_table():
    conn = sqlite3.connect("data/metrics.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            timestamp TEXT,
            cpu REAL,
            memory REAL,
            disk REAL
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(cpu, memory, disk):
    conn = sqlite3.connect("data/metrics.db")
    c = conn.cursor()
    c.execute("INSERT INTO metrics VALUES (?, ?, ?, ?)",
            (datetime.now(), cpu, memory, disk))
    conn.commit()
    conn.close()