# Sentiment_Analysis_yelp_business
This repository will record my work on my first Sentiment analysis project. I have created a model for sentimental analysis of reviews for business in yelp.com
All the scripts are in the notebook file Sentiment_Analysis_yelp and a python file for scraper.

--> First I created a scraper to scrape reviews from the link of a business/service page in yelp.com which is a function in the python file.The scraper uses request and BeautifulSoup to parse through yelp website to find the reviews. When we enter the link of a business in the  "website" variable in the first code shell of notebook, the function scrapes the reviews and sends it over to the notebook.

--> Then the scraped reviews go into pandas dataframe for Data analytics. I used metrices such as word count, character count, average word length, number of stop words and percentage of stop words
For the stop words, I used nltk (Natural language Toolkit) 

--> Next step is Data Cleaning. I lowercased words, removed punctuations, removed stop words and (also has feature to remove manual stop words)

--> After that comes lemmatization using textblob library

--> Final is the Sentimental Analysis. I used TextBlob to calculate Polarity and Subjectivity of reviews for understanding the sentiments of reviews.
