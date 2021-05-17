#coding:utf-8
#자본변동표
import pandas as pd
import numpy as np

df = pd.read_csv('2020_1분기자본변동표.csv')
df_except_row = df[(df['항목코드'] == 'dart_EquityAtBeginningOfPeriod') | (df['항목코드'] == 'ifrs-full_Equity')]
df_print = df_except_row.iloc[:,[2, 3, 5, 7, 11, 20]]
df_print = df_print.fillna('0.0')
print(df_print)