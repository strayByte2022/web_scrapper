from bs4 import BeautifulSoup
import requests
import check_status 
#url
url = "https://ditmewibu.com"
#Status code of the web
print("Status code of web: ", check_status.get_status(url).status_code)
#Scrap html source code 
code = check_status.get_status(url)._content.decode('utf-8')
#print(type(check_status.get_status(url)._content.decode('utf-8')))
f = open('web_source.txt','w')
f.write(code)
f.close()
#scrap content 
content = check_status.get_status(url).content
soup = BeautifulSoup(content,"html.parser")
# Find all <a> tags
links = soup.find_all("p")

# Find all elements with a specific class
elements = soup.find_all(class_="center")

# Find an element by ID
element = soup.find(id="t5-p5")
for link in links:
    print(link.get_text())
