import psycopg2

class DaoEmp():
    def __init__(self):
        self.conn = psycopg2.connect(host = "127.0.0.1", dbname = "Python", user = "postgres", password = "python")
        self.cur = self.conn.cursor()
    
    
    def selects(self):
        mydict = []
        self.cur.execute("select e_id, e_name, sex, addr from emp order by e_id")
        rows = self.cur.fetchall()
        for r in rows:
            mydict.append({'e_id' : r[0], 'e_name' : r[1], 'sex' : r[2], 'addr' : r[3]})
            
        return mydict
    
    
    def select(self, e_id):
        sql = f"""
            select
                e_id, e_name, sex, addr
            from 
                emp
            where
                e_id = '{e_id}'
        """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        r = rows[0]
        ret = {'e_id' : r[0], 'e_name' : r[1], 'sex' : r[2], 'addr' : r[3]}
        return ret
    
    
    def insert(self, e_id, e_name, sex, addr):
        sql = f"""
            insert into emp 
                    (e_id, e_name, sex, addr) 
            values 
                ('{e_id}', '{e_name}', '{sex}', '{addr}');
            """  
        self.cur.execute(sql)
        self.conn.commit()
        cnt = self.cur.rowcount
        return cnt

    
    def update(self, e_id, e_name, sex, addr):
        sql = f"""
        update emp
        set
            e_name = '{e_name}',
            sex = '{sex}',
            addr = '{addr}'
        where
            e_id = '{e_id}'
        """
        self.cur.execute(sql)
        self.conn.commit()
        cnt = self.cur.rowcount
        return cnt
    
    
    def delete(self, e_id):
        sql = f"""
        delete
        from  emp
        where
            e_id = '{e_id}'
        """
        self.cur.execute(sql)
        self.conn.commit()
        cnt = self.cur.rowcount
        return cnt
    
    
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
        
if __name__ == '__main__':
    ds = DaoEmp()
    sample = ds.select("1")
    print(sample)