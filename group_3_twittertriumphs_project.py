#FileName: group_3_twittertriumphs_project.py
#Main File
#edited by dharas, mvasa, abhootra, jwasan, svpanick, sarumall 
#Last Modified: February 25, 2019

#if we're running this as a script
#Running the main module displaying the flow of application

if __name__ == '__main__':
	print("Welcome to Twitter Triumphs\n\n")
	print("-----Data Collection and Data Cleaning-----")
	print("Step 1. Scraping Twitter Data through Twitter API")
	print("Step 2. Scraping S&P500 Data through Yahoo Finance")
	print("Step 3. Scraping Airline Stock Data through NASDAQ")
	print("-----Visualizations-----")
	
#Importing the below modules

#This module scrapes the S&P500 historical stock data from Yahoo Finance
import SP500_WebScraping
#This module scrapes Doanld Trump's Twitter data using tweepy and Twitter API
import Twitter_API_Scraping
#These modules scrape the Airline Industry historical Stock data from NASDAQ for 4 major Airlines given below
import Southwest_Scraping
import Delta_Scraping
import American_Scraping
import JetBlue_Scraping
#For merging
import Clean_Merge_Data
#This module creates all the visualizations on the scraped data
import Visualizations
import China_Trade_Visualization
import Airline_Visualization
