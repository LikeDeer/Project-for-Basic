#coding:utf-8
#포괄손익계산서
import pandas as pd
import numpy as np

df = pd.read_csv('2020_1분기포괄손익계산서.csv')
df_except_row = df[(df['항목코드'] == 'ifrs-full_GrossProfit') | (df['항목코드'] == 'dart_OperatingIncomeLoss')  | (df['항목코드'] == 'ifrs-full_ProfitLoss') | (df['항목코드']== 'ifrs-full_ComprehensiveIncome')]
#회사마다 index이름이 너무 다르다 문제가 생길 것 같음 카테고리 처리 하다가 말았는데 회사 지혼자 쓰는 항목코드도 있음
df_print = df_except_row.iloc[:,[2, 3, 5, 7, 11, 12, 13, 14,15]]
df_print = df_print.fillna('0.0')
print(df_print)