# Eventbrite-scraper
Scrape online events on Eventbrite platform using keyword.

Step-by-step guide can be found at the attached pdf.

Setup (do 1 time only)

Install side packages:

pip install csv

pip install requests

pip install bs4

Each time running the bot, try searching your keywords on eventbrite to make sure there is no typo and it can be searched. Wrong keywords with no results can cause an error.

Input should be in the format:

	entrepreneur;business
	2

Line 1: keywords to search, separated by “;”. Try searching the keyword on eventbrite.
  
Line 2: number of pages to look up, the more this value is, the more results are found but longer time it takes and less accurate results.
  
The output is in the csv file generated.
