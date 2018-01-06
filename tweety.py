#For making request to other websites
import requests

#Formatting color output in terminal
from termcolor import colored

#For parsing HTML and XML documents
from bs4 import BeautifulSoup

if __name__ =="__main__":
    wait = "Please be patient, Your Tweety is fetching the tweets for you..."

    print(colored(wait, 'green'))

    #Making a request to twitter
    req = requests.get('https://www.twitter.com/')
    print("\n <-  Today's Featured Tweets  ->")
    PAGE = req.content

    #Parsing Html Data with BeautifulSoup
    soup = BeautifulSoup(PAGE, 'html.parser')

    #To find all the div with class name="content"
    twitter_account = soup.findAll('div', {'class': 'content'})

    #To alternate the color of the texts
    line = 0
    for tweet in twitter_account:
        #Extracting username,datetime and user's tweet
        username = tweet.strong.text
        datetime = tweet.small.a['title']
        user_tweet = tweet.p.text
    
        #Printing the tweet's information
        print(colored('-'*80, "yellow"))
        line = line + 1
        print(colored(username, "red"))
        print(colored(datetime,"cyan"))
        if line%2 == 0:
            print(user_tweet)
        else:
            print(colored(user_tweet, "blue"))

    #Preventing terminal from closing
    hello = input()
    print(hello)
