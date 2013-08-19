import csv
from bs4 import BeautifulSoup

data = {}
msaName = {}
reader=csv.reader(open('dataset.csv'), delimiter=",")
for row in reader:
	try:
		full_fips = str(row[0])
		rate = float( row[1].strip())
		msaName = str(row[2])
		data[full_fips] = rate
		msaNames[full_fips] = msaName
		print msaNames[full_fips]
		print data[full_fips]
	except:
		pass
