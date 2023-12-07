import requests
from bs4 import BeautifulSoup


'''This function will take the website link from the main notebook, scrape the business site and give the reviews back'''
def scrape_business_website(link):
    r = requests.get(link)
    ##But it doesn't give text to read the data. So, converting the requested data to text and parsing through the html page
    soup = BeautifulSoup(r.text, 'html.parser')
    #lets find the class of the section with reviews in html elements
    divs = soup.find_all(class_= "comment__09f24__D0cxf css-qgunke")
    #creating an array of reviews
    reviews = []
    for div in divs:
        reviews.append(div.text)
    return reviews