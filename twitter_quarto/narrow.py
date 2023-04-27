import pandas as pd
import numpy as np
import xlsxwriter


cols = [0,1,6,7,8,9,13,14,15,16] # cols == id, text, geobox1, gb2, gb3, gb4, year, day, month, sentiment value

ids = []
tweets = [] # list of all tweets
gb1 = []
gb2 = []
gb3 = []
gb4 = []
year = []
day = []
month = []
sen = []


df = pd.read_excel('what.xlsx', usecols=cols)

id_tweet = df.to_numpy()


for item in id_tweet:
    ids.append(item[0])
    tweets.append(item[1])
    gb1.append(item[2])
    gb2.append(item[3])
    gb3.append(item[4])
    gb4.append(item[5])
    year.append(item[6])
    day.append(item[7])
    month.append(item[8])
    sen.append(item[9])


cleaned_ids = []
cleaned_tweets = [] # list of all relevant tweets...
cleaned_gb1 = [] 
cleaned_gb2 = []
cleaned_gb3 = []
cleaned_gb4 = []
cleaned_year = []
cleaned_day = []
cleaned_month = []
cleaned_sen = []

indexes = [] # list of relevant tweet indexes -- used to call id, geo data... etc



for item in tweets:
    if("voto") not in str(item):
        if("@LassoMusica" or "fun") not in str(item): 
            if("artista") not in str(item): 
                if("@victordrija") not in str(item): 
                    if("cantautor") not in str(item): 
                        if("cantante") not in str(item): 
                            indx = tweets.index(item)
                            cleaned_ids.append(ids[indx])
                            cleaned_tweets.append(tweets[indx])
                            cleaned_gb1.append(gb1[indx])
                            cleaned_gb2.append(gb2[indx])
                            cleaned_gb3.append(gb3[indx])
                            cleaned_gb4.append(gb4[indx])
                            cleaned_year.append(year[indx])
                            cleaned_day.append(day[indx])
                            cleaned_month.append(month[indx])
                            cleaned_sen.append(sen[indx])


org = {"id":cleaned_ids, "text":cleaned_tweets, "gb1": cleaned_gb1, "gb2":cleaned_gb2, "gb3":cleaned_gb3,
"gb4": cleaned_gb4, "year":cleaned_year, "day":cleaned_day, "month":cleaned_month, "sen":cleaned_sen}

df1 = pd.DataFrame(org) 


df1.to_excel('parsed_twt_data.xlsx') 





