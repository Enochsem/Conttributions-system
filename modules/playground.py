import requests 

class SMS :
    def __init__(self,recipient, sender,message):
        self.sender = sender
        self.recipient = recipient
        self.message = message
        self.url = "https://sms.arkesel.com/sms/api?action=send-sms"
        self.APIKEY = "OjVOOWgxb1VMbnVLY213QWY="
        self.payload = {'api_key': self.APIKEY, 'to': self.recipient, 'from':self.sender,'sms':self.message}


    def send (self):
        response = requests.get(self.url, params=self.payload)
        if response.status_code == requests.codes.ok:
            data = response.json()
            print(data)
        return data

    def sms_response (self,data):
        print(data)

    def get_balance(self):
        data = self.send()
        if data != "":
            balance = data["main_balance"]
        return balance

    def alert(self):
        balance = self.get_balance()
        if balance <= 0.023:
            print(topup)
            #send aler message to family to top-up








