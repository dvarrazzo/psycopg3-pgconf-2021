import psycopg2

conn = psycopg2.connect(CONNINFO)
cur = conn.cursor()
cur.execute("SELECT * FROM table")
print(cur.fetchall())
cur.close()
conn.close()
