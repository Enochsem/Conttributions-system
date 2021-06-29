
class Contributor :
    def __init__(self,name, contact, amount):
        self.name = name
        self.contact = contact
        self.amount = amount


    def con(self,request):
        return Contributor(
            name = request.form["name"],
             contact = request.form["contact"] , 
             amount = request.form["amount"])