from flask import Flask, json, Response, request, render_template
from werkzeug.utils import secure_filename
from os import path, getcwd
import time
from db import Database
# from face import Face
from handle import Handle
from bottle import run

app = Flask(__name__)


app.db = Database()
app.handle = Handle()
app.request = request

@app.route('/', methods=['GET'])
def home():
    output = json.dumps({'API V':'1.0'})
    return app.handle.success(output)

@app.route('/users', methods=['GET'])
def users():
    users = app.db.select('select * from users')
    lstUsers = []
    for user in users:
        lstUsers.append({'id':user[0], 'name':user[1],'email':user[2], 'created_at':user[3]})
    output = json.dumps(lstUsers)
    return app.handle.success(output)


@app.route("/users/<int:user_id>", methods=['GET'])
def user(user_id):
    # data = request.args.to_dict()
    # print('cheguei',data)
    user_id = int(user_id)
    result = app.db.select('SELECT * FROM users WHERE user_id = ?',[user_id])
    user = {}
    for row in result:
        user = {
            "id": row[0],
            "user_id": row[1],
            "filename": row[2],
            "created": row[3],
        }
    output = json.dumps(user)
    return app.handle.success(output)

@app.route("/users/<int:user_id>", methods=['DELETE'])
def deleteUser(user_id):
    # data = request.args.to_dict()
    # print('cheguei',data)
    user_id = int(user_id)
    app.db.select('DELETE FROM users WHERE user_id = ?',[user_id])
    output = json.dumps({'msg':'Registro excluido com sucesso!!!','status':True})
    return app.handle.success(output)

@app.route('/users', methods=['POST'])
def save():
    name = app.request.form['name']
    email = app.request.form['email']
    created_at = int(time.time())
    user_id = app.db.insert('INSERT INTO users(name, email, created_at) values(?, ?, ?)', [name, email, created_at])
    if user_id:
        output = json.dumps({'msg': 'Registro salvo com sucesso', 'status': True})
    else:
        output = json.dumps({'msg': 'Erro ao salvar registro', 'status': False})

    return app.handle.success(output)

# run(reloader=True)

app.run()
