'''
[개인타자 파일]
G_ID           경기ID(게임키)
GDAY_DS        경기날짜(일자)
T_ID           소속팀코드
VS_T_ID        상대팀코드
HEADER_NO      더블헤더코드- 모든 경기가 우천 등으로 순연되었을 경우, 그 다음 날 하루에 두 경기를 몰아서 하는 제도   
TB_SC          초말 (B/T)- TOP(초, away) / BOTTOM(말, home)
P_ID           선수코드
START_CK       선발- 1(선발) / 0(후발)
BAT_ORDER_NO   타순- 1~9번
PA             타자- 타석수 
AB             타수- 타석횟수(PA와 동일? 확인필요)
RBI            타점- 타자의 타격으로 인해 출루해 있던 주자들이 홈으로 들어오게 되는 타점
RUN            득점
HIT            안타   
H2             2루타 - 타자가 안타를 치고 2루까지 간 것
H3             3루타 - 타자가 안타를 치고 3루까지 간 것
HR             홈런
SB             도루 - 주자가 직접 베이스 진출에 성공한 횟수
CS             도루실패 
SH             희타 - 총희생타(ex번트)
SF             희비 - 타자의 플라이 아웃으로 인해 주자가 득점을 했을경우 
BB             4구 - 볼넷
IB             고4 - 고의 4구
HP             사구- 데드볼
KK             삼진- 3스트라이크아웃
GD             병살타 -  타자의 타격 후 수비수가 그 타구를 잡아 2명의 공격수를 아웃
ERR            실책 - 실수로 인해 진출
LOB            잔루 - 3아웃되는 동안 득점하지 못하고 1루, 2루, 3루에 쌓여 있는 주자
P_HRA_RT       득점권타율- 득점권(2루 3루)에 주자를 두었을 때의 타율
P_AB_CN        득점권타수- 득점권에서 타석에서 볼넷, 희생타, 타격 방해 등을 제외한 회수
P_HIT_CN       득점권안타- 득점권에서의 안타

[개인 투수 파일]


'''

'''
[경기 파일]
#경기
경기일별 기본 정보
2016 : 0401~1009
2017 : 0331~1003
2018 : 0324~1014
2019 : 0323~1001
2020 : 0505~0719
(우천취소시 아예 기록 X)
G_ID :      경기일+원정팀+홈팀+HEADER_NO
GDAY_DS :   경기일
VISIT_KEY : 원정팀
HOME_KEY :  홈팀
HEADER_NO : 더블헤더 여부 (0, 1, 2)
GWEEK :     경기 요일 (* KBO 야구는 매주 월요일는 쉬는 날)
STADIUM :   경기장

#선수
년도별 활동 선수 목록
GYEAR :     년도
PCODE :     선수코드
NAME :      선수명
T_ID :      팀 ID
POSITION :  포지션 (투, 내, 포, 외)
AGE_VA :    나이
MONEY :     연봉(단위 : 만원, 달러(외국인선수) )

#등록선수
각 경기일별 선수 출전 여부
2016 : 0401~1009
2017 : 0331~1003
2018 : 0324~1014
2019 : 0323~1001
2020 : 0505~0719
(경기 데이터와 동일)
GDAY_DS :   경기일
T_ID :      팀 ID
P_ID :      선수코드 (선수데이터의 PCODE와 동일)
ENTRY_YN :  당일 출전 여부(Y, N)

선수 데이터랑 등록선수 데이터에 선수코드가 서로 다른 변수명으로 지정되어 있어서 통일하는게 좋을 것 같아요 
'''

