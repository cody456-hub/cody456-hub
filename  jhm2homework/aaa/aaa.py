import pandas as pd
import yfinance as yf

# 定义股票代码
ticker = 'SPY'

# 获取历史数据
data = yf.download(ticker, start='2020-01-01', end='2025-04-25')

# 将数据保存到 Excel 文件
data.to_excel('SPY_history.xlsx')