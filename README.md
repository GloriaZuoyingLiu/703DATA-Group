# 703DATA-Group
pip install --index-url=https://bcms.bloomberg.com/pip/simple blpapi

from pandas_datareader 
import data import numpy as np
 
time_interval = ['2016-01-01','2020-12-31'] # subject to change later 
df = data.get_data_yahoo(['AMD','AAPL','NVDA','MSFT','TSLA','FB','PYPL','BABA','INTC','ATVI','TTD','CR 􏰀→= time_interval[0],end = time_interval[1])['Adj Close']
 
corr_mat = df.corr()
print(corr_mat)
  
np.fill_diagonal(corr_mat.values,np.nan)
adj_corr = corr_mat.abs()
s = adj_corr.unstack()
s1 = s.sort_values().dropna()
a = list(s1.idxmax())

new_data = data.get_data_yahoo([a[0],a[1]],start = time_interval[0],end =␣ 􏰀→time_interval[1])['Adj Close']