'''
[팀 타자 파일]
2016년~ 2020년
기간: 20160401~20200719
shape: (640, 28)

columns
'G_ID' :    경기날+원정팀+홈팀
'GDAY_DS':  경기날
'T_ID':     홈팀
'VS_T_ID':  원정팀
'HEADER_NO':더블 헤더 여부
'TB_SC'     초말 (B/T)- TOP(초, away) / BOTTOM(말, home)
'PA':       타석
'AB':       타수
'RBI':      타점
'RUN':      득점
'HIT':      안타(?)
'H2':       2루타(?)
'H3':       3루타(?)
'HR':       홈런
'SB':       도루
'CS':       도루실패
'SH':       희생 번트
'SF':       희생 플라이
'BB':       볼넷/4구
'IB':       고의 4구
'HP':       몸에 맞는 공
'KK':       야구에서는 삼진(struc'K'[1]out)을 K로 표기하는데, 한 이닝에서 3타자를 연속으로 삼진 처리하면 KKK
'GD':       더블플레이(?)
'ERR':      평균 자책점
'LOB':      잔루

P_HRA_RT       득점권타율- 득점권(2루 3루)에 주자를 두었을 때의 타율
P_AB_CN        득점권타수- 득점권에서 타석에서 볼넷, 희생타, 타격 방해 등을 제외한 회수
P_HIT_CN       득점권안타- 득점권에서의 안타


[팀 투수 파일]
#team_투수
#2016년~2020년
#기간:20160401~20200719
'G_ID':       경기날+원정팀+홈팀
'GDAY_DS':    경기날
'T_ID':       홈팀
'VS_T_ID':    원정팀
'HEADER_NO':  더블 헤드 여부
'TB_SC':      초말 (B/T)
'CG_CK':      CG는 완투 승
'WLS':        win or lose
'HOLD':       홀드
'INN2':       이닝*3
'BF':         타자와 마주하는 횟수
'PA':         타석 
'AB':         타수 
'HIT':        안타
'H2':         2루타
'H3':         3루타
'HR':         홈런 
'SB':         도루
'CS':         도루사 
'SH':         희생 번트 
'SF':         희생 플라이
'BB':         볼넷 
'IB':         고의 4구 
'HP':         몸에 맞는 공
'KK':         야구에서는 삼진(struc'K'[1]out)을 K로 표기하는데, 한 이닝에서 3타자를 연속으로 삼진 처리하면 KKK
'GD':         병살타
'WP':         폭투 
'BK':         투수 보크 
'ERR':        평균 자책점 
'R':          실점 
'ER':         자책점 
'WHIP_RT':    말 그대로 이닝당 평균적으로 몇 명의 타자를 출루시켰냐를 뜻한다. 즉 총 출루 허용수(총 피안타수 + 총 사구수)를 이닝수로 나눈다.

'P_WHIP_RT'   득점권에서의 이닝당 안타 볼넷 허용률
'P2_WHIP_RT'  2점차에서의  이닝당 안타 볼넷 허용률
'CB_WHIP_RT'  3,4,5번 타자순서에서의 이닝당 안타 볼넷 허용률 

'''

import os
import pandas as pd 
import numpy as np


## visualize
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc
from matplotlib import style

# preprocessing
import itertools as it
import operator
from tqdm import tqdm

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
style.use('ggplot')
%matplotlib auto

os.chdir('C:/Users/etotm/Desktop/bigcont')

game = pd.read_excel('./data/2020빅콘테스트_데이터분석분야_퓨처스리그_데이터정의서.xlsx'
              , sheet_name = '2.경기' ).columns.tolist()
ply = pd.read_excel('./data/2020빅콘테스트_데이터분석분야_퓨처스리그_데이터정의서.xlsx'
              , sheet_name = '3.선수' ).columns.tolist()
t_tusu = pd.read_excel('./data/2020빅콘테스트_데이터분석분야_퓨처스리그_데이터정의서.xlsx'
              , sheet_name = '4.팀투수' ).columns.tolist()
t_tasa = pd.read_excel('./data/2020빅콘테스트_데이터분석분야_퓨처스리그_데이터정의서.xlsx'
              , sheet_name = '5.팀타자' ).columns.tolist()
p_tusu = pd.read_excel('./data/2020빅콘테스트_데이터분석분야_퓨처스리그_데이터정의서.xlsx'
              , sheet_name = '6.개인투수' ).columns.tolist()
p_tasa = pd.read_excel('./data/2020빅콘테스트_데이터분석분야_퓨처스리그_데이터정의서.xlsx'
              , sheet_name = '7.개인타자' ).columns.tolist()
a = pd.read_excel('./data/2020빅콘테스트_데이터분석분야_퓨처스리그_데이터정의서.xlsx'
              , sheet_name = '8.등록선수(일자별)' ).columns.tolist()



