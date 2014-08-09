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



def main():


    file_object = open("html.txt","w")
    user_input = "what time is it in china"
    website_url = url_generator(user_input)
    r = requests.get(website_url)
    soup = BeautifulSoup(r.content)
    file_object.write(soup.prettify())
main()
