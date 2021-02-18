import psycopg3

conn = psycopg3.connect(CONNINFO)
cur = conn.cursor()
cur.execute("SELECT * FROM table")
print(cur.fetchall())
cur.close()
conn.close()