p_tasa16 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_개인타자_2016.csv') ; p_tasa16.columns = p_tasa
p_tasa17 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_개인타자_2017.csv') ; p_tasa17.columns = p_tasa
p_tasa18 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_개인타자_2018.csv') ; p_tasa18.columns = p_tasa
p_tasa19 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_개인타자_2019.csv') ; p_tasa19.columns = p_tasa
p_tasa20 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_개인타자_2020.csv') ; p_tasa20.columns = p_tasa

p_tusu16 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_개인투수_2016.csv') ; p_tusu16.columns = p_tusu
p_tusu17 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_개인투수_2017.csv') ; p_tusu17.columns = p_tusu
p_tusu18 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_개인투수_2018.csv') ; p_tusu18.columns = p_tusu
p_tusu19 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_개인투수_2019.csv') ; p_tusu19.columns = p_tusu
p_tusu20 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_개인투수_2020.csv') ; p_tusu20.columns = p_tusu

t_tasa16 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_팀타자_2016.csv') ; t_tasa16.columns = t_tasa
t_tasa17 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_팀타자_2017.csv') ; t_tasa17.columns = t_tasa
t_tasa18 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_팀타자_2018.csv') ; t_tasa18.columns = t_tasa
t_tasa19 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_팀타자_2019.csv') ; t_tasa19.columns = t_tasa
t_tasa20 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_팀타자_2020.csv') ; t_tasa20.columns = t_tasa


t_tusu16 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_팀투수_2016.csv') ; t_tusu16.columns = t_tusu
t_tusu17 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_팀투수_2017.csv') ; t_tusu17.columns = t_tusu
t_tusu18 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_팀투수_2018.csv') ; t_tusu18.columns = t_tusu
t_tusu19 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_팀투수_2019.csv') ; t_tusu19.columns = t_tusu
t_tusu20 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_팀투수_2020.csv') ; t_tusu20.columns = t_tusu



gm16 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_경기_2016.csv') ; gm16.columns = game
gm17 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_경기_2017.csv') ; gm17.columns = game
gm18 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_경기_2018.csv') ; gm18.columns = game
gm19 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_경기_2019.csv') ; gm19.columns = game
gm20 = pd.read_csv('data/2020빅콘테스트_스포츠투아이_제공데이터_경기_2020.csv') ; gm20.columns = game


ptasa = pd.concat([p_tasa16, p_tasa17, p_tasa18, p_tasa19, p_tasa20], axis=0).reset_index(drop=True)
ptusu = pd.concat([p_tusu16, p_tusu17, p_tusu18, p_tusu19, p_tusu20], axis=0).reset_index(drop=True)
ttasa = pd.concat([t_tasa16, t_tasa17, t_tasa18, t_tasa19, t_tasa20], axis=0).reset_index(drop=True)
ttusu = pd.concat([t_tusu16, t_tusu17, t_tusu18, t_tusu19, t_tusu20], axis=0).reset_index(drop=True)
gm = pd.concat([gm16, gm17, gm18, gm19, gm20], axis=0).reset_index(drop=True)


ttasa.to_csv("ttasa.csv",encoding='cp949')
ttusu.to_csv("ttusu.csv",encoding='cp949')



def SECA(df2):
    df = df2.copy()
    df['SECA'] = (df['2루타'] + 2*df['3루타'] + 3*df['홈런'] + df['도루'] - df['도루실패']) / df['타수']
    return df
#BABIP = (안타-홈런) / (타수-삼진-홈런+희생플라이)
def BABIP(df2):
    df = df2.copy()
    df['BABIP'] = (df['안타'] - df['홈런']) / (df['타수']-df['삼진']-df['홈런']+df['희비'])    
    return df
#OPS (체크확인)
def OPS(df2):
    df = df2.copy()
    cul = (df['1루타'] + df['4구'] + df['사구'])/ (df['타수'] + df['4구'] + df['사구'] + df['희비'])
    jan = (df['1루타'] + 2*df['2루타'] + 3*df['3루타'] + 4*df['홈런']) / df['타수']
    df['OPS'] = cul + jan
    return df
#GPA
def GPA(df2):
    df = df2.copy()
    df['GPA'] = (1.8*df['OPS']) / 4
    return df
#RC
def RC(df2):
    df = df2.copy()
    a=df['1루타']+df['사구']+df['4구']-df['도루실패']-df['병살타']
    b=0.24*(df['4구']+df['사구']-df['고4'])+0.5*(df['희타']+df['희비'])+0.62*df['도루']-0.03*df['삼진']
    c=df['타수']+df['4구']+df['사구']+df['희타']+df['희비']
    df['RC']= (2.4*c+a)*(3*c+b) /(9*c) -0.9*c
    return df
