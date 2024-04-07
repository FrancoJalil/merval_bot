import yfinance as yf
# defining key/request url 

def main():    
    ticker = yf.Ticker("GGAL.BA")
    # requesting data from url 
    print("EMPIEZA")
    
    print(ticker.get_info()['currentPrice'])
    
    print("TERMINA")


if __name__ == '__main__':
    main()