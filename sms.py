import requests 

class SMS :
    def __init__(self,recipient, sender,message):
        self.sender = sender
        self.recipient = recipient
        self.message = message
        self.url = "https://sms.arkesel.com/sms/api?action=send-sms"
        self.APIKEY = "OjVOOWgxb1VMbnVLY213QWY="


    def send (self):
        payload = {
            'api_key': self.APIKEY, 
            'to': self.recipient, 
            'from':self.sender,
            'sms':self.message
            }
        response = requests.get(self.url, params = payload)
        if response.status_code == 200:
            data = response.json()
            print(data)
        return data


if __name__ == "__main__":
    # pass
    sms = SMS("0554317909", "Me", "testing my contact")
    test = sms.send()
    print(test)






