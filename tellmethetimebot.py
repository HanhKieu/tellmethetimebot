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

def initiate_read():
    APP_KEY = 'rwYJa5yvkPvLcfEE6k5wa476v'
    APP_SECRET = 'tDmmgdbWhZHtzBKbJih5rrXdlX7hlKRBuw5W9vzCPygDtZLfKN'
    #APPKEY AND SECRET ARE FOR 0AUTH2, READ ONLY , NO WRITING TO TWITTER
    twitter = Twython(APP_KEY , APP_SECRET, oauth_version = 2)
    ACCESS_TOKEN = twitter.obtain_access_token()
    return Twython(APP_KEY, access_token= ACCESS_TOKEN)



def initiate_write():
    APP_KEY = 'rwYJa5yvkPvLcfEE6k5wa476v'
    APP_SECRET = 'tDmmgdbWhZHtzBKbJih5rrXdlX7hlKRBuw5W9vzCPygDtZLfKN'
    # twitter = Twython(APP_KEY,APP_SECRET)
    OAUTH_TOKEN = '2718807608-M1MQLQrdrOBQ6lDXdOuvZY5GyJKA1yQLmVF3Gzs'
    OAUTH_TOKEN_SECRET = '1HiTaubCcn36SlaSFrZvEnlELRL9bBWAcMyIYqBCaPm95'
    # auth = twitter.get_authentication_tokens(callback_url= None)
    #
    # OAUTH_TOKEN = auth['oauth_token']
    # OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
    #
    # twitter = Twython(APP_KEY,APP_SECRET,
    #                   OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
    # print(auth)
    # pin_input = input("enter pin here")
    # final_step = twitter.get_authorized_tokens(pin_input)
    # OAUTH_TOKEN = final_step['oauth_token']
    # OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']
    #
    # print(OAUTH_TOKEN)
    # print(OAUTH_TOKEN_SECRET)

    return Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

def main():


    twitter_read = initiate_read()
    twitter = initiate_write()
    twitter.update_status(status = "suck my dddWERWERdass")
    timeline = twitter_read.get_user_timeline(screen_name = 'hailthekid' , count = 3)
    print(timeline[2]['text'])



    # user_input = input("Enter Query Request: ")
    # website_url = url_generator(user_input)
    # r = requests.get(website_url)
    # soup = BeautifulSoup(r.content)
    # tweet = get_string_from_bing(soup)
    # print(tweet)



main()