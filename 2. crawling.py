##크롤링 for testset , validationset 구축
import os
import re
import requests
#!pip install bs4
#!pip install selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import numpy as np
import pandas as pd


os.chdir('C:/Users/etotm/Desktop/bigcont')

for n in ['07','08', '09']:
    for i in ['OB', 'WO', 'SK', 'LG', 'NC', 'KT', 'HT', 'SS', 'HH','LT']:
        browser = webdriver.Chrome("./chromedriver")
        browser.get("https://sports.news.naver.com/kbaseball/schedule/index.nhn?date=20200923&month="+ str(n) +"&year=2020&teamCode="+str(i))
        globals()['crawl{}_{}'.format(n,i)] = [browser.find_elements_by_css_selector("div.sch_tb")[j].text 
                                           for j in range(len(browser.find_elements_by_css_selector("div.sch_tb")))]
        globals()['crawl{}_{}2'.format(n,i)] = [browser.find_elements_by_css_selector("div.sch_tb2")[j].text 
                                           for j in range(len(browser.find_elements_by_css_selector("div.sch_tb2")))]
        browser.quit()

crawl07_HH = crawl07_HH+crawl07_HH2
crawl07_HT = crawl07_HT+crawl07_HT2
crawl07_LT = crawl07_LT+crawl07_LT2
crawl07_NC = crawl07_NC+crawl07_NC2
crawl07_OB = crawl07_OB+crawl07_OB2
crawl07_LG = crawl07_LG+crawl07_LG2
crawl07_SS = crawl07_SS+crawl07_SS2
crawl07_WO = crawl07_WO+crawl07_WO2
crawl07_KT = crawl07_KT+crawl07_KT2
crawl07_SK = crawl07_SK+crawl07_SK2

crawl08_HH = crawl08_HH+crawl08_HH2
crawl08_HT = crawl08_HT+crawl08_HT2
crawl08_LT = crawl08_LT+crawl08_LT2
crawl08_NC = crawl08_NC+crawl08_NC2
crawl08_OB = crawl08_OB+crawl08_OB2
crawl08_LG = crawl08_LG+crawl08_LG2
crawl08_SS = crawl08_SS+crawl08_SS2
crawl08_WO = crawl08_WO+crawl08_WO2
crawl08_KT = crawl08_KT+crawl08_KT2
crawl08_SK = crawl08_SK+crawl08_SK2

crawl09_HH = crawl09_HH+crawl09_HH2
crawl09_HT = crawl09_HT+crawl09_HT2
crawl09_LT = crawl09_LT+crawl09_LT2
crawl09_NC = crawl09_NC+crawl09_NC2
crawl09_OB = crawl09_OB+crawl09_OB2
crawl09_LG = crawl09_LG+crawl09_LG2
crawl09_SS = crawl09_SS+crawl09_SS2
crawl09_WO = crawl09_WO+crawl09_WO2
crawl09_KT = crawl09_KT+crawl09_KT2
crawl09_SK = crawl09_SK+crawl09_SK2


crawl_df = np.array([crawl07_HH+crawl07_HT+crawl07_KT+crawl07_LG+crawl07_LT+crawl07_NC+crawl07_OB+crawl07_SK+crawl07_SS+crawl07_WO+
            crawl08_HH+crawl08_HT+crawl08_KT+crawl08_LG+crawl08_LT+crawl08_NC+crawl08_OB+crawl08_SK+crawl08_SS+crawl08_WO+
            crawl09_HH+crawl09_HT+crawl09_KT+crawl09_LG+crawl09_LT+crawl09_NC+crawl09_OB+crawl09_SK+crawl09_SS+crawl09_WO])

for c in crawl_df:
    for i in range(len(c)):
        c[i] = c[i].replace('\n', ' ')

crawl_df = crawl_df.reshape((920,1))
crawl_df = pd.DataFrame(crawl_df)


