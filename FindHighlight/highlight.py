import json
import datetime
import pandas as pd
from collections import Counter 
from matplotlib import pyplot as plt

with open("DreamChat/Samples/LCK/LCK_Summer_Split.json", encoding='UTF-8') as jFile:
    dict1 = json.load(jFile)

# string to time
timeData=[]
for m in dict1:
    timestr = dict1[m]['time']
    dt = datetime.datetime.strptime(timestr, '[%H:%M:%S]')
    timeData.append(dt.hour*3600+dt.minute*60+dt.second)

# sorting
freq = Counter(timeData)
rawData = pd.Series(freq)
rawData = rawData.reindex(list(range(1,rawData.last_valid_index()+1)), fill_value=0)

# filtering (moving arrange filter)
win = 7 #입력
filtData = rawData.rolling(win).mean()


# find highlight
TERM = 10 #입력(하이라이트 기간)
START = 5*60 #입력(시작시간)
PER = 3 #입력(퍼센트)
length = rawData.last_valid_index() #영상길이
lim = length*PER*0.01 #하이라이트 길이

hiData = filtData.drop(list(range(1,START))).sort_values(ascending=[False])
H=[]
hileng=0
num=0
while(hileng<lim):
    hileng=0
    peaktime=hiData.index[num]
    H.append((peaktime-TERM, peaktime))
    H.sort()
    try:
        for i in range(0,len(H)):
            while (True):
                if H[i][1] >= H[i+1][0]:
                    if H[i][1] <= H[i+1][1]:
                        H[i]=(H[i][0],H[i+1][1])
                    del H[i+1]
                else:
                    break
    except IndexError:
        for t in H:
            hileng += t[1]-t[0]
    num+=1
print(H)
print("하이라이트 개수 :" + str(len(H)))
print("하이라이트 길이 :" + str(hileng))

# visualization
filtData.plot(figsize=(50,15), grid=True, title="Catch Highlights")
plt.xlabel("sec")
plt.savefig('graph.png')