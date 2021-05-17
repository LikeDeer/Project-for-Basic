#coding:utf-8
#현금흐름표
import pandas as pd
import numpy as np

df = pd.read_csv('2020_1분기현금흐름표.csv')
df_except_row = df[(df['항목코드'] == 'ifrs-full_CashFlowsFromUsedInOperatingActivities') | (df['항목코드'] == 'dart_ProfitLossForStatementOfCashFlows') | (df['항목코드'] == 'ifrs-full_AdjustmentsForReconcileProfitLoss') | (df['항목코드'] == 'dart_CashAndCashEquivalentsAtBeginningOfPeriodCf') | (df['항목코드'] == 'dart_CashAndCashEquivalentsAtEndOfPeriodCf')]
df_print = df_except_row.iloc[:,[2, 3, 5, 7, 11, 12, 13, 14]]
df_print = df_print.fillna('0.0')
print(df_print)