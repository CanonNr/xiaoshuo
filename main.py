import requests
from bs4 import BeautifulSoup


def get_list():
    root_url = "xxxx"
    r = requests.get(root_url)
    r.encoding = "gbk"
    soup = BeautifulSoup(r.text, "html.parser")

    url_list = []
    for dd in soup.find_all("dd"):
        link = dd.find("a")
        if not link:
            continue
        url_list.append(("xxxx" % link['href'], link.get_text()))
        #print(link)

   # print(url_list)
    return url_list

def get_content(url):
    r = requests.get(url)
    r.encoding = "gbk"
    soup = BeautifulSoup(r.text, "html.parser")
    s = soup.find("div", id='content').get_text('\r\n \r\n ', "<br>")
    return s
    #return s.replace(u'\xa0', '')

def save(url, title):
    with open("result.txt", "a+", encoding='utf-8') as out:
        out.write(title)
        out.write('\r\n')
        out.write('\r\n')
        out.write('\r\n')
        out.write('\r\n')
        out.write(get_content(url))
        out.write('\r\n')
        out.write('\r\n')
        out.write('\r\n')
        out.write('\r\n')


for item in get_list():
    save(item[0], item[1])
    print(item[1])
