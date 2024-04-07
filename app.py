import json 
import requests 
# defining key/request url 
key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

def main():    
    # requesting data from url 
    data = requests.get(key)   
    data = data.json() 
    print("EMPIEZA")
    print(f"{data['symbol']} price is {data['price']}") 
    print("TERMINA")


if __name__ == '__main__':
    main()