import sys

#For making request to other websites
import requests

#Formatting color output in terminal
from termcolor import colored

#For parsing HTML and XML documents
from bs4 import BeautifulSoup

def main():
    choice = 'Y'
    get_tweety()
    while choice == 'Y':
        print("Want to refresh Tweety (Y/N)")
        choice = input()
        if choice == 'N':
            sys.exit(1)
        print("Choose any one among the below, which you want to visit")
        print("1. Featured\n2. Sports\n3. Music\n4. Entertainment\n5. News\n6. Lifestyle")
        category = input()
        switch_tweety(category)

def switch_tweety(category):
    switcher = {
        '1': 'get_tweety()',
        '2': 'get_sports()',
        '3': 'get_music()',
        '4': 'get_entertainment()',
        '5': 'get_news()',
        '6': 'get_lifestyle()',
    }
    print(eval(switcher.get(category, "TRY AGAIN You entered an invalid input")))
            
                
#Fetching Sports category tweets
def get_sports():

    heading = "\n <- Today's Sports Tweets ->"
    print(colored(heading, 'grey'))
    #Making a request to sports category of twitter
    req = requests.get('https://twitter.com/i/streams/category/687094923246440462')  
    PAGE = req.content

    #Parsing Html Data with BeautifulSoup
    soup = BeautifulSoup(PAGE, 'html.parser')

    #To find all the div with class name="content"
    sports_tweets = soup.findAll('div', {'class': 'content'})

    #To alernate the color of texts
    line = 0 
    for sports in sports_tweets:
        #Extracting username,datetime and user's tweet
        username = sports.strong.text
        datetime = sports.small.a['title']
        user_tweet = sports.p.text.replace(u'\u200b', '*')

        #Printing the tweet's information
        print(colored('-'*80, "yellow"))
        line = line + 1
        print(colored(username, "red"))
        print(colored(datetime,"cyan"))
        if line%2 == 0:
            print(user_tweet)
        else:
            print(colored(user_tweet, "grey"))


#Fetching Music category tweets
def get_music():

    heading = "\n <- Today's Music Tweets ->"
    print(colored(heading, 'blue'))
    #Making a request to Music category of twitter
    req = requests.get('https://twitter.com/i/streams/category/687094923246440475')  
    PAGE = req.content

    #Parsing Html Data with BeautifulSoup
    soup = BeautifulSoup(PAGE, 'html.parser')

    #To find all the div with class name="content"
    music_tweets = soup.findAll('div', {'class': 'content'})

    #To alernate the color of texts
    line = 0 
    for music in music_tweets:
        #Extracting username,datetime and user's tweet
        username = music.strong.text
        datetime = music.small.a['title']
        user_tweet = music.p.text.replace(u'\u200b', '*')

        #Printing the tweet's information
        print(colored('-'*80, "yellow"))
        line = line + 1
        print(colored(username, "red"))
        print(colored(datetime,"cyan"))
        if line%2 == 0:
            print(user_tweet)
        else:
            print(colored(user_tweet, "blue"))


#Fetching Entertainment category tweets
def get_entertainment():

    heading = "\n <- Today's Entertainment Tweets ->"
    print(colored(heading, 'green'))
    #Making a request to entertainment category of twitter
    req = requests.get('https://twitter.com/i/streams/category/687094923246440457')  
    PAGE = req.content

    #Parsing Html Data with BeautifulSoup
    soup = BeautifulSoup(PAGE, 'html.parser')

    #To find all the div with class name="content"
    entertainment_tweets = soup.findAll('div', {'class': 'content'})

    #To alernate the color of texts
    line = 0 
    for entertainment in entertainment_tweets:
        #Extracting username,datetime and user's tweet
        username = entertainment.strong.text
        datetime = entertainment.small.a['title']
        user_tweet = entertainment.p.text.replace(u'\u200b', '*')

        #Printing the tweet's information
        print(colored('-'*80, "yellow"))
        line = line + 1
        print(colored(username, "red"))
        print(colored(datetime,"cyan"))
        if line%2 == 0:
            print(user_tweet)
        else:
            print(colored(user_tweet, "green"))


#Fetching News category tweets
def get_news():

    heading = "\n <- Today's News Tweets ->"
    print(colored(heading, 'red'))
    #Making a request to news category of twitter
    req = requests.get('https://twitter.com/i/streams/category/687094923246440476')  
    PAGE = req.content

    #Parsing Html Data with BeautifulSoup
    soup = BeautifulSoup(PAGE, 'html.parser')

    #To find all the div with class name="content"
    news_tweets = soup.findAll('div', {'class': 'content'})

    #To alernate the color of texts
    line = 0 
    for news in news_tweets:
        #Extracting username,datetime and user's tweet
        username = news.strong.text
        datetime = news.small.a['title']
        user_tweet = news.p.text.replace(u'\u200b', '*')

        #Printing the tweet's information
        print(colored('-'*80, "yellow"))
        line = line + 1
        print(colored(username, "red"))
        print(colored(datetime,"cyan"))
        if line%2 == 0:
            print(user_tweet)
        else:
            print(colored(user_tweet, "red")) 


#Fetching Lifestyle category tweets
def get_lifestyle():

    heading = "\n <- Today's Lifestyle Tweets ->"
    print(colored(heading, 'cyan'))
    #Making a request to lifestyle category of twitter
    req = requests.get('https://twitter.com/i/streams/category/776655075057868800')  
    PAGE = req.content

    #Parsing Html Data with BeautifulSoup
    soup = BeautifulSoup(PAGE, 'html.parser')

    #To find all the div with class name="content"
    lifestyle_tweets = soup.findAll('div', {'class': 'content'})

    #To alernate the color of texts
    line = 0 
    for lifestyle in lifestyle_tweets:
        #Extracting username,datetime and user's tweet
        username = lifestyle.strong.text
        datetime = lifestyle.small.a['title']
        user_tweet = lifestyle.p.text.replace(u'\u200b', '*')

        #Printing the tweet's information
        print(colored('-'*80, "yellow"))
        line = line + 1
        print(colored(username, "red"))
        print(colored(datetime,"cyan"))
        if line%2 == 0:
            print(user_tweet)
        else:
            print(colored(user_tweet, "cyan"))


# Fetching tweets
def get_tweety(): 
    wait = "Please be patient, Your Tweety is fetching the tweets for you..."
    print(colored(wait, 'green'))

    #Making a request to twitter
    req = requests.get('https://www.twitter.com/')
    heading = "\n <-  Today's Featured Tweets  ->"

    print(colored(heading, 'blue'))
    PAGE = req.content

    #Parsing Html Data with BeautifulSoup
    soup = BeautifulSoup(PAGE, 'html.parser')

    #To find all the div with class name="content"
    twitter_account = soup.findAll('div', {'class': 'tweet'})

    #To alternate the color of the texts
    line = 0
    for tweet in twitter_account:
        #Extracting username,datetime and user's tweet
        username = tweet.strong.text
        datetime = tweet.small.a['title']
        user_tweet = tweet.p.text.replace(u'\u200b', '*')

        #Printing the tweet's information
        print(colored('-'*80, "yellow"))
        line = line + 1
        print(colored(username, "red"))
        print(colored(datetime,"cyan"))
        if line%2 == 0:
            print(user_tweet)
        else:
            print(colored(user_tweet, "blue"))

if __name__=="__main__": main()
