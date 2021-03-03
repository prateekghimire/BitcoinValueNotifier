from plyer import notification
from bs4 import BeautifulSoup
import requests
import time

def BTCvalue():
    url='https://www.coindesk.com/price/bitcoin'
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "lxml")
    BTC=soup.find('div',attrs={'class':'price-large'}).text
    return BTC

BTC=BTCvalue()

notification.notify(title="Bitcoin Value",message=BTC,timeout=10)

BTCold=BTC

BTCold=(float(BTCold[1:].replace(',','')))

while True:
    BTCnew=BTCvalue()
    BTCnew=(float(BTCnew[1:].replace(',','')))

    print("****Looping****")

    print(BTCold)
    print(BTCnew)

    if(BTCold<BTCnew):
        message="Bitcoin Value Increased!!"
        print(message)
        notification.notify(title="Bitcoin Notification",message=message,timeout=3)
    elif(BTCold>BTCnew):
        message="Bitcoin Value Decreased!!"
        print(message)
        notification.notify(title="Bitcoin Notification",message=message,timeout=3)
    

    BTCold=BTCnew

    print("***SLEEPING***")
    time.sleep(5)
    print("***WAKING UP***")
    


