from flask import Flask, render_template, url_for,  request, redirect, flash
from db import DB
from sms import SMS
from methods import *

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8zffhgf46@@]'

gideon = "0546353625"
ekow = "0203558351"
general_family = "0554317909"

TABLE_NAME = "contributor"

@app.route("/", methods=["POST","GET"])
def index():

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

        db.insert(TABLE_NAME, "name", "contact", "amount", "beneficiary", name, contact, amount, beneficiary)
        
        if beneficiary == "Gideon":
            beneficiary_sms(contributor_name, amount, contributor_contact, beneficiary, gideon)
            
        elif beneficiary == "Ekow":
            beneficiary_sms(contributor_name, amount, contributor_contact, beneficiary, ekow)
        
        elif beneficiary == "General Family":
            beneficiary_sms(contributor_name, amount, contributor_contact, beneficiary, general_family)
        
        flash("Successful")
        return redirect(url_for("index"))

    return render_template("index.html")




@app.route("/admin")
def admin():
    db = DB()
    contributors = db.select_all(TABLE_NAME)
    lenght = len(contributors)
    return render_template("admin.html", contributors = contributors, lenght = lenght)


@app.route("/thanks")
def thanks():
    return render_template("appreciation.html")




if __name__ == "__main__":
    app.run(debug = True)
    