#FileName: Southwest_Scraping.py
#edited by dharas, mvasa, abhootra, jwasan, svpanick, sarumall 
#Last Modified: February 25, 2019

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from pandas import ExcelWriter
import numpy as np
from urllib.error import HTTPError
from urllib.error import URLError

#FileName: Southwest_Scraping.py
#edited by dharas, mvasa, abhootra, jwasan, svpanick, sarumall 
#Last Modified: February 25, 2019

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from pandas import ExcelWriter
import numpy as np
from urllib.error import HTTPError
from urllib.error import URLError

try:
    url = 'https://www.nasdaq.com/symbol/luv/historical'

    html = urlopen(url)
    bsoup = BeautifulSoup(html.read(), "lxml")

    #Rates Table
    rates_table = bsoup.findAll("div", {"id" : "quotes_content_left_pnlAJAX"})[0]

    #putting all columns into an empty dataframe
    df = pd.DataFrame(columns = ['Date','Open','High','Low','Close/Last','Volume'])

    #Putting actual data into dataframe by web scraping

    rows = rates_table.findChildren(['tr'])

    i = 0
    for row in rows:
        lst = []
        cells = row.findChildren('td')

        for cell in cells:
            value = cell.string
            lst.append(value)
        if len(lst) == df.shape[1]:
            df.loc[i] = lst 
            i += 1

    #Writing the dataframe into Excel
    output_filename = 'Southwest.xlsx'
    writer = ExcelWriter(output_filename)
    df.to_excel(writer)
    writer.save()

except HTTPError as e:
    print("Error code: ", e.code)
except URLError as e:
    print("Reason: ", e.reason)