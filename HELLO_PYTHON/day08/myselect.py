import psycopg2, pprint


class myselect():
    
    def __init__(self):
        self.db = psycopg2.connect(host='localhost', dbname='Python',user='postgres',password='python',port=5432)
        self.cursor=self.db.cursor()
        
    def __del__(self):
        self.db.close()
        self.cursor.close()    
        
    def execute(self,query,args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchall()
        return row
    
    def commit(self):
        self.cursor.commit()
        
    def readDB(self):
        self.cursor.execute("SELECT * FROM sample")
        result=self.cursor.fetchall()
        print(result)
