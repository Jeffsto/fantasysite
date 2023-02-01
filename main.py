from flask import Flask, render_template, request
import datafile
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__, static_folder='/static')
app.config['SECRET_KEY'] = datafile.storedkey
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{datafile.mysqladmin}:{datafile.mysqlpw}@{datafile.mysqlhost}:3306/{datafile.mysqldb}'
print(app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register/")
def register():
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True,host= '0.0.0.0',port=8888)
