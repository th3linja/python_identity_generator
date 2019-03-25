from bs4 import BeautifulSoup
import requests

def strp_value(str):
    try:
        if ('value="') in str:
            text_beg = str.index('value="') + 7
            text_end = str.index('"/></div>')
            str = str[text_beg:text_end]
            return str
        if ('<p>') in str:
            text_beg = str.index('<p>') + 3
            text_end = str.index('</p>')
            str = str[text_beg:text_end]
            return str
        return str
    except ValueError:
        print("error:")

data_string = []

url = 'https://www.fakepersongenerator.com/'
page = requests.get(url)
resp = requests.head(url)

soup = BeautifulSoup(page.content, 'html.parser')
category = soup.select('.info-title')
data = soup.select('.info-detail')


for c in range(len(category)):
    category[c] = category[c].string.strip()

for d in range(len(data)):
    data[d] = strp_value(str(data[d]))
    data[d] = data[d].replace('&lt;', '<')
    data[d] = data[d].replace('<br/>', '\n\t\t')

print("ID Generator")
for i in range(len(data)):
    print(category[i] + ': ' + data[i])

print()
print(resp.text, resp.headers)
print(category)
print(data)