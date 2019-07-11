#FileName: Clean_Merge_Data.py
#edited by dharas, mvasa, abhootra, jwasan, svpanick, sarumall 
#Last Modified: February 25, 2019

from dateutil.parser import parse
import pandas as pd
from pandas import ExcelWriter

twitter_raw_filename = 'realDonaldTrump_tweets.csv'
# reading the twitter scrapped data file
tweets = pd.read_csv(twitter_raw_filename)
# setting the column of tweets dataframe
tweets.columns = ["Twitter_ID","Tweet_ID","Timestamp","Tweet_Content"]

tweets = tweets[pd.notnull(tweets["Tweet_Content"])]

SP500_clean_filename = 'S&P500_1Yr_Data.xlsx'
# reading the S&P500 scraped data file
SP500 = pd.read_excel(SP500_clean_filename, sheet_name='Clean')

#cleaning the Twitter data to change the format of data and make the data consistent
for index, row in tweets.iterrows():
    row["Tweet_Content"] = row["Tweet_Content"].strip('b\'')
    row["Timestamp"] = parse(row["Timestamp"]).strftime('%m/%d/%y')
    row["Timestamp"] = pd.to_datetime(row["Timestamp"])
    tweets["Timestamp"] = pd.to_datetime(tweets['Timestamp']).dt.date    
SP500 = SP500.reindex(index = SP500.index[::-1])
# setting the column of tweets dataframe
tweets.columns = ["Twitter_ID","Tweet_ID","Date","Tweet_content"]
# changing the type of SP500 Date column to datetime
SP500 = SP500.astype({"Date":"datetime64"})
# converting the Date column of tweets dataframe to datetime
tweets = tweets.astype({"Date":"datetime64"})

#Writing the dataframe into Excel
output_filename = 'cleaned_twitter.xlsx'
writer = ExcelWriter(output_filename)
tweets.to_excel(writer)
writer.save()

#---MERGING---
# dataframe that stores merged data of S&P500 and tweets
# merging on common column Date
tweets_stock = tweets.merge(SP500,how = 'left', on = 'Date')
tweets_stock = tweets_stock[pd.notnull(tweets_stock["Open"])]
tweets_stock.reset_index(drop = True)

#---CLEANING AND MERGING AIRLINE DATA (with Twitter Data)---
#Southwest_Airlines
# reading the data scraped from southwest file
airline_filename = 'Southwest.xlsx'
southwest_airlines = pd.read_excel(airline_filename)
# setting the columns for southwest_airlines dataframe
southwest_airlines.columns = ['Index','Date','Open_swa','High_swa','Low_swa','Close/Last_swa','Volume_swa']
southwest_airlines = southwest_airlines.drop('Index',axis = 1)
# cleaning up the data, removing extra spaces
southwest_airlines['Volume_swa'] = southwest_airlines['Volume_swa'].str.strip()
southwest_airlines = southwest_airlines.reindex(index = southwest_airlines.index[::-1])
# converting the datatype of date column
southwest_airlines['Date'] = pd.to_datetime(southwest_airlines['Date'], errors = 'coerce')
# merging the tweets and southwest_airlines dataframe
tweets_and_swa = tweets.merge(southwest_airlines,how = 'left', on = 'Date')
tweets_and_swa = tweets_and_swa[pd.notnull(tweets_and_swa["Open_swa"])]
tweets_and_swa.reset_index(drop = True)

#DeltaAirlines
# reading the data scraped from delta airlines file
airline_filename = 'DeltaAirlines.xlsx'
delta_airlines = pd.read_excel(airline_filename)
delta_airlines = delta_airlines.drop(delta_airlines.index[0])
# setting the columns for delta airlines dataframe
delta_airlines.columns = ['Index', 'Date','Open_da','High_da','Low_da','Close/Last_da','Volume_da']

