import requests
from bs4 import BeautifulSoup
page=requests.get("http://www.pec.ac.in/faculty/cse")
soup = BeautifulSoup(page.content, 'html.parser')
text=list(soup.find_all('a'))
f=open('scrap','w')
for s in text:
 f.write(s.get_text())
 f.write("\n")
f.close()
