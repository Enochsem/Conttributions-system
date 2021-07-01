from flask import Flask, render_template, url_for,  request, redirect, flash
from db import DB
from sms import SMS


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8zffhgf46@@]'

BENEFICIARY_1 = "0546353625"
BENEFICIARY_2 = "0203558351"
BENEFICIARY_3 = "0554317909"

TABLE_NAME = "contributor"

@app.route("/", methods=["POST","GET"])
def index():
    contributor_name = ""
    contributor_contact =""
    amount = ""
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
            send_sms(contributor_name, amount,contributor_contact, beneficiary,BENEFICIARY_1)
            send_sms1()
        elif beneficiary == "Ekow":
            send_sms(contributor_name, amount,contributor_contact, beneficiary,BENEFICIARY_2)
        elif beneficiary == "General Family":
            send_sms(contributor_name, amount,contributor_contact, beneficiary, BENEFICIARY_3)
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


def get_total(beneficiary):
    total = 0
    db = DB()
    data = db.select_where(TABLE_NAME, "beneficiary", beneficiary)
    lenght =len(data)
    print(data)
    for amount in range(len(data)):
        total += int(data[amount][3])
        print(total)
    return total

    
def send_sms(contributor_name, contributor_amount, contributor_contact, beneficiary_name, beneficiary_number):
    total_amount = get_total(beneficiary_name)
    message = "You have received {:,.2f}GHS from {} ({}). Your total balance is {:,.2f}GHS. Thank you".format(float(contributor_amount),contributor_name,contributor_contact,float(total_amount))
    recipient = BENEFICIARY_1
    sender = "Rev Nickel".upper()
    sms = SMS(contributor_amount, contributor_name, beneficiary_number, sender, message)
    sms.send()
    print("sent")

def send_sms1(contributor_name):
    message = "Dear {}, Your donation has been received. Very Rev. Evelyn Efua Nickel"
    recipient = contributor_contact
    sms = SMS(contributor_name,sender,message)
    sms.send()

# @app.route("/testplayground", methods = ["GET","POST"])
# def testplayground():
#     if request.method == "POST":
#         test = request.form["test"]
#         flash("button clicked on ")
#     return render_template("testplayground.html")



if __name__ == "__main__":
    app.run(debug = True)
    