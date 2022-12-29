import psycopg2

conn = psycopg2.connect(host="127.0.0.1", dbname="Python", user="postgres", password="python")

cur = conn.cursor()

cur.execute("select * from sample;")
rows = cur.fetchall()

print(rows)

cur.close()
conn.close()