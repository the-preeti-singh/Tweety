#For making request to other websites
import requests

#Formatting color output in terminal
from termcolor import colored

#For parsing HTML and XML documents
from bs4 import BeautifulSoup

#Making a request to twitter
req = requests.get('https://www.twitter.com/')
PAGE = req.content

#Parsing Html Data with BeautifulSoup
soup = BeautifulSoup(PAGE, 'html.parser')

#To find all the div with class name="content"
twitter_account = soup.findAll('div', {'class': 'content'})

#To alternate the color of the texts
line = 0
for tweet in twitter_account:
    print(colored('-'*80, "yellow"))
    line = line + 1
    print(colored(tweet.strong.text, "red"))
    if line%2 == 0:
        print(tweet.p.text)
    else:
        print(colored(tweet.p.text, "blue"))

#preventing terminal from closing
hello = input()
print(hello)
