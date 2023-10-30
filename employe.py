from flask import Flask,request,jsonify, render_template,redirect,url_for,flash
from flask_cors import cross_origin
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "cardiodb"
mysql = MySQL(app)

@app.route('/employe',methods=['Get'])
def info():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from employe")
    UserData = cursor.fetchall()

    payload = []
    content = {}

    for result in UserData:
        content = {
            "id"             : result[0],
            "first_name"     : result[1],
            "last_name"      : result[2],
            "email"          : result[3],
            "password"       : result[4],
            "address"        : result[5],
            "phone_number"   : result[6],
            "id_role"        : result[7],
            "created_at"     : result[8],
            "state"          : result[9],
        }

        payload.append(content)
        content = {}
    return   jsonify(payload)
    # return render_template("index.html",data=UserData)  


