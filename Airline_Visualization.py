#FileName: Airline_Visualization.py
#edited by dharas, mvasa, abhootra, jwasan, svpanick, sarumall 
#Last Modified: February 25, 2019

#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from dateutil.parser import parse
import re
import matplotlib.pyplot as plt
import Clean_Merge_Data


#Regex to check if tweet content contains Shutdown
pat = r'Shutdown|shutdown'

list = []


#Enumerating over tweets to get the dates when the tweet contained shutown to store the date
for i,line in enumerate(Clean_Merge_Data.tweets['Tweet_content']):
    if re.search(pat,line)!= None:
        list.append(Clean_Merge_Data.tweets['Date'].loc[i])
        
#Converting the list into DataFrame
list1 = pd.DataFrame(list, columns=['Date'])

#Merging the regex tweet data with the clean data with only dates that are present in the list for all airlines
resultDelta = pd.merge(Clean_Merge_Data.tweets_and_da, list1, on='Date')
resultAmerican = pd.merge(Clean_Merge_Data.tweets_and_aa, list1, on='Date')
resultJetBlue = pd.merge(Clean_Merge_Data.tweets_and_ja, list1, on='Date')
resultSouthWest = pd.merge(Clean_Merge_Data.tweets_and_swa, list1, on='Date')

#Plotting the graphs for visualization

#Delta Airlines plot
tDelta = pd.Series(data=(Clean_Merge_Data.tweets_and_da['Open_da'].values-Clean_Merge_Data.tweets_and_da['Close/Last_da'].values), index=Clean_Merge_Data.tweets_and_da['Date'])
tDeltaTweet = pd.Series(data=(resultDelta['Open_da'].values-resultDelta['Close/Last_da'].values), index=resultDelta['Date'])

plt.subplot(1,1,1)
plt.gca().set_title('Effect of shutdown Tweets on Delta Airlines')
tDelta.plot(label = 'Delta Airlines',color='r', legend = True)
tDeltaTweet.plot(label = 'Delta Airlines with Shutdown',color='g', legend = True)
plt.show()

#American Airlines plot
tAmerican = pd.Series(data=(Clean_Merge_Data.tweets_and_aa['Open_aa'].values-Clean_Merge_Data.tweets_and_aa['Close/Last_aa'].values), index=Clean_Merge_Data.tweets_and_aa['Date'])
tAmericanTweet = pd.Series(data=(resultAmerican['Open_aa'].values-resultAmerican['Close/Last_aa'].values), index=resultAmerican['Date'])

plt.subplot(1,1,1)
plt.gca().set_title('Effect of shutdown Tweets on American Airlines')
tAmerican.plot(label = 'American Airlines',color='r', legend = True)
tAmericanTweet.plot(label = 'American Airlines with Shutdown',color='g', legend = True)
plt.show()

#JetBlue Plot
tJetBlue = pd.Series(data=(Clean_Merge_Data.tweets_and_ja['Open_ja'].values-Clean_Merge_Data.tweets_and_ja['Close/Last_ja'].values), index=Clean_Merge_Data.tweets_and_ja['Date'])
tJetBlueTweet = pd.Series(data=(resultJetBlue['Open_ja'].values-resultJetBlue['Close/Last_ja'].values), index=resultJetBlue['Date'])

plt.subplot(1,1,1)
plt.gca().set_title('Effect of shutdown Tweets on JetBlue Airlines')
tJetBlue.plot(label = 'JetBlue Airlines',color='r', legend = True)
tJetBlueTweet.plot(label = 'JetBlue Airlines with Shutdown',color='g', legend = True)
plt.show()

#SouthWest Plot
tSouthWest = pd.Series(data=(Clean_Merge_Data.tweets_and_swa['Open_swa'].values-Clean_Merge_Data.tweets_and_swa['Close/Last_swa'].values), index=Clean_Merge_Data.tweets_and_swa['Date'])
tSouthWestTweet = pd.Series(data=(resultSouthWest['Open_swa'].values-resultSouthWest['Close/Last_swa'].values), index=resultSouthWest['Date'])

plt.subplot(1,1,1)
plt.gca().set_title('Effect of shutdown Tweets on SouthWest Airlines')
tSouthWest.plot(label = 'SouthWest Airlines',color='r', legend = True)
tSouthWestTweet.plot(label = 'SouthWest Airlines with Shutdown',color='g', legend = True)
plt.show()

plt.tight_layout()