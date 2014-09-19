#!/usr/bin/python3.4
import requests
from bs4 import BeautifulSoup
from twython import Twython
from twython import TwythonStreamer
from keys import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET #HIDING MY PERSONAL INFO FROM YOU GUYS


def url_generator(user_input):
    #this generates a search URL from bing, given the user's input
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
    #this function takes in the beautifully formatted html, called 'soup'
    #it parses the soup for the time
    #in this case there are three possibilities in the html of what the time could be
    #because there are three possibilities we use try and excepts to catch any errors

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



class MyStreamer(TwythonStreamer):


    twitter =  Twython(APP_KEY ,APP_SECRET ,OAUTH_TOKEN ,OAUTH_TOKEN_SECRET)
    def on_success(self, data):
        if 'text' in data: #text is a dictionary item in data
            tweet = data['text']
            tweet = tweet.replace('@whatsthetimebot','')
            tweet = 'What time is it in' + tweet
            website_url = url_generator(tweet)
            r = requests.get(website_url)
            soup = BeautifulSoup(r.content)
            tweet = get_string_from_bing(soup)
            success = False
            for i in range(0,len(tweet) - 1): #if there is a number in the tweet. Lazy programming...
                if tweet[i].isdigit():
                    tweet = '@' + str(data['user']['screen_name']) + ' ' + tweet
                    MyStreamer.twitter.update_status(status = tweet ,in_reply_to_status_id = data['id'])
                    success = True
                    break
            if(success == False):
                tweet = '@' + str(data['user']['screen_name']) + ' ' + 'Try tweeting:"What time is it in (location)"'
                MyStreamer.twitter.update_status(status = tweet ,in_reply_to_status_id = data['id'])



    def on_error(self, status_code, data):
        print(status_code)

def main():

    stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    stream.statuses.filter(track = '@whatsthetimebot')

main()