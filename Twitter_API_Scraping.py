#!/usr/bin/env python
# -*- coding: utf-8 -*-

#FileName: Twitter_API_Scraping.py
#edited by dharas, mvasa, abhootra, jwasan, svpanick, sarumall 
#Last Modified: February 25, 2019

import csv

#http://www.tweepy.org/
import tweepy

#Twitter API credentials entered here
consumer_key = "uHsc3zSnRlhB4vlukHTW3yf52" 
consumer_secret = "nFCXtts9rTkS9IJ5iHZmWvLZznSAGsEDPLZSlLB5u4GCZhChnB"
access_key = "753116747553701888-b8GOBBovkQj8tC0EEgQuwX5CKyYqG5f"
access_secret = "SQ8PcOUaxpK2LDrkT34y3P8B90gy4PByFOzPPbxi8kDpC"

#method to get a user's last tweets
def get_tweets(username):
    #http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    #set count to however many tweets you want
    number_of_tweets = 10000
    #get tweets
    tweets_for_csv = []
 
    
    for tweet in tweepy.Cursor(api.user_timeline, screen_name = username, tweet_mode="extended").items(number_of_tweets):
    
		#create array of tweet information: username, tweet id, date/time, text     
        tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8")])
        #write to a new csv file from the array of tweets
        outfile = username + "_tweets.csv"#Name of file where tweets will be saved
        
        with open(outfile, 'w+') as file:
            writer = csv.writer(file, delimiter=',')#Write the file
            writer.writerows(tweets_for_csv)
        
get_tweets("realDonaldTrump")#pass donald trump's user_id as parameter