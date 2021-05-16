#coding:utf-8
#재무상태표
import pandas as pd
import numpy as np

df = pd.read_csv('2020_1분기자본변동표.csv')
df_except_row = df[(df['항목코드'] == 'dart_EquityAtBeginningOfPeriod') | (df['항목코드'] == 'ifrs-full_Equity')]
df_print = df_except_row.loc[:,['회사명', '업종명', '결산기준일', '항목명', '자본']]
df_print = df_print.dropna(axis=1)
print(df_print)