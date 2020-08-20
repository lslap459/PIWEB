from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///namwonwoo.db' #'mysql://root:''@localhost/crud'
app.config['SQlALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee2(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    position = db.Column(db.String(100))
    email = db.Column(db.String(200))
    tel = db.Column(db.String(200))

    def __init__(self, username, position, email, tel):
        self.username = username
        self.position = position
        self.email = email
        self.tel = tel


@app.route('/')
def index():
    all_data = Employee2.query.order_by(Employee2.userid.desc()).all() # select * from employee
    return render_template("index.html", employee2=all_data)

@app.route("/insert", methods=['POST'])
def insert():
    if request.method == "POST":
        username = request.form["username"]
        position = request.form["position"]
        email = request.form["email"]
        tel = request.form["tel"]

        insertUser = Employee2(username,position,email,tel)
        db.session.add(insertUser)
        db.session.commit()

        return redirect(url_for('index'))

@app.route("/delete/<uid>")
def delete(uid):
    delUser = Employee2.query.get(uid)
    db.session.delete(delUser)
    db.session.commit()

    return redirect(url_for('index'))


@app.route("/update", methods=["POST"])
def update():
    if request.method == "POST":
        updateuser = Employee2.query.get(request.form.get('userid'))
        updateuser.username = request.form['username']
        updateuser.position = request.form['position']
        updateuser.email = request.form['email']
        updateuser.tel = request.form['tel']
        db.session.commit()
        return redirect(url_for('index'))

@app.route("/search", methods=["POST"])
def search():
    txtsearch = request.form['txtsearch']
    searchuser = Employee2.query.filter(Employee2.username.contains(txtsearch))
    return render_template("index.html", employee2=searchuser, txtsearch=txtsearch)