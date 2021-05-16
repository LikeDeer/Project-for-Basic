#coding:utf-8
#�ڻ��Ѱ�� �ں��Ѱ踸 dataframe���� ��Ÿ �� �����Դϴ�.
import pandas as pd

df = pd.read_csv('2020_1분기재무상태표.csv')
df_except_row = df[(df['항목코드'] == 'ifrs-full_Assets') | (df['항목코드'] == 'ifrs-full_Equity')]
df_print = df_except_row.loc[:,['회사명', '업종명', '결산기준일', '항목명', '당기 1분기말', '전기말']]
print(df_except_row)