# cleaning up the data, removing extra spaces
delta_airlines['Date'] = delta_airlines['Date'].str.strip()
delta_airlines['Open_da'] == delta_airlines['Open_da']
delta_airlines['High_da'] = delta_airlines['High_da']
delta_airlines['Low_da'] = delta_airlines['Low_da']
delta_airlines['Close/Last_da'] = delta_airlines['Close/Last_da']
delta_airlines['Volume_da'] = delta_airlines['Volume_da'].str.strip()
delta_airlines = delta_airlines.reindex(index = delta_airlines.index[::-1])
# converting the datatype of date column
delta_airlines['Date'] = pd.to_datetime(delta_airlines['Date'], errors = 'coerce')
# merging the tweets and delta airlines dataframe
tweets_and_da = tweets.merge(delta_airlines,how = 'left', on = 'Date')
tweets_and_da = tweets_and_da[pd.notnull(tweets_and_da["Open_da"])]
tweets_and_da.reset_index(drop = True)

#AmericanAirlines
# reading the data scraped from american airlines file
airline_filename = 'AmericanAirlines.xlsx'
american_airlines = pd.read_excel(airline_filename)
american_airlines = american_airlines.drop(american_airlines.index[0])
# setting the columns for american airlines dataframe
american_airlines.columns = ['Index', 'Date','Open_aa','High_aa','Low_aa','Close/Last_aa','Volume_aa']
# cleaning up the data, removing extra spaces
american_airlines['Date'] = american_airlines['Date'].str.strip()
american_airlines['Open_aa'] = american_airlines['Open_aa']

american_airlines['High_aa'] = american_airlines['High_aa']
american_airlines['Low_aa'] = american_airlines['Low_aa']
american_airlines['Close/Last_aa'] = american_airlines['Close/Last_aa']

american_airlines['Volume_aa'] = american_airlines['Volume_aa'].str.strip()
american_airlines = american_airlines.reindex(index = american_airlines.index[::-1])
# converting the datatype of date column
american_airlines['Date'] = pd.to_datetime(american_airlines['Date'], errors = 'coerce')
tweets_and_aa = tweets.merge(american_airlines,how = 'left', on = 'Date')
tweets_and_aa = tweets_and_aa[pd.notnull(tweets_and_aa["Open_aa"])]
tweets_and_aa.reset_index(drop = True)

#JetBlue_Airlines
# reading the data scraped from jet blue airlines file
airline_filename = 'JetBlue.xlsx'
jetblue_airline = pd.read_excel(airline_filename)
jetblue_airline = jetblue_airline.drop(jetblue_airline.index[0])
# setting the columns for jetblue airlines dataframe
jetblue_airline.columns = ['Index','Date','Open_ja','High_ja','Low_ja','Close/Last_ja','Volume_ja']
# cleaning up the data, removing extra spaces
jetblue_airline['Date'] = jetblue_airline['Date'].str.strip()
jetblue_airline['Open_ja'] = jetblue_airline['Open_ja']
jetblue_airline['High_ja'] = jetblue_airline['High_ja']
jetblue_airline['Low_ja'] = jetblue_airline['Low_ja']
jetblue_airline['Close/Last_ja'] = jetblue_airline['Close/Last_ja']
jetblue_airline['Volume_ja'] = jetblue_airline['Volume_ja'].str.strip()
jetblue_airline = jetblue_airline.reindex(index = american_airlines.index[::-1])
# converting the datatype of date column
jetblue_airline['Date'] = pd.to_datetime(jetblue_airline['Date'], errors = 'coerce')
tweets_and_ja = tweets.merge(jetblue_airline,how = 'left', on = 'Date')
tweets_and_ja = tweets_and_ja[pd.notnull(tweets_and_ja["Open_ja"])]

print("---Statistical Description---")
#Statistical Descriptive Analysis
print(tweets_and_ja.describe())
print(tweets_and_aa.describe())
print(tweets_and_da.describe())
print(tweets_and_swa.describe())