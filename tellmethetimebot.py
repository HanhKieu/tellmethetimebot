#!/usr/bin/python3.4
import requests
from bs4 import BeautifulSoup

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


    user_input = input("Enter Query Request: ")
    website_url = url_generator(user_input)
    r = requests.get(website_url)
    soup = BeautifulSoup(r.content)
    tweet = get_string_from_bing(soup)
    print(tweet)

main()