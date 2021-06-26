import requests
import smtplib,ssl
import json
from win10toast import ToastNotifier

class CoinStatusCheck:

    def __init__(self):
        self.cont = ssl.create_default_context()
        self.toast = ToastNotifier()
        try:
            with open("input.json") as f:
                data = json.load(f)
                self.sendermail = data['sentmail']
                rm = data['receiver_email']
                self.recieved_mail = list(rm.split(","))
                self.password = data['password']
                self.url = data['url']
        except Exception as e:
            print(e)

    def invoke_service(self):
        try:
            res = requests.get(self.url)
            if res.status_code == 200:
                #print(res.text)
                self.send_mail()
                self.toast.show_toast("Hello....","You got notification", duration = 10)
            else:
                print('Call failled')
        except Exception as e:
            print(e)

    def send_mail(self):

        try:
            with smtplib.SMTP("smtp.gmail.com",port=587) as server:
                message = """\
                Subject: Hi there , Test email by angles
    
                This message is sent from Python."""
                server.ehlo()
                server.starttls(context=self.cont)
                server.ehlo()
                server.login(self.sendermail, self.password)
                server.sendmail(self.sendermail, self.recieved_mail, message)
                print('Message Sent...',self.recieved_mail,self.sendermail)

        except Exception as e:
            print('Exception',e)

if __name__ == '__main__':
    v = CoinStatusCheck()
    v.invoke_service()
    #invoke_service()
    #send_mail()