
from pip._vendor import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA'
    req = requests.get(url)
    req_html = req.text

    soup = BeautifulSoup(req_html, 'html.parser')
    links = soup.find_all('a')
    # for link in links:
    #     print(f"<a href = {link.get('href')}> <{link.text}>")

    g_data = soup.find_all("div", {"class":"info"})

    for item in g_data:
        print(item.contents[0].find_all("a", {"class":"business-name"}))
        print(item.contents[1].find_all("div", {"class":"street-address"})[0].text)
        print(item.contents[1].find_all("div", {"class":"locality"})[0].text)
        print(item.contents[1].find_all("div", {"class":"phones"})[0].text, '\n')



if __name__ == '__main__':
    main()