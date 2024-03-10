import requests
from bs4 import BeautifulSoup
import pandas as pd

df=pd.read_excel(r"C:\workspace\Lauterbach & Amen\test.xlsx")

i = 1
act_text = []

while i <= 27:
    URL = f"https://insidepublicaccounting.com/category/mergers-acquisitions/page/{i}"
    page = requests.get(URL, headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36}"})

    soup = BeautifulSoup(page.content, "html.parser")

    link = soup.find_all("div", class_="elementor elementor-1000005770")
    for links in link:
        content = links.find_all("h3", class_="gp-post-title")

    link_lst = []
    
    for val in content:
        act_link = val.find("a")
        click_link = act_link["href"]
        if len(link_lst) <= 11:
            link_lst.append(click_link)
    print(len(link_lst))

    for url in link_lst:
        act_page = requests.get(url, headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36}"})
        act_soup = BeautifulSoup(act_page.content, "html.parser")
        text = act_soup.find("div", class_="gp-element-post-content")
        act_text.append(text.text.strip())

    print(i)
    i += 1

if i > 27:
    df.insert(loc = 0, column = "Results", value = act_text)
    df.to_csv('C:\workspace\Lauterbach & Amen\scraped.csv',sep=",",index=False,encoding='utf-16')


