import psycopg2

col01 = '4'

conn = psycopg2.connect(host="127.0.0.1", dbname="Python", user="postgres", password="python")
cur = conn.cursor()

#f스트링은 파이썬 3.5버전 이상부터 돌아감

sql = f"""
    delete from sample
    where  col01='{col01}'
        
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

