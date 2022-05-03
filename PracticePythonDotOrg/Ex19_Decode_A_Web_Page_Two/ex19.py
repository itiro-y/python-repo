# Decode a Web Page Two

import requests
from bs4 import BeautifulSoup as soup

def main():
    r = requests.get('http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
    r_html = r.text
    soup_code = soup(r_html, 'html.parser')

    #Title
    print(soup_code.find("h1", {"data-testid": "ContentHeaderHed"}).text)

    #Subtitle
    print(soup_code.find("div", {"class": "ContentHeaderDek-uqvGp cnMHcB"}).text)

    #Author of the article
    #print(soup_code.find("span", {"class": """BaseWrap-sc-TURhJ BaseText-fFzBQt BylinePreamble-igNUzc eTiIvU bpdSnf kntvqh byline__preamble"""}).text, 
         # soup_code.find("a", {"class": """BaseWrap-sc-TURhJ BaseText-fFzBQt BaseLink-gZQqBA BylineLink-eZnyPI eTiIvU BUczl gkimUc nZHeQ byline__name-link button"""}).text, '\n')

    body = soup_code.find_all("p")
    temp_list = []
    temp_list_2 = []
    for item in body:
        temp_list.append(item.text)    

    for i in range(len(temp_list)):
        if i > 0:
            if temp_list[i] != temp_list[i - 1]:
                temp_list_2.append(temp_list[i])
        else:
            temp_list_2.append(temp_list[i])   

    breaking_point = int(len(temp_list_2) / 4)
    for i in range(len(temp_list_2)):
        if i % breaking_point == 0:
            print('\n')
        else:
            print(temp_list_2[i], end='') 


if __name__ == '__main__':
    main()