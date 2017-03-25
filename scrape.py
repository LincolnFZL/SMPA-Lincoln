import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
    	list_of_cells.append(cell.text)
    # loop over the cells
    # and append them to the list_of_cells
    list_of_rows.append(list_of_cells)
    

outfile = open("executions.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Schedules_Executions", "Linck", "Last_Name", "First_Name", "TDCJ_Number", "Date_of_Birth", "Race", "Date_Received", "County"])
writer.writerows(list_of_rows)
