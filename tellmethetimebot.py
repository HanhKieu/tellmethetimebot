#!/usr/bin/python3.4
import requests
from bs4 import BeautifulSoup
from twython import Twython
from twython import TwythonStreamer

def url_generator(user_input):
    words = user_input.split(" ")
    website_url = "http://www.bing.com/search?q="
    count = 0
    for word in words:
        if(count == (len(words) - 1) ):
            website_url = website_url + word
            break
        website_url = website_url + word + "+"
        count = count + 1

    return website_url



def get_string_from_bing(soup):
    current_time_text = soup.find_all("div", class_="b_focusLabel")
    current_time = soup.find_all("div", class_="b_focusTextLarge")
    standard_time = soup.find_all("div", class_="b_factrow")

    bing_string = ""
    try:
        bing_string = current_time_text[0].text + " " +  bing_string
    except:
        pass
    try:
        bing_string = current_time[0].text + " " + bing_string
    except:
        pass
    try:
        bing_string = standard_time[0].text + " " + bing_string
    except:
        pass

    return bing_string



def main():

    APP_KEY = 'rwYJa5yvkPvLcfEE6k5wa476v'
    APP_SECRET = 'tDmmgdbWhZHtzBKbJih5rrXdlX7hlKRBuw5W9vzCPygDtZLfKN'

    OAUTH_TOKEN = '2718807608-M1MQLQrdrOBQ6lDXdOuvZY5GyJKA1yQLmVF3Gzs'
    OAUTH_TOKEN_SECRET = '1HiTaubCcn36SlaSFrZvEnlELRL9bBWAcMyIYqBCaPm95'

    twitter =  Twython(APP_KEY ,APP_SECRET ,OAUTH_TOKEN ,OAUTH_TOKEN_SECRET)






    class MyStreamer(TwythonStreamer):
        def on_success(self, data):
            if 'text' in data:
                #print(data['text'].encode('utf-8'))
                tweet = data['text']
                tweet = tweet.replace('@whatsthetimebot','')
                print(tweet)



        def on_error(self, status_code, data):
            print(status_code)



    stream = MyStreamer(APP_KEY, APP_SECRET,
                        OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track = '@whatsthetimebot')


    # user_input = input("Enter Query Request: ")
    # website_url = url_generator(user_input)
    # r = requests.get(website_url)
    # soup = BeautifulSoup(r.content)
    # tweet = get_string_from_bing(soup)
    # print(tweet)



main()