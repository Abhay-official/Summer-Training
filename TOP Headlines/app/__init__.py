from bs4 import BeautifulSoup
import urllib.request
headers = {}
headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

class Topheadlines:
	def __init__(self, url, order=1):
		self.url = url
		self.order = order
		req = urllib.request.Request(self.url,headers=headers)
		resp = urllib.request.urlopen(req)
		scrap_data = BeautifulSoup(resp.read(), "html.parser")
		self.scrap_data = scrap_data

	def html(self):
		return self.scrap_data.prettify()

	def headlines(self):
		d_l = []
		self.head_list = [(i.text,i.get('href')) for i in self.scrap_data.find_all("a")]
		__n = self.__AvgHeadLen()
		for i in self.head_list:
			if len(i[0].strip())>__n:
                                d_l.append((i[0].strip(),i[1]))
		return d_l

	def __AvgHeadLen(self):
		total_letter = 0
		for i in self.head_list:
			total_letter = total_letter+len(i[0].strip())
		return int(total_letter//len(self.head_list)*self.order)

from flask import Flask, redirect, url_for, request, render_template
import requests
import re

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/search', methods =['POST'])
def search():
	search = request.form['search']
	msg=""
	if search == "":
		return render_template('index.html')
	else:
		match = re.search(r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)',search)
		if match:			
			N = Topheadlines(search)
			headline = []
			links = []
			for i in N.headlines():
				headline.append(i[0])
				links.append(i[1])
	
			new_match = re.search(r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)',links[1])
			if new_match:
				new=""
			else:
				if search[-1]== "/":
    					new=search[0:-1]
				else:
					new=search

			return render_template('search.html',headline=headline,links=links,search=search,new=new)
		else:
			msg = "Enter valid Url"
			return render_template("index.html",msg=msg)

@app.route('/feedback')
def feedback():
        return render_template('feedback.html')

@app.route('/about')
def about():
        return render_template('about.html')

if __name__ == '__main__':
   app.run(debug = True)