#XR
def XR(df2):
    df = df2.copy()
    df['XR']=df['1루타']*0.5+df['2루타']*0.72+df['3루타']*1.04+df['홈런']*1.44+(df['4구']+df['사구']+df['고4'])*0.34+df['고4']*0.25+df['도루']*0.18-df['도루실패']*0.32 -(df['타수']-(df['안타']+df['2루타']+df['3루타']+df['홈런'])-df['삼진'])*0.09 -df['삼진']*0.098-df['병살타']*0.37+df['희비']*0.37+df['희타']*0.04
    return df    
#wOBA
def wOBA(df2):
    df=df2.copy()
    df['wOBA']=(0.72*(df['4구']-df['고4']) + 0.75*df['사구'] + 0.90*df['1루타'] + 0.92*df['실책'] + 1.24*df['2루타'] + 1.56*df['3루타'] + 1.95*df['홈런'])/(df['타석'] - df['고4'])
    return df
#ISO
def ISO(df2):
    df = df2.copy()
    df['ISO'] = (df['2루타'] +2*df['3루타'] + 3*df['홈런'])/df['타석']
    return df
# EOBP
def EOBP(df2):
    df = df2.copy()
    df['출루율'] = (df['안타'] + df['4구'] + df['사구'])/ (df['타수'] + df['4구'] + df['사구'] + df['희비'])
    df['타율'] =  df['안타']/ df['타수']
    df['EOBP'] = df['출루율'] - df ['타율'] 
    return df

def saver(ptasa):
    
    ptasa = SECA(ptasa)
    ptasa = BABIP(ptasa)
    ptasa = OPS(ptasa)
    ptasa = GPA(ptasa)
    ptasa = RC(ptasa)
    ptasa = XR(ptasa)
    ptasa = wOBA(ptasa)
    ptasa = ISO(ptasa)
    ptasa = EOBP(ptasa)
    
    return ptasa



#### 셋구축
def make_game(gm, ttusu):
    gm = gm[['게임키','일자','홈팀코드','원정팀코드','더블헤더코드','요일','구장']]
    gm.rename(columns = {'홈팀코드': '팀코드', '원정팀코드':'상대팀코드'}, inplace = True)
    
    ttusu = ttusu.drop_duplicates(['게임키'], keep='first')
    
    gm = gm.merge(ttusu[['게임키' , '결과']])
    return gm


