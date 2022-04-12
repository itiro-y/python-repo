# Write to a File

import requests
from bs4 import BeautifulSoup as soup

def main():
    r = requests.get('https://www.nytimes.com/')
    r_html = r.text

    bs = soup(r_html, 'html.parser')

    news = bs.find_all("section", {"class":"story-wrapper"})

    title_list = []

    for item in news:
        try:
            title_list.append(item.find_all("h3", {"class":"indicate-hover"})[0].text)
        except:
            pass

    file_name = input(str('What is the file name? \n > '))

    for i in range(len(title_list)):
        if i > 0:
            if title_list[i] != title_list[i - 1]:
                with open(f'/PythonStuff/PracticePythonDotOrg/{file_name}.txt', 'a') as f:
                    f.write(f'{str(title_list[i])} \n')
        else:
            with open(f'/PythonStuff/PracticePythonDotOrg/{file_name}.txt', 'a') as f:
                f.write(f'{str(title_list[i])} \n')
            

if __name__ == '__main__':
    main()