ind = []
for i in range(len(crawl_df)):
    if ('취소' in crawl_df[0][i]) or ('없습니다' in crawl_df[0][i]): 
        ind.append(i)

crawl_df.drop(ind , axis=0, inplace= True)
crawl_df = crawl_df.reset_index(drop=True)


for i in range(len(crawl_df)):
    crawl_df[0][i] = crawl_df[0][i].replace('MBC SPORTS+','').replace('SBS SPORTS','')\
        .replace('KBS N SPORTS','').replace('SPOTV2','').replace('SPOTV','').replace('업데이트 예정','')\
            .replace('KBS2', '').replace('(', '').replace(')', '').replace(',', '').replace('    ', ' ')\
                .replace('  ', ' ').replace('   ', ' ').replace('  ', ' ')

for i in range(len(crawl_df)):
    crawl_df[0][i] = crawl_df[0][i].split(' ')



test = pd.DataFrame(columns = ['일자', '원정팀코드', '홈팀코드', '요일','구장', '더블헤더코드', '결과'])

date = []
day = []
away = []
home =[]
stadium = []
result = []

for i in range(len(crawl_df)):
    date.append(crawl_df[0][i][0])
    day.append(crawl_df[0][i][1])
    away.append(crawl_df[0][i][3])
    home.append(crawl_df[0][i][5])
    stadium.append(crawl_df[0][i][6])
    result.append(crawl_df[0][i][4])

test['일자'] = date
test['요일'] = day
test['원정팀코드'] = away
test['홈팀코드'] = home
test['구장'] = stadium
test['더블헤더코드'] = 0
test['결과'] = result

test = test.append(pd.DataFrame(np.zeros((14,7)), columns = ['일자', '원정팀코드', '홈팀코드', '요일','구장', '더블헤더코드', '결과'])).reset_index(drop=True)

test['일자'][710] = crawl_df[0][276][0]
test['요일'][710] = crawl_df[0][276][1]
test['원정팀코드'][710] = crawl_df[0][276][8]
test['홈팀코드'][710] = crawl_df[0][276][10]
test['구장'][710] = crawl_df[0][276][11]
test['더블헤더코드'][710] += 1 
test['결과'][710] = crawl_df[0][276][9]        


test['일자'][711] = crawl_df[0][298][0]
test['요일'][711] = crawl_df[0][298][1]
test['원정팀코드'][711] = crawl_df[0][298][8]
test['홈팀코드'][711] = crawl_df[0][298][10]
test['구장'][711] = crawl_df[0][298][11]
test['더블헤더코드'][711] += 1 
test['결과'][711] = crawl_df[0][298][9]


test['일자'][712] = crawl_df[0][322][0]
test['요일'][712] = crawl_df[0][322][1]
test['원정팀코드'][712] = crawl_df[0][322][8]
test['홈팀코드'][712] = crawl_df[0][322][10]
test['구장'][712] = crawl_df[0][322][11]
test['더블헤더코드'][712] += 1
test['결과'][712] = crawl_df[0][322][9]


test['일자'][713] = crawl_df[0][392][0]
test['요일'][713] = crawl_df[0][392][1]
test['원정팀코드'][713] = crawl_df[0][392][8]
test['홈팀코드'][713] = crawl_df[0][392][10]
test['구장'][713] = crawl_df[0][392][11]
test['더블헤더코드'][713] += 1
test['결과'][713] = crawl_df[0][392][9]


test['일자'][714] = crawl_df[0][469][0]
test['요일'][714] = crawl_df[0][469][1]
test['원정팀코드'][714] = crawl_df[0][469][8]
test['홈팀코드'][714] = crawl_df[0][469][10]
test['구장'][714] = crawl_df[0][469][11]
test['더블헤더코드'][714] += 1
test['결과'][714] = crawl_df[0][469][9]


