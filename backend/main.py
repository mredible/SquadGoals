from flask import Flask, request, jsonify
import pymysql

db = pymysql.connect("localhost", "root", "gordon64", "HackQuarantine")
#db = pymysql.connect("localhost", "username", "password", "database")

app = Flask(__name__)

@app.route('/')
def home():
    cursor = db.cursor()
    cursor.execute("select * from Users;")
    results = cursor.fetchall()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
