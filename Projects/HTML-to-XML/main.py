from bs4 import BeautifulSoup 

file = r"E:\angular projects\mean gym\gym-mean-stack\src\app\pages\header\header\header.component.html"

with open(file, 'r', encoding='utf8') as html:
    soup = BeautifulSoup(html, "html.parser")
    # print(soup)

lines = soup.prettify().splitlines()
# print(lines)
content = "\n".join(lines[1:])
# print(content)

with open("output.xml", "w", encoding='utf8') as XML:
    XML.write(content)
