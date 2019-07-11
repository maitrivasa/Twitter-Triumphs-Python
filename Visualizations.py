#FileName: Visualizations.py
#edited by dharas, mvasa, abhootra, jwasan, svpanick, sarumall 
#Last Modified: February 25, 2019

import pandas as pd
import matplotlib.pyplot as plt
import numpy as  np

#This is the downloadable data we are using from the below mentioned website
#Reference: https://www.washingtonpost.com/graphics/2019/politics/shutdown-federal-worker-impact/?utm_term=.3be0efa7cb1b
#This file is saved and stored in the main project directory

#Error Handling if the file isn't present
try:
    filename = "Shutdown_1.xlsx"
    #Storing the file information into a pandas dataframe 
    df_shutdown_1 = pd.read_excel(filename)
    
    #Visualisation 1
    print("Lets draw some insights about the impact of shutdown on federal workers")

    states = df_shutdown_1[1:]['State'].unique()
    sums = df_shutdown_1[1:]['IndustryTotal']

    # height = list(wordlist.values())
    # bars = tuple(wordlist.keys())
    y_pos = np.arange(0, len(states)*5,5)
    #print(y_pos)

    plt.figure(figsize=(15,5))

    rects = plt.bar(y_pos, sums, width = 3)
    plt.xticks(y_pos, states, rotation = 'vertical')

    #rects = plt.bar(states,sums, width = 0.8, bottom=None, align='edge')
    plt.xticks(rotation='vertical')
    plt.title("2018-19 Shutdown: Impact on Federal Workers in TRANSPORTATION INDUSTRY")
    plt.xlabel("US State")
    plt.ylabel("Number of workers")

    stateTotal = df_shutdown_1[1:]['StateTotal'].values
    total_count = df_shutdown_1.iloc[0]['StateTotal']

    #setting the total for every state
    i=0
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., 1*height,
                 str(round(stateTotal[i]/total_count*100, 2)) + "%", ha='center', va='bottom')
        i += 1

    plt.show()

    #Visualisation 2

    print("Lets draw some insights about the number of tweets and corresponding hashtags")
    filename = "cleaned_twitter.xlsx"
    hashtags = pd.read_excel(filename)
    hashtags = hashtags['Tweet_content']

    wordlist = {'shutdown':0, 'wall':0, 'war':0, 'immigration':0, 'jamal':0, 'trade':0, 'border':0, 'mexico':0}
    for i in hashtags:
        for k,v in wordlist.items():
            if k.lower() in i.lower():
                wordlist[k] += 1

    height = list(wordlist.values())
    bars = tuple(wordlist.keys())
    y_pos = np.arange(len(bars))

    plt.bar(y_pos, height, color=['black', 'red', 'green', 'blue', 'yellow', 'orange', 'violet', 'pink'])
    plt.xticks(y_pos, bars, rotation = 'vertical')

    plt.title("When Trump Tweets...")
    plt.ylabel("Count of Tweets")
    plt.xlabel("Tweet Word")

    plt.show()

except NameError:
    print("File Not Found")
except Exception:
    print("Error in reading")     