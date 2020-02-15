from flask import Flask,render_template
app = Flask(__name__)
import csv

@app.route('/')
def home():
    return render_template("./index.html")



@app.route('/submit_form',methods = ['POST','GET'])
def submit_form():
    if request.method="POST":
        data = request.form.todict()
     else:
        return "Something went wrong"   


def write_to_file(data):
    with open("database.py",mode="a") as database:
        name = data["name"]
        email = data["email"] 
        subject = data["subject"]
        message = data["message"]
