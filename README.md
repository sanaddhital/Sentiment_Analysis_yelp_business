# Sentiment_Analysis_yelp_business
This repository will record my work on my first Sentiment analysis project. I have created a model for sentimental analysis of reviews in yelp.com
All the scripts are in the notebook file Sentiment_Analysis_yelp.

--> First I created a scraper to scrape reviews from the link of a business/service page in yelp.com. You just need to put the link of a business in the 
"website" variable in the first code shell.

--> Then request and BeautifulSoup will parse through the page to find the reviews.

--> The next step is Data analytics. I used metrices such as word count, character count, average word length, number of stop words and percentage of stop words
For the stop words, I used nltk (Natural language Toolkit) 

-->Next step is Data Cleaning. I lowercased words, removed punctuations, removed stop words and (also has feature to remove manual stop words)

--> I lemmatized the words using textblob library

--> Final is the Sentimental Analysis. I used TextBlob to calculate Polarity and Subjectivity of reviews for understanding the sentiments of reviews.
