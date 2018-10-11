from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup as bsp

### extract multiple URLs from a URL 
### and write them on a txt file
fw1 = open("urls_to_read.txt", 'w')

url = input("URL을 입력하세요: ")
html = urlopen(url)
bsObj = bsp(html.read(), 'html.parser')

for link in bsObj.find_all('a'):
    fw1.write(str(link.get('href'))+"\n")

fw1.close()

### make URLs blacklist
lis = []
li = 'a'

leng = input('크롤링 하지 않을 URL의 개수: ')
for i in range(int(leng)):
    li = input('%dth URL: ' %(i+1))
    lis.append(li)

for j in lis:
    print(j)

### print and write dump in a txt file
fr = open("urls_to_read.txt", 'r')
fw2 = open("dump_results.txt", 'w')

while True:
    check=0
    front = fr.readline()
    url = 'declare'

    # EOF
    if not front: break

    # check the blacklist
    for k in lis:
        if front == k:
            check += 1
    
    if check > 0:
        continue

    # normies
    if front[:4] == 'http':
        url = front
    else: continue

    # parsing and get pure text
    req=requests.get(url)
    soup=bsp(req.content,'html.parser')
    desc=soup.find_all("p")

    for i in desc:
        print(i.text)
        fw2.write(str(i.text))
    print("URL: "+str(url))

fr.close()
fw2.close()