test['일자'][715] = crawl_df[0][502][0]
test['요일'][715] = crawl_df[0][502][1]
test['원정팀코드'][715] = crawl_df[0][502][8]
test['홈팀코드'][715] = crawl_df[0][502][10]
test['구장'][715] = crawl_df[0][502][11]
test['더블헤더코드'][715] += 1
test['결과'][715] = crawl_df[0][502][9]


test['일자'][716] = crawl_df[0][527][0]
test['요일'][716] = crawl_df[0][527][1]
test['원정팀코드'][716] = crawl_df[0][527][8]
test['홈팀코드'][716] = crawl_df[0][527][10]
test['구장'][716] = crawl_df[0][527][11]
test['더블헤더코드'][716] += 1
test['결과'][716] = crawl_df[0][527][9]


test['일자'][717] = crawl_df[0][576][0]
test['요일'][717] = crawl_df[0][576][1]
test['원정팀코드'][717] = crawl_df[0][576][8]
test['홈팀코드'][717] = crawl_df[0][576][10]
test['구장'][717] = crawl_df[0][576][11]
test['더블헤더코드'][717] += 1 
test['결과'][717] = crawl_df[0][576][9]

test['일자'][718] = crawl_df[0][583][0]
test['요일'][718] = crawl_df[0][583][1]
test['원정팀코드'][718] = crawl_df[0][583][8]
test['홈팀코드'][718] = crawl_df[0][583][10]
test['구장'][718] = crawl_df[0][583][11]
test['더블헤더코드'][718] += 1 
test['결과'][718] = crawl_df[0][583][9]

test['일자'][719] = crawl_df[0][607][0]
test['요일'][719] = crawl_df[0][607][1]
test['원정팀코드'][719] = crawl_df[0][607][8]
test['홈팀코드'][719] = crawl_df[0][607][10]
test['구장'][719] = crawl_df[0][607][11]
test['더블헤더코드'][719] += 1 
test['결과'][719] = crawl_df[0][607][9]


test['일자'][720] = crawl_df[0][622][0]
test['요일'][720] = crawl_df[0][622][1]
test['원정팀코드'][720] = crawl_df[0][622][8]
test['홈팀코드'][720] = crawl_df[0][622][10]
test['구장'][720] = crawl_df[0][622][11]
test['더블헤더코드'][720] += 1 
test['결과'][720] = crawl_df[0][622][9]


test['일자'][721] = crawl_df[0][649][0]
test['요일'][721] = crawl_df[0][649][1]
test['원정팀코드'][721] = crawl_df[0][649][8]
test['홈팀코드'][721] = crawl_df[0][649][10]
test['구장'][721] = crawl_df[0][649][11]
test['더블헤더코드'][721] += 1 
test['결과'][721] = crawl_df[0][649][9]


test['일자'][722] = crawl_df[0][663][0]
test['요일'][722] = crawl_df[0][663][1]
test['원정팀코드'][722] = crawl_df[0][663][8]
test['홈팀코드'][722] = crawl_df[0][663][10]
test['구장'][722] = crawl_df[0][663][11]
test['더블헤더코드'][722] += 1 
test['결과'][722] = crawl_df[0][663][9]


test['일자'][723] = crawl_df[0][695][0]
test['요일'][723] = crawl_df[0][695][1]
test['원정팀코드'][723] = crawl_df[0][695][8]
test['홈팀코드'][723] = crawl_df[0][695][10]
test['구장'][723] = crawl_df[0][695][11]
test['더블헤더코드'][723] += 1 
test['결과'][723] = crawl_df[0][695][9]

test = test.drop_duplicates()

# 일자전처리
test.일자 = pd.to_datetime(test.일자, format='%m.%d')
test.일자 =test.일자.astype('str').apply(lambda x: str(x)[-5:])
test.일자 =test.일자.apply(lambda x: x.replace('-',""))
test.일자 = '2020' + test.일자 
test = test.reset_index(drop=True)

# 승패전처리
test.loc[test.결과 == 'VS', '결과'] = '0'

test['결과']

