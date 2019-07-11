#FileName: China_Trade_Visualization.py
#edited by dharas, mvasa, abhootra, jwasan, svpanick, sarumall 
#Last Modified: February 25, 2019

#!/usr/bin/env python
# coding: utf-8
import Clean_Merge_Data
import pandas as pd
import re
import matplotlib.pyplot as plt

#get_ipython().run_line_magic('matplotlib', 'inline')

# loading twitter and sp500 merged dataframe
stocks = Clean_Merge_Data.tweets_stock
# loading s&p500 dataframe in SP500
SP500 = Clean_Merge_Data.SP500
temp_dataList = []
# search pattern to extract tweets related to china trade war
pat=r'((Trade|Market|Tariff|Deal|War|negotiat.* economy|agreement|distributors|dispute|pay).*China)|(China.*(Trade|Market|Tariff|Deal|War|negotiat.* economy|agreement|distributors|dispute|pay))'
# extracting date, tweet, opening stock and closing stock based on dates when trump tweets about China trade
for i, line in enumerate(stocks['Tweet_content']):
    if(re.search(pat,line, re.IGNORECASE)):
        temp_dataList.append([stocks['Date'].iloc[i],stocks['Tweet_content'].iloc[i], stocks['Open'].iloc[i], stocks['Close'].iloc[i]])        
# storing the extracted result in a dataframe
stocksOnChinaTweet = pd.DataFrame(temp_dataList, columns=['Date','Tweet', 'Open','Close']);
# preparing timeseries of deviation in stock market when trump tweets about china trade
plotStockChina = pd.Series(data=(stocksOnChinaTweet['Open'].values-stocksOnChinaTweet['Close'].values), index=stocksOnChinaTweet['Date'])
# preparing timeseries of deviation in stock market on all the stocks
plotStock =  pd.Series(data=(SP500['Open'].values-SP500['Close'].values), index=SP500['Date'])
# setting the plot attributes
plt.subplot(1,1,1)
plt.gca().set_title('Effect of China Trade war tweets on Stock Market')
plotStockChina.plot(label = 'Stock trend during China trade war',color='r', legend = True)
plotStock.plot(label = 'Stock trend',color='g', legend = True)
date_China = stocksOnChinaTweet["Date"]
plt.axvspan(date_China[0], date_China[len(date_China)-1], facecolor='#ffffe0', alpha=0.5)
plt.show()

temp_dataList = []
# search pattern to extract tweets related to mexico border
pat=r'((wall|border).*Mexic.*)|(Mexic.*(wall|border))'
# extracting date, tweet, opening stock and closing stock based on dates when trump tweets about Mexico wall
for i, line in enumerate(stocks['Tweet_content']):
    if(re.search(pat,line, re.IGNORECASE)):
        temp_dataList.append([stocks['Date'].iloc[i],stocks['Tweet_content'].iloc[i], stocks['Open'].iloc[i], stocks['Close'].iloc[i]])        
# storing the extracted result in a dataframe
stocksOnMexicoTweet = pd.DataFrame(temp_dataList, columns=['Date','Tweet', 'Open','Close']);
# preparing timeseries of deviation in stock market to be plotted when trump tweets about Mexico wall
plotStockMexico = pd.Series(data=(stocksOnMexicoTweet['Open'].values-stocksOnMexicoTweet['Close'].values), index=stocksOnMexicoTweet['Date'])
# preparing timeseries of deviation in stock market on all the stocks
plotStock =  pd.Series(data=(SP500['Open'].values-SP500['Close'].values), index=SP500['Date'])
# setting plot attributes
plt.subplot(1,1,1)
plt.gca().set_title('Effect of Mexico Wall tweets on Stock Market')
plotStockMexico.plot(label = 'Stock trend during Mexico Border Tweets',color='r', legend = True)
plotStock.plot(label = 'Stock trend',color='g', legend = True)
date_Mexico = stocksOnMexicoTweet["Date"]
plt.axvspan(date_Mexico[0], date_Mexico[len(date_Mexico)-1], facecolor='#ffffe0', alpha=0.5)
plt.show()