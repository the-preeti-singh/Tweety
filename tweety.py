import requests
from termcolor import colored

from bs4 import BeautifulSoup

req = requests.get('https://www.twitter.com/')
print(req)
page = req.content
soup = BeautifulSoup(page,'html.parser')

twitter_account = soup.findAll('div', {'class': 'content'})

line=0
for tweet in twitter_account:
    print(colored ('-'*73,"yellow"))
    line = line + 1
    print(colored(tweet.strong.text,"red"))
    if line%2==0:
        print(tweet.p.text)
    else:
        print(colored(tweet.p.text,"blue"))
hello = input()
print(hello)
