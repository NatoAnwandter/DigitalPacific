import MySQLdb
class DBHelper:
    def __init__(self):

        self.mydb = MySQLdb.connect(

            host        =   'localhost', 
            user        =   'root', 
            password    =   "",
            database    =   "bd_pacific",
            port = 3306

#            host        =   'Nato.mysql.pythonanywhere-services.com',
#            user        =   'Nato',
#            password    =   "administrador",
#            database    =   "Nato$default",

        )
    #Nombbre base de datos
    dbname = "bd_pacific"

    def select_user(self, room_name, username):
            cursor = self.mydb.cursor()
            query = "SELECT aru.sala_chat_id, au.username  from aplicaciones_sala_chat_users aru inner join aplicaciones_sala_chat ar on aru.sala_chat_id = ar.id inner join  aplicaciones_usuario au on aru .usuario_id = au.id   where ar.name = %s and au.username != %s"
            params = (room_name, username)
            cursor.execute(query, params)
            myresult = cursor.fetchall()
            #print(myresult)
            return myresult    

#Consulta preliminar mysql
# select aru.room_id, ar.name, aru.usuario_id, au.username  
# from aplicaciones_room_users aru 
# inner join aplicaciones_room ar
# on aru.room_id = ar.id
# inner join  aplicaciones_usuario au 
# on aru .usuario_id = au.id 
# where ar.name = "prueba1" and au.username != "fabian"           