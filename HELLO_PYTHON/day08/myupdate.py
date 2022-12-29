import psycopg2

col01 = '4'
col02 = '8'
col03 = '8'

conn = psycopg2.connect(host="127.0.0.1", dbname="Python", user="postgres", password="python")
cur = conn.cursor()

#f스트링은 파이썬 3.5버전 이상부터 돌아감

sql = f"""
    update sample
      set  col02='{col02}',
           col03='{col03}'
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

