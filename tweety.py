#requests package which is designed to be used by humans to interact with the language
import requests

#colored an Python package from termcolor library for ANSII color formatting like HTML for output in terminal
from termcolor import colored

#Beautiful Soup an Python package from bs4 engine for parsing HTML and XML documents
from bs4 import BeautifulSoup

#making a request to twitter
req = requests.get('https://www.twitter.com/')
print(req)
page = req.content

#parsing Html Data with BeautifulSoup
soup = BeautifulSoup(page,'html.parser')

#to find all the div with class name="content"
twitter_account = soup.findAll('div', {'class': 'content'})

#to alternate the color of the texts
line=0
for tweet in twitter_account:
    print(colored ('-'*73,"yellow"))
    line = line + 1
    print(colored(tweet.strong.text,"red"))
    if line%2==0:
        print(tweet.p.text)
    else:
        print(colored(tweet.p.text,"blue"))

#preventing terminal from closing
hello = input()
print(hello)
