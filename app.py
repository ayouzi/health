from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_cors import cross_origin
from flask_mysqldb import MySQL

import employe

# import info
# import connDB

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "cardiodb"
mysql = MySQL(app)

# mysql = connDB.mysql
# infos = info.Info()


@app.route('/', methods=['Get'])
def index():
    return "Hello"


@app.route('/info', methods=['Get'])
def info():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from employe")
    UserData = cursor.fetchall()

    # payload = []
    # content = {}

    # for result in UserData:
    #     content = {
    #         "id"             : result[0],
    #         "first_name"     : result[1],
    #         "last_name"      : result[2],
    #         "email"          : result[3],
    #         "password"       : result[4],
    #         "address"        : result[5],
    #         "phone_number"   : result[6],
    #         "id_role"        : result[7],
    #         "created_at"     : result[8],
    #         "state"          : result[9],
    #     }

    #     payload.append(content)
    #     content = {}
    # return   jsonify(payload)
    return render_template("index.html", data=UserData)


@app.route("/delete/<string:id_user>", methods=['Get'])
def delete(id_user):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE from employe where id=%s", (id_user))
    cursor.connection.commit()
    flash("Suppression Employe reussi ")
    return redirect(url_for('info'))


@app.route("/insert", methods=['POST'])
def insert():
    if request.method == 'POST':
        nom = request.form["nom"]
        prenom = request.form["prenom"]
        email = request.form["email"]
        adresse = request.form["adresse"]
        password = request.form["password"]
        telephone = request.form["telephone"]
        role = request.form["role"]
        status = request.form["status"]

        cursor = mysql.connection.cursor()
        cursor.execute(""" 
                INSERT into employe 
                 (first_name,last_name,email,password,address,phone_number,id_role,state) 
                 VALUES 
                 (%s,%s,%s,%s,%s,%s,%s,%s)
            
            """, (nom, prenom, email, password, adresse, telephone, role, status))
        cursor.connection.commit()
        flash("Insert new  user is Successfuly")
        return redirect(url_for('info'))


@app.route("/update", methods=['POST'])
def update():
    if request.method == 'POST':
        user_id = request.form["user_id"]

        nom = request.form["nom"]
        prenom = request.form["prenom"]
        email = request.form["email"]
        adresse = request.form["adresse"]
        password = request.form["password"]
        telephone = request.form["telephone"]
        role = request.form["role"]
        status = request.form["status"]

        cursor = mysql.connection.cursor()
        cursor.execute("""
          UPDATE employe SET 
           first_name=%s, last_name=%s,email=%s,address=%s,password=%s,phone_number=%s,id_role=%s,state=%s
          WHERE id = %s """,
                       (nom, prenom, email, adresse, password, telephone, role, status, user_id))
        cursor.connection.commit()

        flash("Update Employe Successfuly")
        return redirect(url_for('info'))


# 33333333333333333333
# Employe
################

# API Select All Patient
@app.route('/patient', methods=['Get'])
def patient():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from patient")
    UserData = cursor.fetchall()

    payload = []
    content = {}

    for result in UserData:
        content = {
            "id": result[0],
            "codeClient": result[1],
            "image_path": result[2],
            "age": result[3],
            "gender": result[4],
            "last_name": result[5],
            "email": result[6],
            "address": result[7],
            "number_phone": result[8],
            "id_employe": result[9],
            "id_medecin": result[10],
            "created_at": result[11],
            "state": result[12],
        }

        payload.append(content)
        content = {}
    return jsonify(payload)
    # return render_template("index.html",data=UserData)


# API Insert new Patient
@app.route('/patient/add', methods=['POST'])
def patientAdd():
    if request.method == 'POST':
        codeClient      = request.form["codeClient"]
        image_path      = request.form["image_path"]
        age             = request.form["age"]
        gender          = request.form["gender"]
        last_name       = request.form["last_name"]
        email           = request.form["email"]
        address         = request.form["address"]
        number_phone    = request.form["number_phone"]
        id_employe      = request.form["id_employe"]
        id_medecin      = request.form["id_medecin"]
        status          = request.form["status"]

        cursor = mysql.connection.cursor()
        cursor.execute(""" 
                INSERT into patient 
                 (codeClient,image_path,age,gender,last_name,email,address,number_phone,id_employe,id_medecin,state) 
                 VALUES 
                 (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            
            """, (codeClient, image_path, int(age), int(gender), last_name, email, address, number_phone,int(id_employe),int(id_medecin),int(status)))
        cursor.connection.commit()
        # flash("Insert new  user is Successfuly")
        # return redirect(url_for('info'))

        return jsonify(200)


# API Edit  Patient
@app.route("/patient/edit", methods=['POST'])
def patientEdit():
    if request.method == 'POST':
        patient_id      = request.form["patient_id"]

        codeClient      = request.form["codeClient"]
        image_path      = request.form["image_path"]
        age             = request.form["age"]
        gender          = request.form["gender"]
        last_name       = request.form["last_name"]
        email           = request.form["email"]
        address         = request.form["address"]
        number_phone    = request.form["number_phone"]
        id_employe      = request.form["id_employe"]
        id_medecin      = request.form["id_medecin"]
        status          = request.form["status"]

        cursor = mysql.connection.cursor()
        cursor.execute("""
          UPDATE patient SET 
           codeClient=%s, image_path=%s,age=%s,gender=%s,last_name=%s,email=%s
           ,address=%s,number_phone=%s,id_employe=%s,id_medecin=%s,state=%s
          WHERE id = %s """,
           (codeClient, image_path, int(age), int(gender), last_name, email, address, number_phone,int(id_employe),int(id_medecin),int(status),patient_id))
        cursor.connection.commit()

        return jsonify(200)


# API Delete  Patient
@app.route("/patient/delete/<string:id_patient>", methods=['Get'])
def patientDelete(id_patient):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE from patient where id=%s", (id_patient))
    cursor.connection.commit()
    
    return jsonify(200)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
