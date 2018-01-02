import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.twitter.com/')
print(req)
page = req.content

soup = BeautifulSoup(page,'html.parser')

mera_moto = soup.findAll('p', {'class': 'tweet-text'})
    
for moto in mera_moto:
    print('----------------------------------------------------------------------')
    print(moto.text)    
     
hello = input()
print(hello)