def make_tusu_col(ptusu, gm, ttusu):
    ptusu = BABIP(ptusu) # BAPIP 파생변수
    gm = make_game(gm, ttusu) # game세트 생성
    pts = ptusu.copy()
    ## 홈기준
    # 선발
    b = pts.loc[pts.선발==1,['게임키','팀코드','상대팀코드','득점권WHIP','2점차이하WHIP','345번타자WHIP','BABIP']]
    gm1 = gm.merge(b, on=['게임키','팀코드','상대팀코드'])
    gm1.rename(columns = {'득점권WHIP':'득점권WHIP_Hptu1', '2점차이하WHIP' : '2점차이하WHIP_Hptu1', '345번타자WHIP':'345번타자WHIP_Hptu1', 'BABIP':'BABIP_Hptu1'}, inplace = True)
    # 후발
    c = pts.loc[pts.선발==0,['게임키','팀코드','상대팀코드','득점권WHIP','2점차이하WHIP','345번타자WHIP','BABIP']]
    ex = pd.DataFrame(index = range(len(c['게임키'].unique())), columns=c.loc[c.게임키 == c['게임키'][0], :].mean().index.tolist())
    gamekey = []
    for i in range(c['게임키'].nunique()):
        ex.iloc[i] = c.loc[c.게임키 == c['게임키'].unique()[i], :].mean().values
        gamekey.append(c['게임키'].unique()[i])
    ex['게임키'] = gamekey ; gm1 = gm1.merge(ex, on=['게임키'], how='outer').fillna(0)
    gm1.rename(columns = {'득점권WHIP':'득점권WHIP_Hptu0', '2점차이하WHIP' : '2점차이하WHIP_Hptu0', '345번타자WHIP':'345번타자WHIP_Hptu0', 'BABIP':'BABIP_Hptu0'}, inplace = True)

    ## 원정기준
    # 선발
    b = gm.merge(b, on=['게임키','팀코드','상대팀코드'], how='outer')
    b = b.tail(3200).reset_index(drop=True)
    b = b[['득점권WHIP', '2점차이하WHIP', '345번타자WHIP', 'BABIP']]
    b.rename(columns = {'득점권WHIP':'득점권WHIP_Aptu1',  '2점차이하WHIP' : '2점차이하WHIP_Aptu1', '345번타자WHIP':'345번타자WHIP_Aptu1', 'BABIP':'BABIP_Aptu1'}, inplace = True)
    gm1 = pd.concat([gm1,b], axis=1)
    # 후발
    gm['구분'] = gm.일자.astype(str) + gm.팀코드 + gm.상대팀코드
    c = pts.loc[pts.선발==0,['일자','팀코드','상대팀코드','구원','득점권WHIP','2점차이하WHIP','345번타자WHIP','BABIP']] 
    c['구분'] = c.일자.astype(str) + c.팀코드 + c.상대팀코드
    ex = pd.DataFrame(index = range(len(c['구분'].unique())), columns=c.loc[c.구분 == c['구분'][0], :].mean().index.tolist())
    gamekey = []
    for i in range(len(c['구분'].unique())):
        ex.iloc[i] = c.loc[c.구분 == c['구분'].unique()[i], :].mean().values
        gamekey.append(c['구분'].unique()[i])
    ex['구분'] = gamekey ; sa = gm.merge(ex, on=['구분'], how='outer').tail(3200)[['득점권WHIP', '2점차이하WHIP','345번타자WHIP','BABIP']].reset_index(drop=True)
    sa.rename(columns = {'득점권WHIP':'득점권WHIP_Aptu0', '2점차이하WHIP' : '2점차이하WHIP_Aptu0', 
                          '345번타자WHIP':'345번타자WHIP_Aptu0', 'BABIP':'BABIP_Aptu0'}, inplace = True)
    gm1 = pd.concat([gm1, sa], axis=1 )
    return gm1


gm = make_tusu_col(ptusu, gm, ttusu)

gm.isnull().sum()
gm = gm.fillna(0)

#-----------------------------------------------------------------
ptasa = ptasa.groupby(['게임키','팀코드','타순']).sum().reset_index()


# 타석 변수 생성
ptasa['타석'] = ptasa['타수']+ptasa['4구']+ptasa['사구']+ptasa['희타']+ptasa['희비']
ptasa['1루타'] = ptasa['안타']-(ptasa['2루타']+ptasa['3루타']+ptasa['홈런'])

# 타자의 세이버 매트릭스 
ptasa = SECA(ptasa)
ptasa = BABIP(ptasa)
ptasa = OPS(ptasa)
ptasa = GPA(ptasa)
ptasa = RC(ptasa)
ptasa = XR(ptasa)
ptasa = wOBA(ptasa)
ptasa = ISO(ptasa)
ptasa = EOBP(ptasa)

a = ptasa.describe().T


#결측값 0으로 대체 -> 결측인 경우는 0/0
#-inf 0으로 대체 -> -n/0
ptasa.isnull().sum()
ptasa = ptasa.fillna(0)
ptasa.SECA = ptasa.SECA.apply(lambda x : x*0 if x==-np.inf else x)



