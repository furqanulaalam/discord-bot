from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://www.iustlive.com/Index/Default.aspx").text
base_url = "https://www.iustlive.com"

soup = BeautifulSoup(source, 'lxml')

csv_file = open("notifications.csv",'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Notifications', 'Links'])

content = soup.find('div', id = "main-content")
table = content.find('table')
rows = table.find_all('tr')

for item in rows:
    try:
        n_url = item.td.a['href'].split('..')
        csv_writer.writerow([item.td.a.text, base_url + n_url[1]])
    except:
        pass
    
csv_file.close()    