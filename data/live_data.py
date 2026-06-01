import yfinance as yf


def get_nifty_data():

    nifty = yf.Ticker("^NSEI")

    hist = nifty.history(period="5d")

    return hist
