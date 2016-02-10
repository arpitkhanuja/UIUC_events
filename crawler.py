class Crawler:
	def __init__(self, dbname=""):
		pass

	def __del__(self):
		pass

	def dbCommit(self):
		pass

	def getEntryID(self, table, field, value, createnew=True):
		return None

	def addToIndexx(self, url, soup):
		print "Indexing %s" % url

	def getTextOnly(self, soup):
		return None

	def separateWords(self, text):
		return None

	def isIndexed(self, url):
		return False

	def addLinkRef(self, urlFrom, urlTo, linkText):
		pass

	def crawl(self, pages, depth=2):
		pass

	def createIndexTables(self):
		pass

if __name__ == "__main__":
	print __name__