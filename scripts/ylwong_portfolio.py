import pandas
import yfinance as yf
from matplotlib import * as plt

def trial():
    df = yf.download('0388.HK',start='2020-01-01',end='2026-08-27')
    print(df.head())


