#FileName: SP500_WebScraping.py
#edited by dharas, mvasa, abhootra, jwasan, svpanick, sarumall 
#Last Modified: February 25, 2019

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from pandas import ExcelWriter
from urllib.error import HTTPError
from urllib.error import URLError

try:
    url = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1527825600&period2=1549688400&' + \
          'interval=1d&filter=history&frequency=1d'

    html = urlopen(url)
    bsoup = BeautifulSoup(html.read(), "lxml")

    #Rates Table
    rates_table = bsoup.findAll("table", {"class" : "W(100%) M(0)"})[0]

    #putting all columns into an empty dataframe
    col_names = []
    for tx in bsoup.find_all('th'):    
        col_names.append(tx.text.strip('*'))

    df = pd.DataFrame(columns = col_names)

    #Putting actual data into dataframe by web scraping
    rows = rates_table.findChildren(['tr'])

    i = 0
    for row in rows:
        lst = []
        cells = row.findChildren('td')
        for cell in cells:
            value = cell.string
            lst.append(value)
            #print("The value in this cell is %s" % value)
        if len(lst) == df.shape[1]:
            df.loc[i] = lst 
            i += 1

    #Writing the dataframe into Excel
    writer = ExcelWriter('S&P500_1Yr_Data.xlsx')
    df.to_excel(writer, 'Raw')

    #Cleaning the data

    df_cleaned = df

    #Removing all the commas from numeric data
    for col in df_cleaned.columns[1:]:
        df_cleaned[col] = df_cleaned[col].str.replace(',', '')  
        #Converting strs to nuemric data-type
        df_cleaned[col] = pd.to_numeric(df_cleaned[col])

    # convert column "Open" of a DataFrame from str to date type
    df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'])

    #Writing the clean dataframe into Excel
    df.to_excel(writer, 'Clean')
    writer.save()

except HTTPError as e:
    print("Error code: ", e.code)
except URLError as e:
    print("Reason: ", e.reason)