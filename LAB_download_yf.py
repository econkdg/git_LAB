# ====================================================================================================
# download yf
# ====================================================================================================
# import library

import datetime
import pandas_datareader as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
import os
import yfinance as yf
import FinanceDataReader as fdr
# ----------------------------------------------------------------------------------------------------
# download yf


class yf_data:

    def __init__(self, code, start, end):

        self.code = code
        self.start = start
        self.end = end

    def yf_download_simple(self):

        raw_data = yf.download(self.code, start=self.start, end=self.end)
        data = pd.DataFrame(raw_data)

        save = data.to_excel(excel_writer='data.xlsx', encoding='cp949')

        return save

        # data.to_excel(excel_writer='self.code_data.xlsx') -> absolute path

    def yf_plot(self):

        raw_data = yf.download(self.code, start=self.start, end=self.end)
        data = pd.DataFrame(raw_data)

        column_name = ['Open', 'Low', 'High', 'Close', 'Adj Close', 'Volume']

        for i in range(6):

            data[column_name[i]].plot()

            plt.title('{} plot'.format(column_name[i]), fontsize=15)
            plt.xlabel('date', fontsize=15)
            plt.grid(alpha=0.3)

            fig = plt.show()

        return fig


firm = [yf_data('AAPL', '2020-01-01', '2020-12-31')]
# ====================================================================================================
