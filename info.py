from connDB import mysql

class Info:
    #def __init__(self):
       # self.cursor = mysql.connect().cursor()

    def getInfo(self):
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from users")

        UserData = cursor.fetchall()

        payload = []
        content = {}

        for result in UserData:
            content = {
                "id"       : result[0],
                "name"     : result[1],
                "email"    : result[2],
                "password" : result[3],
                "state"    : result[4],
            }

            payload.append(content)
            content = {}
            
        return payload