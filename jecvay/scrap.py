import requests
import BeautifulSoup

response = requests.get("http://www.zhihu.com")
soup = BeautifulSoup.BeautifulSoup(response.text)
xsrf = soup.find("input", {"name": "_xsrf"})["value"]
print xsrf


