import csv
from bs4 import BeautifulSoup

data = {}
msaNames = {}
reader=csv.reader(open('dataset.csv'), delimiter=",")
for row in reader:
	try:
		
		full_fips = row[0]
		
		rate = float( row[1].strip())
		msaName = row[2]
		data[full_fips] = rate
		msaNames[full_fips] = msaName
	except:
		pass


svg = open ('USA_Counties_with_FIPS_and_names.svg' , 'r').read()

soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])

paths = soup.findAll('path')

colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]

path_style = "font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:"


for p in paths:

	if p['id'] not in ["State_Lines", "separator"]:
        # pass
		try:
			rate = data[p['id']]
			geoName = msaNames[p['id']]
		except:
			continue


		if rate > 80:
			color_class = 5
		elif rate > 50:
			color_class = 4
		elif rate > 40:
			color_class = 3
		elif rate > 30:
			color_class = 2
		elif rate > 20:
			color_class = 1
		else:
			color_class = 0

		color = colors[color_class]
		p['style'] = path_style + color
		new_tag = soup.new_tag("title")
		new_tag.string=geoName
		p.append(new_tag)
		

print soup.prettify()
