from bs4 import BeautifulSoup
import requests
import pprint

def create_custom_list(links,subtext):
	hn =[]
	for index,item in enumerate(links):
		title=item.getText()
		href= item.get('href',None)
		vote = subtext[index].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points',''))
			if points>100:
				hn.append({'title':title,'links': href,'points':points})
	return hn

pp = pprint.PrettyPrinter(indent=4)

def abc(i):
	res = requests.get(f'https://news.ycombinator.com/news?p={i}')
	soup = BeautifulSoup(res.text,'html.parser')
	links = soup.select('.storylink')
	subtext= soup.select('.subtext')
	return sorted(create_custom_list(links, subtext),reverse=True,key=lambda k:k['points'])

pp.pprint(abc('1'))
pp.pprint(abc('2'))