import psycopg2

conn = psycopg2.connect(host="127.0.0.1", dbname="Python", user="postgres", password="python")

cur = conn.cursor()

sql = """
    insert into sample
        (col01,col02,col03)
    values
        (3,3,3),
        (4,4,4)
"""

cur.execute(sql)
conn.commit()
count = cur.rowcount
print("count",count)


cur.execute("select * from sample;")
rows = cur.fetchall()

print(rows)

cur.close()
conn.close()

