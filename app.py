from flask import Flask, render_template, url_for,  request, redirect
from db import DB
from sms import SMS


app = Flask(__name__)

BENEFICIARY_1 = "0546353625"
BENEFICIARY_2 = "0203558351"
BENEFICIARY_3 = "0554317909"

TABLE_NAME = "contributor"

@app.route("/", methods=["POST","GET"])
def index():
    contributor_name = ""
    amount = ""
    if request.method == "POST":
        db = DB()
        name = request.form["name"]
        contact = request.form["contact"]
        amount = request.form["amount"]
        beneficiary = request.form["beneficiary"]

        contributor_name = name

        db.insert(TABLE_NAME, "name", "contact", "amount", "beneficiary", name, contact, amount, beneficiary)
        
        if beneficiary == "BENEFICIARY_1":
            send_sms(contributor_name, amount, beneficiary,BENEFICIARY_1)
        elif beneficiary == "BENEFICIARY_2":
            send_sms(contributor_name, amount, beneficiary,BENEFICIARY_2)
        elif beneficiary == "BENEFICIARY_3":
            send_sms(contributor_name, amount, beneficiary, BENEFICIARY_3)

        return redirect(url_for("thanks"))

    return render_template("index.html")


# Funds




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
    
def send_sms(contributor_name, contributor_amount, beneficiary_name, beneficiary_number):
    total_amount = get_total(beneficiary_name)
    message = "You have received {}Ghs from {}. Your total balance is {}Ghs. Thank you".format(contributor_amount,contributor_name,total_amount)
    recipient = BENEFICIARY_1
    sender = "Funds"
    sms = SMS(contributor_amount, contributor_name, beneficiary_number, sender, message)
    sms.send()
    print("sent")


if __name__ == "__main__":
    app.run(debug = True)
    