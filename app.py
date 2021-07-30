from flask import Flask, render_template, url_for,  request, redirect, flash,session
from db import DB
from sms import SMS
from methods import *

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8zffhgf46@@]'

gideon = "0546353625"
ekow = "0203558351" 
augusta = "0243288066"
general_family = "0554317909"

TABLE_NAME = "contributor"



@app.route("/login",  methods = ["GET", "POST"])
def login():
    
    db = DB()
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        status = db.authentication("admin", "name", name, "password", password)
        
        if status == True:
            #set session and get admin name
            session['admin_name'] = name
            return redirect(url_for("index"))

    return render_template("appreciation.html")




@app.route("/", methods=["POST","GET"])
def index():
    
    admin_name = session.get("admin_name")

    if not session.get("admin_name"):
        return redirect(url_for("login"))


    contributor_name = ""
    contributor_contact =""

    amount = ""  #accumulator

    if request.method == "POST":
        db = DB()
        name = request.form["name"]
        contact = str(request.form["contact"])
        amount = str(request.form["amount"])
        beneficiary = request.form["beneficiary"]

        contributor_name = name
        contributor_contact = contact

        db.insert(TABLE_NAME, "name", "contact", "amount", "beneficiary","admin_name", name, contact, amount, beneficiary, admin_name)
        
        if beneficiary == "Gideon":
            beneficiary_sms(contributor_name, amount, contributor_contact, beneficiary, gideon)
            
        elif beneficiary == "Ekow":
            beneficiary_sms(contributor_name, amount, contributor_contact, beneficiary, ekow)

        elif beneficiary == "Augusta":
            beneficiary_sms(contributor_name, amount, contributor_contact, beneficiary, augusta)
        
        elif beneficiary == "General Family":
            beneficiary_sms(contributor_name, amount, contributor_contact, beneficiary, general_family)
        
        flash("Successful")
        return redirect(url_for("index"))

    return render_template("index.html",admin_name = admin_name)




@app.route("/admin", methods = ["GET", "POST"])
def admin():
    db = DB()
    contributors = db.select_all(TABLE_NAME)
    lenght = len(contributors)

    if request.method == "POST":
        db.delete_rows(TABLE_NAME)
        print("deleted")
    return render_template("admin.html", contributors = contributors, lenght = lenght)


@app.route("/thanks")
def thanks():
    return render_template("appreciation.html")




if __name__ == "__main__":
    app.run(debug = True)
    