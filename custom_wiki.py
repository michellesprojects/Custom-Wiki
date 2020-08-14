import requests
import webbrowser

#function for excluding articles based on certain keywords
blocked_words = ['village','river','language','school','city','genus','singer','town','state','county','district','politic','player','ball','champion','island','community','species','plant','protein','song','album','film','director','actor','actress','building','sport','province','is located','neighborhood']

def exclude_articles():

	for i in range(0,5):

		valid = False
		while(not valid):

			#get info of a random wikipedia article
			response = requests.get('https://en.wikipedia.org/api/rest_v1/page/random/summary')
			json = response.json()

			summary = json['extract']

			if not any(c in summary for c in blocked_words):
				valid = True

				#get the URL to open in browser
				title = json['title']

				#remove non-ascii characters 
				title = "".join(i for i in title if ord(i)<128)

				url = 'https://en.wikipedia.org/wiki/' + title.replace(" ","_")

				#open the URL

				webbrowser.open_new_tab(url)


#exclude_articles()

#function for searching for articles with certain keywords
wanted_words = ['belief','philosophy','science',' art ','literature','history','artitecture','theory','invent','linguistics','theology',' myth','folklore']

def include_articles():

	for i in range(0,5):

		valid = False
		while(not valid):

			#get info of a random wikipedia article
			response = requests.get('https://en.wikipedia.org/api/rest_v1/page/random/summary')
			json = response.json()

			summary = json['extract']

			if any(c in summary for c in wanted_words):
				valid = True

				#get the URL to open in browser
				title = json['title']

				#remove non-ascii characters 
				title = "".join(i for i in title if ord(i)<128)

				url = 'https://en.wikipedia.org/wiki/' + title.replace(" ","_")

				#open the URL

				webbrowser.open_new_tab(url)



#include_articles()

def scan_full_article():

	for i in range(0,5):

		valid = False
		while(not valid):

			#get info of a random wikipedia article
			response = requests.get('https://en.wikipedia.org/api/rest_v1/page/random/html')
			html = response.text

			

			if any(c in html for c in wanted_words):
				valid = True

				#get the URL to open in browser
				title = response.url
				title = title.replace("https://en.wikipedia.org/api/rest_v1/page/html/","")

				url = 'https://en.wikipedia.org/wiki/' + title

				webbrowser.open_new_tab(url)


scan_full_article()