# (x = 3,4,5번 타자) y = 나머지타자 | 1 -> 홈, 2-> 원정
def merge_df(gm,ptasa):
    df= gm.copy()
    p_clean = ptasa[(ptasa.타순 == 3) | (ptasa.타순 == 4) | (ptasa.타순 == 5)].groupby(['게임키','팀코드']).mean().reset_index()
    p_etc = ptasa.drop(ptasa[(ptasa.타순 == 3) | (ptasa.타순 == 4) | (ptasa.타순 == 5)].index,inplace=False,axis=0).groupby(['게임키','팀코드']).mean().reset_index()

    
    a = pd.DataFrame(np.array(p_clean.loc[:,['게임키','팀코드','SECA','BABIP', 'GPA', 'RC', 'XR', 'wOBA', 'ISO', 'EOBP']])\
             .reshape(3200,20),columns=['게임키','팀코드','SECA1','BABIP1', 'GPA1', 'RC1', 'XR1', 'wOBA1', 'ISO1', 'EOBP1','게임키2','팀코드2','SECA2','BABIP2', 'GPA2', 'RC2', 'XR2', 'wOBA2', 'ISO2', 'EOBP2']).drop(['게임키2','팀코드','팀코드2'],inplace=False,axis=1)
    b = pd.DataFrame(np.array(p_etc.loc[:,['게임키','팀코드','SECA','BABIP', 'GPA', 'RC', 'XR', 'wOBA', 'ISO', 'EOBP']])\
             .reshape(3200,20),columns=['게임키','팀코드','SECA1','BABIP1', 'GPA1', 'RC1', 'XR1', 'wOBA1', 'ISO1', 'EOBP1','게임키2','팀코드2','SECA2','BABIP2', 'GPA2', 'RC2', 'XR2', 'wOBA2', 'ISO2', 'EOBP2']).drop(['게임키2','팀코드','팀코드2'],inplace=False,axis=1)
    d = df.merge(a, on='게임키')
    return d.merge(b, on='게임키')


train = merge_df(gm ,ptasa)
#p.to_csv('final_train.csv', index=False)
train.isnull().sum()


# 누적(기준 : 3,4,5 그외 )
def calm(train):
 
    ptasa['년도'] = ptasa['게임키'].apply(lambda x : int(x[:4]))
    p_clean = ptasa[(ptasa.타순 == 3) | (ptasa.타순 == 4) | (ptasa.타순 == 5)].groupby(['게임키','팀코드']).sum().reset_index()
    p_etc = ptasa.drop(ptasa[(ptasa.타순 == 3) | (ptasa.타순 == 4) | (ptasa.타순 == 5)].index,inplace=False,axis=0).groupby(['게임키','팀코드']).sum().reset_index()
    
    p_clean['년도'] = p_clean['게임키'].apply(lambda x : int(x[:4]))
    p_etc['년도'] = p_etc['게임키'].apply(lambda x : int(x[:4]))
    
    
    cols = ['타수', '타점','득점', '안타', '2루타', '3루타', '홈런', '도루', '도루실패',\
       '희타', '희비', '4구', '고4','사구', '삼진', '병살타', '실책', '타석', '1루타']
    a = pd.DataFrame()
    b = pd.DataFrame()
    c = pd.DataFrame()
    d = pd.DataFrame()
    
    
    for i in tqdm(range(len(train))):
        year =  int(train.게임키[i][:4])
        home = train.팀코드[i]
        away = train.상대팀코드[i]
       
        p1 = p_clean[(p_clean.팀코드 == home) & (p_clean.년도== int(year))].reset_index(drop=True)
        p2 = p_etc[(p_etc.팀코드 == home) & (p_etc.년도== int(year))].reset_index(drop=True)
        
        p3 = p_clean[(p_clean.팀코드 == away) & (p_clean.년도== int(year))].reset_index(drop=True)
        p4 = p_etc[(p_etc.팀코드 == away) & (p_etc.년도== int(year))].reset_index(drop=True)
        
        
        for col in cols:
            p1[col] = list(it.accumulate(p1[col]))
            p2[col] = list(it.accumulate(p2[col]))
            p3[col] = list(it.accumulate(p3[col]))
            p4[col] = list(it.accumulate(p4[col]))
            
        p1 = saver(p1)
        p2 = saver(p2)
        p3 = saver(p3)
        p4 = saver(p4)
        
        
        
        one = p1[p1.게임키 == train.게임키[i]].loc[:,['SECA','BABIP', 'GPA', 'RC', 'XR', 'wOBA', 'ISO', 'EOBP']]
        two = p2[p2.게임키 == train.게임키[i]].loc[:,['SECA','BABIP', 'GPA', 'RC', 'XR', 'wOBA', 'ISO', 'EOBP']]
        three = p3[p3.게임키 == train.게임키[i]].loc[:,['SECA','BABIP', 'GPA', 'RC', 'XR', 'wOBA', 'ISO', 'EOBP']]
        four = p4[p4.게임키 == train.게임키[i]].loc[:,['SECA','BABIP', 'GPA', 'RC', 'XR', 'wOBA', 'ISO', 'EOBP']]
        
        
        
        a = a.append(one)
        b = b.append(two)
        c = c.append(three)
        d = d.append(four)
        
    #train = pd.concat([train,a,b,c,d],axis=0)
        
    a = a.reset_index(drop=True)
    b = b.reset_index(drop=True)
    c = c.reset_index(drop=True)
    d = d.reset_index(drop=True)
    
    for col in a.columns.tolist():
        a.rename(columns = {col:col+"h_clean"}, inplace = True)
    for col in b.columns.tolist():
        b.rename(columns = {col:col+"h_etc"}, inplace = True)
    for col in c.columns.tolist():
        c.rename(columns = {col:col+"a_clean"}, inplace = True)
    for col in d.columns.tolist():
        d.rename(columns = {col:col+"a_etc"}, inplace = True)

    kk = pd.concat([train,a,b,c,d],axis=1)
        
        
    return kk

