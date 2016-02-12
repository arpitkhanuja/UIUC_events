from bs4 import BeautifulSoup
from crawler import Crawler
import urllib2

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

class CalendarCrawler(Crawler):

	def __init__(self, dbname=""):
		Crawler.__init__(self, dbname)

	def crawl(self, url):
		site = urllib2.urlopen(url)
		soup = BeautifulSoup(site.read(), "lxml")

		for week_list_row in soup.findAll("li", attrs={"class": "week-list-row"}):
			date = ' '.join(week_list_row.h3.text.split())
			print date
			for event in week_list_row.findAll("li"):
				event_time = event.find(attrs={"class": "event-time"}).text
				event_desc = event.find(attrs={"class": "event-name"}).text
				print event_time + " " + event_desc 

			print 

if __name__ == "__main__":
	crawler = CalenderCrawler("")
	crawler.crawl("http://illinois.edu/calendar/list/7")