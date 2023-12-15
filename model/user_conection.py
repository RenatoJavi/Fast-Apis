import psycopg

class UserConection():
    conn = None
    def __init(self):
        try:
            self.conn = psycopg.connect("dbname=fastapi_test user=postgres password=Javier host=localhost port=5432")
        except psycopg.OperationalError as err:    
            print(err)
            self.conn.close()
            
            
def __def__(self):
    self.conn.close()       