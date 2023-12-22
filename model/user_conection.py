import psycopg

class UserConection():
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=fastapi_test user=postgres password=Javier host=localhost port=5432")
        except psycopg.OperationalError as err:    
            print(err)
            self.conn.close()
            
     # crud --> leer todos los datos
     
    def read_todo(self): # esta va a leer la db y la va a desplegar en la api
         with self.conn.cursor() as cur:
             data= cur.execute(""" SELECT * FROM "usuario"   """)
             return data.fetchall()
         
     # filtrar por solo una dato id
     # crud --> leer unico datos\
    def read_un_usuario(self, id):
        with  self.conn.cursor() as cursor:
            data=cursor.execute(""" SELECT * FROM "usuario" WHERE id= %s  """,(id,))
            return data.fetchone()
        
        
        # crud --> escribir datos 
    def write(self, data):#para escribir datos en nuestra bd
         with self.conn.cursor() as cursor: #crea un contexto de coneccion a la bd y cierra la conexion
             cursor.execute("""INSERT INTO "usuario"(name,phone) VALUES(%(name)s, %(phone)s)""", data)
             self.conn.commit() # confirmar la intro de esos datos
             
             
       # crud --> eliminar datos
    def delete_usuario (self, id):   
        with self.conn.cursor() as cur:
            cur.execute(""" DELETE FROM "usuario" WHERE id = %s""",(id,))
            self.conn.commit() 
      
      # crud --> actualizar datos      
    def actualizar_usuario(self, data):
        with self.conn.cursor() as cursor:
            cursor.execute("""  
                           UPDATE "usuario" 
                           SET name =%(name)s, phone=%(phone)s 
                           WHERE id=%(id)s
                           """,data)  
            self.conn.commit()
     
  #desctructor , cierra la conexion a la base         
    def __def__(self):
        self.conn.close()       
