import requests
from bs4 import BeautifulSoup


url = 'https://sports.news.naver.com/news?oid=216&aid=0000124319'

result = requests.get(url)

headers =  {'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, liek Gecko) Chrome/92.0.4515.131Safari/537'}

result = requests.get(url, headers=headers)

doc = BeautifulSoup(result.text, 'html.parser')


title = doc.select('h4.title')[0].get_text()
print(title)
