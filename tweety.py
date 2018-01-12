import sys

#For making request to other websites
import requests

#Formatting color output in terminal
from termcolor import colored

#For parsing HTML and XML documents
from bs4 import BeautifulSoup

def main():
    choice = 'Y'
    while choice == 'Y':
        get_tweety()
        print("Want to refresh Tweety (Y/N)")
        choice = input()
        if choice == 'N':
            sys.exit(1)
        else:
            print("Choose any one among the below, which you want to visit")
            print("1. Featured\n2. Sports\n3. Music\n4. Entertainment\n5. News\n6. Lifestyle")
            category = input()
          
            def switch_tweety(category):
                switcher = {
                    1: get_tweety(),
                    2: get_sports(),
                    3: get_music(),
                    4: get_entertainment(),
                    5: get_news(),
                    6: get_lifestyle()
                }
                print(switcher.get(category, "TRY AGAIN You entered an invalid input"))


#Fetching Sports category tweets
def get_sports():

    #Making a request to sports category of twitter
    req = requests.get('https://twitter.com/i/streams/category/687094923246440462')  
    print("\n <- Today's Sports Tweets ->")
    PAGE = re.content

    #Parsing Html Data with BeautifulSoup
    soup = BeautifulSoup(PAGE, 'html.parser')

    #To find all the div with class name="content"
    sports_tweets = soup.findAll('div', {'class': 'content'})

    #To alernate the color of texts
    line = 0 
    for sports in sports_tweets:
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


#Fetching Music category tweets
def get_music():

    #Making a request to Music category of twitter
    req = requests.get('https://twitter.com/i/streams/category/687094923246440475')  
    print("\n <- Today's Music Tweets ->")
    PAGE = re.content

    #Parsing Html Data with BeautifulSoup
    soup = BeautifulSoup(PAGE, 'html.parser')

    #To find all the div with class name="content"
    music_tweets = soup.findAll('div', {'class': 'content'})

    #To alernate the color of texts
    line = 0 
    for music in music_tweets:
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


#Fetching Entertainment category tweets
def get_entertainment():

    #Making a request to entertainment category of twitter
    req = requests.get('https://twitter.com/i/streams/category/687094923246440457')  
    print("\n <- Today's Entertainment Tweets ->")
    PAGE = re.content

    #Parsing Html Data with BeautifulSoup
    soup = BeautifulSoup(PAGE, 'html.parser')

    #To find all the div with class name="content"
    entertainment_tweets = soup.findAll('div', {'class': 'content'})

    #To alernate the color of texts
    line = 0 
    for entertainment in entertainment_tweets:
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


#Fetching News category tweets
def get_news():

    #Making a request to news category of twitter
    req = requests.get('https://twitter.com/i/streams/category/687094923246440476')  
    print("\n <- Today's News Tweets ->")
    PAGE = re.content

    #Parsing Html Data with BeautifulSoup
    soup = BeautifulSoup(PAGE, 'html.parser')

    #To find all the div with class name="content"
    news_tweets = soup.findAll('div', {'class': 'content'})

    #To alernate the color of texts
    line = 0 
    for news in news_tweets:
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


#Fetching Lifestyle category tweets
def get_lifestyle():

    #Making a request to lifestyle category of twitter
    req = requests.get('https://twitter.com/i/streams/category/776655075057868800')  
    print("\n <- Today's Lifestyle Tweets ->")
    PAGE = re.content

    #Parsing Html Data with BeautifulSoup
    soup = BeautifulSoup(PAGE, 'html.parser')

    #To find all the div with class name="content"
    lifestyle_tweets = soup.findAll('div', {'class': 'content'})

    #To alernate the color of texts
    line = 0 
    for lifestyle in lifestyle_tweets:
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


# Fetching tweets
def get_tweety():
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

if __name__ =="__main__": main()
    
