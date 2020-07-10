import sqlite3
from sqlite3 import Error

 
def select_events(event_id):
    conn = sqlite3.connect("../LETS-NullPointerException/db.sqlite3")

    cur = conn.cursor()
    cur.execute("SELECT name, time, text FROM articles_event WHERE id={}".format(event_id))
 
    return cur.fetchall()
