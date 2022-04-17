import pandas as pd
import time
import requests
def get_data(list1,list2): # function takes list of indicators and list of countries as arguments
    data=pd.DataFrame(columns=[x for x in list1])
    data['alpha-2']=list2
    for i in list1:
        time.sleep(1)
        temp=[]
        for n in [x.lower() for x in list2]:
            try:
                r=requests.get(f'http://api.worldbank.org/v2/country/{n}/indicator/{i}?date=2010&format=json').json()[1]
                temp.append(r[0]['value'])
            except:
                temp+=[None]

        data[i]=temp
    return data