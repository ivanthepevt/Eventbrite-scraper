import csv
import requests
import bs4

text = input().split(";")
#print(text)
numofpages = int(input())
eventlinks = []
for searchq in text:
	#print(searchq)
	for i in range(numofpages):
		url = 'https://www.eventbrite.com/d/online/free--events/' + searchq + "/?page=" + str(i+1) + "&lang=en"
		#print(url)
		# Fetch the URL data using requests.get(url),
		# store it in a variable, request_result.
		request_result = requests.get(url)

		# Creating soup from the fetched request
		soup = bs4.BeautifulSoup(request_result.text, "html.parser")
		link_object = soup.find_all('a', href=True)

		# Iterate through the object
		# and print it as a string.
		for link in link_object:
			eventlinks.append(link['href'])
#print(eventlinks)
with open('EventsFound.csv', mode='w') as eventlist:
	eventlist_writer = csv.writer(eventlist, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
	eventlist_writer.writerow(['Date', 'Format', 'Location', 'Event', 'Link'])
	eventlinks = list(dict.fromkeys(eventlinks))
	for url in eventlinks:
		if "/e/" in url:
			#print(url)
			try:
				request_result = requests.get(url)
			except:
				continue
			# Creating soup from the fetched request
			soup = bs4.BeautifulSoup(request_result.text, "html.parser")
			content = soup.find('h1')
			try:
				title = (content.getText())
			except:
				title = "???"
			#print(title)

			loc = soup.find_all("div", {"class": "event-detail__content"})
			try:
				time = loc[0].getText()
				location = loc[1].getText()
			except:
				location = "???"
				time = "???"
				continue
			loc = soup.find_all("a", {"id": "organizer-link-org-panel"})
			try:
				organizer = loc[0].getText()
			except:
				organizer = "???"
			name = "[" + organizer + "] " + title
			print(name)
			eventlist_writer.writerow([time, 'Online', location, name , url])

