import csv
import requests
from BeautifulSoup import BeautifulSoup
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


response = requests.get("http://m.mlb.com/was/roster/transactions/")
html = response.content
list_of_rows = []
soup = BeautifulSoup(html)
table = soup.find('table')

for row in table.findAll('tr')[1:]:
	list_of_cells = []
	for cell in row.findAll('td'):
		if cell.find('a'):
			# if we find an 'a' tag, save it.
			link = cell.find('a')['href']
			list_of_cells.append(link)
			list_of_cells.append(cell.text)
		else:
			# if we don't find an 'a' tag, just save the text
			list_of_cells.append(cell.text)
	list_of_rows.append(list_of_cells)
    

outfile = open("transactions.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Date", "Url", "Text"])
writer.writerows(list_of_rows)
