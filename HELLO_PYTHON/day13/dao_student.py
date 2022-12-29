import psycopg2

class Daostudent():
    def __init__(self):
        self.conn = psycopg2.connect(host = "127.0.0.1", dbname = "Python", user = "postgres", password = "python")
        self.cur = self.conn.cursor()
    
    
    def selects(self):
        mydict = []
        self.cur.execute("select s_id, s_name, mobile, addr from student order by s_id")
        rows = self.cur.fetchall()
        for r in rows:
            mydict.append({'s_id' : r[0], 's_name' : r[1], 'mobile' : r[2], 'addr' : r[3]})
            
        return mydict
    
    
    def select(self, s_id):
        sql = f"""
            select
                s_id, s_name, mobile, addr
            from 
                student
            where
                s_id = '{s_id}'
        """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        r = rows[0]
        ret = {'s_id' : r[0], 's_name' : r[1], 'mobile' : r[2], 'addr' : r[3]}
        return ret
    
    
    def insert(self, s_id, s_name, mobile, addr):
        sql = f"""
            insert into student 
                    (s_id, s_name, mobile, addr) 
            values 
                ('{s_id}', '{s_name}', '{mobile}', '{addr}');
            """  
        self.cur.execute(sql)
        self.conn.commit()
        cnt = self.cur.rowcount
        return cnt

    
    def update(self, s_id, s_name, mobile, addr):
        sql = f"""
        update student
        set
            s_name = '{s_name}',
            mobile = '{mobile}',
            addr = '{addr}'
        where
            s_id = '{s_id}'
        """
        self.cur.execute(sql)
        self.conn.commit()
        cnt = self.cur.rowcount
        return cnt
    
    
    def delete(self, s_id):
        sql = f"""
        delete
        from  student
        where
            s_id = '{s_id}'
        """
        self.cur.execute(sql)
        self.conn.commit()
        cnt = self.cur.rowcount
        return cnt
    
    
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
        
if __name__ == '__main__':
    ds = Daostudent()
    sample = ds.select("1")
    print(sample)