final = calm(train)
#final = final.fillna(0)


#final = pd.read_csv('traintrain.csv', index_col=0)
final['home'] = 1
final2 = final.copy()
del final2['home']



col = ['게임키', '일자',  '상대팀코드','팀코드', '더블헤더코드', '요일', '구장', '결과', 
       '득점권WHIP_Aptu1','2점차이하WHIP_Aptu1', '345번타자WHIP_Aptu1', 'BABIP_Aptu1', '득점권WHIP_Aptu0', '2점차이하WHIP_Aptu0', '345번타자WHIP_Aptu0', 'BABIP_Aptu0',
       '득점권WHIP_Hptu1', '2점차이하WHIP_Hptu1', '345번타자WHIP_Hptu1', 'BABIP_Hptu1', '득점권WHIP_Hptu0', '2점차이하WHIP_Hptu0', '345번타자WHIP_Hptu0', 'BABIP_Hptu0', 
       'SECA2_x', 'BABIP2_x', 'GPA2_x', 'RC2_x', 'XR2_x', 'wOBA2_x','ISO2_x', 'EOBP2_x','SECA1_x', 'BABIP1_x', 'GPA1_x', 'RC1_x', 'XR1_x', 'wOBA1_x', 'ISO1_x','EOBP1_x',
       'SECA2_y', 'BABIP2_y', 'GPA2_y','RC2_y', 'XR2_y', 'wOBA2_y', 'ISO2_y', 'EOBP2_y', 'SECA1_y', 'BABIP1_y', 'GPA1_y', 'RC1_y', 'XR1_y', 'wOBA1_y','ISO1_y', 'EOBP1_y', 
       'SECAa_clean', 'BABIPa_clean', 'GPAa_clean', 'RCa_clean', 'XRa_clean', 'wOBAa_clean', 'ISOa_clean', 'EOBPa_clean', 
       'SECAa_etc', 'BABIPa_etc', 'GPAa_etc', 'RCa_etc', 'XRa_etc', 'wOBAa_etc', 'ISOa_etc', 'EOBPa_etc',
       'SECAh_clean','BABIPh_clean', 'GPAh_clean', 'RCh_clean', 'XRh_clean', 'wOBAh_clean', 'ISOh_clean', 'EOBPh_clean', 
       'SECAh_etc', 'BABIPh_etc', 'GPAh_etc', 'RCh_etc', 'XRh_etc', 'wOBAh_etc', 'ISOh_etc','EOBPh_etc']

final2 = pd.DataFrame(np.array(final2),columns = col)
final2.결과 = final2.결과.apply(lambda x : x.replace("W","L") if x =="W" else x.replace("L","W"))
final2['home'] = 0


final.일자 = final.일자.astype('int')
final2.일자 = final2.일자.astype('int')

final = pd.concat([final,final2],axis=0)
final.sort_values(by=['일자'], ascending=True, inplace=True)

final.일자 = pd.to_datetime(final.일자,format='%Y%m%d')
final.iloc[:,8:] = final.iloc[:,8:].astype('float')

final.to_csv("final_train.csv")



# 팀별로 세트만들기
#final = pd.read_csv("final_train.csv",index_col =0)

for i in final.팀코드.unique().tolist():
    globals()['df{}'.format(i)] = final[(final.팀코드 == i)]  
    globals()['df{}'.format(i)].to_csv("{}.csv".format(i))



