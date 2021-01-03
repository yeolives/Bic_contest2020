import os 
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc
from matplotlib import style
%matplotlib auto
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
style.use('ggplot')


os.chdir('C:/Users/etotm/Desktop/bigcont')

train = pd.read_csv("final_train.csv",index_col=0)
train.일자 = pd.to_datetime(train.일자, format='%Y-%m-%d')

test = pd.read_csv("final_test_real.csv",index_col=0)
test = test.iloc[82:,]
test = test.drop_duplicates(test.columns)
test['게임키'] = test.일자.astype('str') + test.원정팀코드 + test.홈팀코드 + test.더블헤더코드.astype('str')

test2 = test.copy()
test.columns = ['일자', '상대팀코드', '팀코드', '요일', '구장', '더블헤더코드', '결과','게임키']
test2.columns = ['일자', '팀코드', '상대팀코드', '요일', '구장', '더블헤더코드', '결과','게임키']
test['home'] = 1
test2['home'] = 0
test2.결과 = test2[test2.결과.isnull()==False].결과.apply(lambda x : x.replace("W","L") if x =="W" else x.replace("L","W"))
test = pd.concat([test,test2],axis=0)
test.sort_values(by=['일자'], ascending=True, inplace=True)
test = test[['게임키','일자','팀코드','상대팀코드','요일', '구장', '더블헤더코드', '결과', 'home']]
test = test.reset_index(drop=True)
test.일자 = pd.to_datetime(test.일자, format='%Y%m%d')

test.to_csv('final_test.csv', encoding='euc_kr')


# 팀별나누고 arima예측한 값 붙이기
for i in test.팀코드.unique().tolist():
    globals()['te_{}'.format(i)] = test[(test.팀코드 == i)].reset_index(drop=True)

coll = ['득점권WHIP_Hptu1', '2점차이하WHIP_Hptu1', '345번타자WHIP_Hptu1', 'BABIP_Hptu1',
       '득점권WHIP_Hptu0', '2점차이하WHIP_Hptu0', '345번타자WHIP_Hptu0', 'BABIP_Hptu0',
       'SECA1_x', 'BABIP1_x', 'GPA1_x', 'RC1_x', 'XR1_x', 'wOBA1_x', 'ISO1_x',
       'EOBP1_x', 'SECA1_y', 'BABIP1_y', 'GPA1_y', 'RC1_y', 'XR1_y',
       'wOBA1_y', 'ISO1_y', 'EOBP1_y','SECAh_clean','BABIPh_clean', 'GPAh_clean', 'RCh_clean', 'XRh_clean', 'wOBAh_clean',
       'ISOh_clean', 'EOBPh_clean', 'SECAh_etc', 'BABIPh_etc', 'GPAh_etc','RCh_etc', 'XRh_etc', 'wOBAh_etc', 'ISOh_etc', 'EOBPh_etc']

coll_a = ['득점권WHIP_Aptu1', '2점차이하WHIP_Aptu1', '345번타자WHIP_Aptu1', 'BABIP_Aptu1',
       '득점권WHIP_Aptu0', '2점차이하WHIP_Aptu0', '345번타자WHIP_Aptu0', 'BABIP_Aptu0',
       'SECA2_x', 'BABIP2_x', 'GPA2_x', 'RC2_x', 'XR2_x', 'wOBA2_x', 'ISO2_x',
       'EOBP2_x', 'SECA2_y', 'BABIP2_y', 'GPA2_y', 'RC2_y', 'XR2_y',
       'wOBA2_y', 'ISO2_y', 'EOBP2_y','SECAa_clean','BABIPa_clean', 'GPAa_clean', 'RCa_clean', 'XRa_clean', 'wOBAa_clean',
       'ISOa_clean', 'EOBPa_clean', 'SECAa_etc', 'BABIPa_etc', 'GPAa_etc','RCa_etc', 'XRa_etc', 'wOBAa_etc', 'ISOa_etc', 'EOBPa_etc']

df_HH = pd.read_csv('HH1.csv', index_col=0).loc[:,coll]
df_HT = pd.read_csv('HT1.csv', index_col=0).loc[:,coll]
df_KT = pd.read_csv('KT1.csv', index_col=0).loc[:,coll]
df_LT = pd.read_csv('LT1.csv', index_col=0).loc[:,coll]
df_OB = pd.read_csv('OB1.csv', index_col=0).loc[:,coll]

df_LG = pd.read_csv('LG1.csv', index_col=0)
df_NC = pd.read_csv('NC1.csv', index_col=0)
df_SK = pd.read_csv('SK1.csv', index_col=0)
df_SS = pd.read_csv('SS1.csv', index_col=0)
df_WO = pd.read_csv('WO1.csv', index_col=0)


# arima변수 (홈기준) concat
te_HH = pd.concat([te_HH, df_HH.head(len(te_HH))], axis=1)
te_HT = pd.concat([te_HT, df_HT.head(len(te_HT))], axis=1)
te_KT = pd.concat([te_KT, df_KT.head(len(te_KT))], axis=1)
te_LG = pd.concat([te_LG, df_LG.head(len(te_LG))], axis=1)
te_LT = pd.concat([te_LT, df_LT.head(len(te_LT))], axis=1)
te_NC = pd.concat([te_NC, df_NC.head(len(te_NC))], axis=1)
te_OB = pd.concat([te_OB, df_OB.head(len(te_OB))], axis=1)
te_SK = pd.concat([te_SK, df_SK.head(len(te_SK))], axis=1)
te_SS = pd.concat([te_SS, df_SS.head(len(te_SS))], axis=1)
te_WO = pd.concat([te_WO, df_WO.head(len(te_WO))], axis=1)


total = pd.concat([te_HH,te_HT,te_KT,te_LG,te_LT,te_NC,te_OB,te_SK,te_SS,te_WO],axis=0)
total.sort_values(by=['게임키','일자'], ascending=True, inplace=True)
total = total.reset_index(drop=True)

def merge_final(df):
    
    a = pd.DataFrame()
    
    for i in range(len(df)):
        row = total[(total.게임키 == df.게임키[i]) & (total.팀코드 == df.상대팀코드[i])].loc[:,coll]
        a = a.append(row)
        
    a = a.reset_index(drop=True)
    a.columns = coll_a
    final = pd.concat([df,a],axis=1)
    return final


for i in ['te_HH','te_HT','te_KT','te_LG','te_LT','te_NC','te_OB','te_SK','te_SS','te_WO']:
    globals()['{}'.format(i)] = merge_final(globals()[i])
    #globals()['{}'.format(i[-2:])].to_csv('{}.csv'.format(i[-2:]),encoding="euc-kr")    

total = pd.concat([te_HH,te_HT,te_KT,te_LG,te_LT,te_NC,te_OB,te_SK,te_SS,te_WO],axis=0)

final = pd.concat([train,total],axis=0)
    

for i in final.팀코드.unique().tolist():
    globals()['final_{}'.format(i)] = final[(final.팀코드 == i)].reset_index(drop=True)


