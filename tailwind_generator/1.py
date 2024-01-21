from bs4 import BeautifulSoup

with open('static/files/base.html', 'r') as html:
    base = BeautifulSoup(html.read(), 'html.parser')

with open('static/files/for_header.html', 'r') as html:
    for_header = BeautifulSoup(html.read(), 'html.parser')

base.find('header').insert(0, for_header)
print(base.prettify())

file2 = open('static/files/file2.html', 'w+', encoding='utf-8')
file2.write(base.prettify())
file2.close()

# soup = BeautifulSoup(html, 'html.parser')

# soup.find('head').insert(4, 'YYYY')
# print(soup.prettify())