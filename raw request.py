to = "0554317909"
comingFrom = "Funds"
api_key = "OnhkSzhGTWVwaWtnUENlYWs="

total ="40"
amount = "20"
contributor = "sem"
message = "You have received {}Ghs from {}. Your total balance is {}Ghs. Thank you".format(amount,contributor,total)

url = "https://sms.arkesel.com/sms/api?action=send-sms"
payload = {'api_key': api_key, 'to': to, 'from':comingFrom,'sms':message}
response = requests.get(url, params=payload)
if response.status_code == 200:
    print(response.json())



    # {'code': 'ok', 'message': 'Successfully Sent', 'balance': 7, 'main_balance': 0.17400000000000002, 'user': 'Enoch Sem'}
    # {'code': '112', 'message': 'Sender ID should be less than 11 characters'}

# {'code': 'ok', 'message': 'Successfully Sent', 'balance': 6, 'main_balance': 0.17400000000000002, 'user': 'Enoch Sem'}