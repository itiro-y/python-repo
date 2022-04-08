# Decode A Web Page

from turtle import title
import requests
from bs4 import BeautifulSoup as soup

def main():
    r = requests.get('https://www.nytimes.com/')
    r_html = r.text

    bs = soup(r_html, 'html.parser')

    news = bs.find_all("section", {"class":"story-wrapper"})

    title_list = []

    for item in news:
        temp_var = ''
        try:
            title_list.append(item.find_all("h3", {"class":"indicate-hover"})[0].text)
        except:
            pass    


    for i in range(len(title_list)):
        temp_var = ''
        if i > 0:
            if title_list[i] != title_list[i - 1]:
                print(title_list[i], '\n')
        else:
            print(title_list[i], '\n')
if __name__ == '__main__':
    main()