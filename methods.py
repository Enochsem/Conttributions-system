from db import DB
from sms import SMS

TABLE_NAME = "contributor"


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

    
def beneficiary_sms(contributor_name, contributor_amount, contributor_contact, beneficiary_name, beneficiary_number):

    total_amount = get_total(beneficiary_name)

    recipient = beneficiary_number
    sender = "hello".upper()  #Rev Nickel
    message = """
    You have received {:,.2f}GHS 
    from {} ({}). 
    Your total balance is {:,.2f}GHS. 
    Thank you
    """.format(float(contributor_amount),contributor_name,contributor_contact,float(total_amount))
    
    sms = SMS(recipient, sender, message)
    sms.send()

    print("sent")