for i in range(len(test)):
    if test['결과'][i] != '0':
        test['결과'][i] = test['결과'][i].split(':')
    else: 
        pass

for i in range(len(test)):
    if test['결과'][i] != '0':
        if int(test['결과'][i][0]) > int(test['결과'][i][1]):
            test['결과'][i] = 'L'
        elif int(test['결과'][i][0]) < int(test['결과'][i][1]):
            test['결과'][i] = 'W'
        elif int(test['결과'][i][0]) == int(test['결과'][i][1]):
            test['결과'][i] = 'D'
    else:
        pass
test.loc[test.결과 == '0', '결과'] = np.nan

# 팀코드전처리
test.loc[test.홈팀코드 == '한화', '홈팀코드'] = 'HH'
test.loc[test.홈팀코드 == '두산', '홈팀코드'] = 'OB'
test.loc[test.홈팀코드 == 'KIA', '홈팀코드'] = 'HT'
test.loc[test.홈팀코드 == '롯데', '홈팀코드'] = 'LT'
test.loc[test.홈팀코드 == '삼성', '홈팀코드'] = 'SS'
test.loc[test.홈팀코드 == '키움', '홈팀코드'] = 'WO'

test.loc[test.원정팀코드 == '한화', '원정팀코드'] = 'HH'
test.loc[test.원정팀코드 == '두산', '원정팀코드'] = 'OB'
test.loc[test.원정팀코드 == 'KIA', '원정팀코드'] = 'HT'
test.loc[test.원정팀코드 == '롯데', '원정팀코드'] = 'LT'
test.loc[test.원정팀코드 == '삼성', '원정팀코드'] = 'SS'
test.loc[test.원정팀코드 == '키움', '원정팀코드'] = 'WO'

# 오름차순정렬
test.sort_values(by=['일자'], ascending=True, inplace=True)

test = test.loc[test.일자 != '20200929', :].reset_index(drop=True)


# 빅콘제공데이터 합치기
k = pd.read_excel('./2020 KBO 정규시즌 잔여경기 현황_공지(200918).xlsx'
              , sheet_name = '잔여경기' )

col = k.iloc[1].values.tolist()
k = pd.DataFrame(data = k.iloc[2:].values, columns=col)
k['일자'] = k['일자'].astype('str')
for i in range(len(k)):
    k['일자'][i] = k['일자'][i].replace('-', '')

k.rename(columns = {'HOME':'홈팀코드', 'AWAY':'원정팀코드'}, inplace = True)

k.loc[k.홈팀코드 == '한화', '홈팀코드'] = 'HH'
k.loc[k.홈팀코드 == '두산', '홈팀코드'] = 'OB'
k.loc[k.홈팀코드 == 'KIA', '홈팀코드'] = 'HT'
k.loc[k.홈팀코드 == '롯데', '홈팀코드'] = 'LT'
k.loc[k.홈팀코드 == '삼성', '홈팀코드'] = 'SS'
k.loc[k.홈팀코드 == '키움', '홈팀코드'] = 'WO'

k.loc[k.원정팀코드 == '한화', '원정팀코드'] = 'HH'
k.loc[k.원정팀코드 == '두산', '원정팀코드'] = 'OB'
k.loc[k.원정팀코드 == 'KIA', '원정팀코드'] = 'HT'
k.loc[k.원정팀코드 == '롯데', '원정팀코드'] = 'LT'
k.loc[k.원정팀코드 == '삼성', '원정팀코드'] = 'SS'
k.loc[k.원정팀코드 == '키움', '원정팀코드'] = 'WO'

k = k.loc[k.비고 != '미진행 경기' , :]
k = k[['일자','원정팀코드','홈팀코드','요일', '구장']]

k['더블헤더코드'] = np.nan ; k['결과'] = np.nan

final_test = pd.concat([test,k], axis=0).reset_index(drop=True)


final_test.to_csv('final_test_real.csv', encoding='euc-kr')
