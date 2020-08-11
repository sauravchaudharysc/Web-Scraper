#Actually allowed to download the initital HTML
import requests
#Beautiful soup allows to use the actual HTML and grab different data so use the data that we have gathered.
from bs4 import BeautifulSoup

#to print in a better way
import pprint

#So we can think of this as web-browser that we are using without the actual data.
#We tried to grab the data from the url
res = requests.get('https://news.ycombinator.com/news')


#This will print a response text of 200
#print(res)

 
#Print all those data that we have extracted
#print(res.text)

#So this tells this is an HTML and i want to parse it
#To Convert it from a string to that we can actually use
soup = BeautifulSoup(res.text , 'html.parser')

#list all the statements with class name story link
#use dot as in css selector to select link
links = soup.select('.storylink')
#The count i.e named as score is inside the span having class subtext so we consider
#subtext in case if no score is defined it wont have an error.
subtext =  soup.select('.subtext')

#To sort the news according to votes
def sort_stories_by_votes(hn):
	return sorted(hn, key=lambda k:k['votes'],reverse=True)


def create_custom_hn(links, subtext):
 hn = []
 #we enumerate only links .
 for idx, item in enumerate(links):
 	title = item.getText()
 	href = item.get('href',None)
 	vote = subtext[idx].select('.score')
 	if len(vote):
 		points = int(vote[0].getText().replace(' points',''))
 		if points > 99:
 		  hn.append({'title': title, 'links': href , 'votes': points})
 return sort_stories_by_votes(hn)
pprint.pprint(create_custom_hn(links,subtext))


