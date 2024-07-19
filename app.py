import yfinance as yf
from datetime import timedelta
import datetime
from utils.tw import post_tweet

symbols = [
    'ALUA.BA', 'BBAR.BA', 'BMA.BA', 'BYMA.BA', 'CEPU.BA', 'COME.BA', 'CRES.BA', 'EDN.BA', 'GGAL.BA', 'HARG.BA', 'LOMA.BA', 'MIRG.BA', 'PAMP.BA', 'SUPV.BA', 'HAVA.BA', 'IRSA.BA', 'TECO2.BA', 'TGNO4.BA', 'TGSU2.BA', 'TRAN.BA', 'TXAR.BA', 'VALO.BA', 'YPFD.BA', 'AGRO.BA', 'ALUA.BA', 'AUSO.BA', 'BHIP.BA', 'BOLT.BA', 'BPAT.BA', 'CADO.BA',
    'CAPX.BA', 'CARC.BA', 'CECO2.BA', 'CELU.BA', 'CGPA2.BA', 'CTIO.BA', 'CVH.BA', 'DGCU2.BA', 'FERR.BA', 'FIPL.BA', 'GAMI.BA', 'GBAN.BA', 'GCDI.BA', 'GCLA.BA', 'AGRO.BA', 'INTR.BA', 'INVJ.BA', 'LEDE.BA', 'LONG.BA', 'METR.BA', 'MOLA.BA', 'MOLI.BA', 'MORI.BA', 'MTR.BA', 'OEST.BA', 'PATA.BA', 'POLL.BA', 'RICH.BA', 'ROSE.BA', 'SAMI.BA', 'SEMI.BA'
]

months = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

month = months[datetime.date.today().month]
day = datetime.date.today().day

def is_market_day():
    # Obtener el ticker de un símbolo cualquiera, por ejemplo, SPY (ETF S&P 500)
    ticker = yf.Ticker("^MERV")

    # Obtener los datos históricos del símbolo para hoy
    historical_data = ticker.history(
        start=datetime.date.today(), 
        end=datetime.date.today() + timedelta(days=1))

    # Verificar si hay datos para hoy
    if not historical_data.empty:
        return True
    else:
        return False


def get_merval_variance():
    ticker = yf.Ticker("^MERV")
    historical_data = ticker.history(
        start=datetime.date.today(), end=datetime.date.today() + timedelta(days=1))

    prevClose = round(ticker.get_info()['previousClose'], 2)
    currPrice = round(historical_data['Close'].iloc[0], 2)

    dif = round((currPrice - prevClose) / prevClose * 100, 2)
    
    post_tweet(f"La variación de precios de la mervaleta el dia {day} de {month} es del {dif}%")


def main():
    performances = []
    for symbol in symbols:
        ticker = yf.Ticker(symbol)
        prevClose = ticker.get_info()['previousClose']
        currPrice = ticker.get_info()['currentPrice']
        dif = round((currPrice - prevClose) / prevClose * 100, 2)

        performances.append({symbol: dif})

    performances.sort(key=lambda x: list(x.values())[0], reverse=True)

    best_performer = list(performances[0].keys())[0]
    best_performance = list(performances[0].values())[0]
    post_tweet(f"La acción estrella del {day} de {month} es:\n{best_performer} con un rendimiento de {best_performance}%")
    
    worst_performer = list(performances[-1].keys())[0]
    worst_performance = list(performances[-1].values())[0]
    post_tweet(f"La acción más golpeada del {day} de {month} es:\n{worst_performer} con un rendimiento de {worst_performance}%")

    worst_performers = "\n".join([f"{list(perf.keys())[0]} con un rendimiento de {list(perf.values())[0]}%" for perf in performances[-3:]])
    post_tweet(f"Las acciones con peor rendimiento el día de hoy {day} de {month} son:\n{worst_performers}")

    top_performers = "\n".join([f"{list(perf.keys())[0]} con un rendimiento de {list(perf.values())[0]}%" for perf in performances[:3]])
    post_tweet(f"Las acciones con mejor rendimiento el día de hoy {day} de {month} son:\n{top_performers}")

    get_merval_variance()

if __name__ == '__main__':
    if is_market_day():
        main()
        