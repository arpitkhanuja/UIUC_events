from bs4 import BeautifulSoup
import SimpleHTTPServer
import SocketServer
import requests
import os
import metamind.api as f00d

api_key = '2EWTUU-EHG8K6HLRJ'
meta_key = 'JmcPgWqRabTIZKNNWfflIoOhRduQaHzp8BVXHtaS2QqBVKmfU7'

class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		pass

	def do_POST(self):
		try:
			arr = self.rfile.read(int(self.headers.getheader('Content-Length')))
			out = open('out', 'wb')
			out.write(arr)
			out.close()
			# os.remove('out')
			res = classifier.predict(['out'], input_type="files")
			food = res[0]['label']
			query = "+".join(food.split())
			r = get_xml(query)
			string = parse_query(r)
			shit = (process_result(string))
			dasani = ''
			for poop in shit:
			    if poop[0] != '%' and poop[0] != '*' and poop[0] != '(':
			        dasani += (str(poop).strip())
			self.send_response(200)
			# self.send_header("Content-Type", "application/json")
			self.end_headers()
			self.wfile.write(dasani)
		except:
			pass

def preprocess_query(query):
    string = ''
    for i in query:
        string += i + '+'
    string = string[:-1]
    return string

def get_xml(query):
    link = 'http://api.wolframalpha.com/v2/query?input={0}&appid={1}'.format(query, api_key)
    r = requests.get(link)
    return r
    
def parse_query(req):    
    soup = BeautifulSoup(req.text, "xml")
    s = None
    for l in soup.find_all('pod', {'id':'NutritionLabelSingle:ExpandedFoodData'}):
        s = l.find('plaintext')
    return s.text

def process_result(res):
    lis = res.split('\n')
    return lis

f00d.set_api_key(meta_key)
classifier = f00d.ClassificationModel(id=41125)

PORT = 8000
handler = SocketServer.TCPServer(("", PORT), myHandler)
print "serving at port 8000"
handler.serve_forever()



