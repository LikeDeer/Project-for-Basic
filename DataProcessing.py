#coding:utf-8
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

def Jaemu():
    df = pd.read_csv('2020_1분기재무상태표.csv')
    df_except_row = df[(df['항목코드'] == 'ifrs-full_Assets') | (df['항목코드'] == 'ifrs-full_Equity')]
    df_print = df_except_row.loc[:,['회사명', '업종명', '결산기준일', '항목명', '당기 1분기말', '전기말']]
    jaemu = DataFrame(df_print)
    jaemu.to_csv('C:\\Users\\Asus\\Desktop\\2020 1분기 전처리 후파일\\2020_1분기_재무재표_전처리_후.csv')

def Jabon():
    df = pd.read_csv('2020_1분기자본변동표.csv')
    df_except_row = df[(df['항목코드'] == 'dart_EquityAtBeginningOfPeriod') | (df['항목코드'] == 'ifrs-full_Equity')]
    df_print = df_except_row.iloc[:,[2, 3, 5, 7, 11, 20]]
    df_print = df_print.fillna('0.0') #결측치를 대체하거나 제거하기 쉽지않아 일단 0.0으로 대체함. 아예 삭제하고싶은데 잘 안됨
    jabon = DataFrame(df_print)
    jabon.to_csv('C:\\Users\\Asus\\Desktop\\2020 1분기 전처리 후파일\\2020_1분기_자본변동표_전처리_후.csv')

def Sonik():
    df = pd.read_csv('2020_1분기포괄손익계산서.csv')
    df_except_row = df[(df['항목코드'] == 'ifrs-full_GrossProfit') | (df['항목코드'] == 'dart_OperatingIncomeLoss')  | (df['항목코드'] == 'ifrs-full_ProfitLoss') | (df['항목코드']== 'ifrs-full_ComprehensiveIncome')]
    #회사마다 index이름이 너무 다르다 문제가 생길 것 같음 카테고리 처리 하다가 말았는데 회사 지혼자 쓰는 항목코드도 있음
    df_print = df_except_row.iloc[:,[2, 3, 5, 7, 11, 12, 13, 14,15]]
    df_print = df_print.fillna('0.0')
    sonik= DataFrame(df_print)
    sonik.to_csv('C:\\Users\\Asus\\Desktop\\2020 1분기 전처리 후파일\\2020_1분기_포괄손익계산서_전처리_후.csv')

def Hungm():
    df = pd.read_csv('2020_1분기현금흐름표.csv')
    df_except_row = df[(df['항목코드'] == 'ifrs-full_CashFlowsFromUsedInOperatingActivities') | (df['항목코드'] == 'dart_ProfitLossForStatementOfCashFlows') | (df['항목코드'] == 'ifrs-full_AdjustmentsForReconcileProfitLoss') | (df['항목코드'] == 'dart_CashAndCashEquivalentsAtBeginningOfPeriodCf') | (df['항목코드'] == 'dart_CashAndCashEquivalentsAtEndOfPeriodCf')]
    df_print = df_except_row.iloc[:,[2, 3, 5, 7, 11, 12, 13, 14]]
    df_print = df_print.fillna('0.0')
    hungm = DataFrame(df_print)
    hungm.to_csv('C:\\Users\\Asus\\Desktop\\2020 1분기 전처리 후파일\\2020_1분기_현금흐름표_전처리_후.csv')

Jaemu()
Jabon()
Sonik()
Hungm()

