#!/usr/bin/python3.4


def url_generator(user_input):
    words = user_input.split(" ")
    website_url = "https://www.google.com/#q="
    count = 0
    for word in words:
        if(count == (len(words) - 1) ):
            website_url = website_url + word
            break
        website_url = website_url + word + "+"
        count = count + 1

    return website_url



def main():

    user_input = "what time is it in china"
    website_url = url_generator(user_input)

    print(website_url)


main()

