from flask import jsonify
from flaskext .mysql import MySQL

class Model:

def __init__ ( self , app):
self .mysql = MySQL()
app.config[ ’MYSQL_DATABASE_USER’] = ’root’
app.config[ ’MYSQL_DATABASE_PASSWORD’] = ’xxxxx’
app.config[ ’MYSQL_DATABASE_DB’] = ’flaskmysql’
app.config[ ’MYSQL_DATABASE_HOST’] = ’127.0.0.1’
self .mysql.init_app(app)

self .conn = self.mysql.connect()
self .cursor = self .conn.cursor()