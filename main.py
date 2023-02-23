import requests
import json
import time
from win10toast import ToastNotifier

def update():
    r=requests.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD,VND')
    data = r.json()["BTC"]
    
    text=f'USD: {data["USD"]} \tVND: {data["VND"]}'
    
    data2 = r.json()["ETH"]
    text2=f'USD: {data2["USD"]} \tVND: {data2["VND"]}'

    t=ToastNotifier()
    t.show_toast("Price","\nBTC\n"+ text + "\nETH\n" + text2,duration=20)
    
if __name__=="__main__":
    while True:
        update()
        time.sleep(30)