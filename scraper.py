# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv # Import the csv module

# The URL of the website you want to scrape
url = "https://en.wikipedia.org/wiki/List_of_restaurant_chains_in_India"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("success!")
else:
    print("Error", response.text)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')
# print("soup", soup)

# Look for the specific HTML tags that contain the restaurant info
restaurants = soup.select("div.mw-content-ltr.mw-parser-output ul li")

# Open (or create) a CSV file with write permissions
with open('restaurants.csv', 'w', newline='') as file:
    writer = csv.writer(file) # Create a csv writer object
    writer.writerow(["Name"]) # Write the header row

# Loop through the list of restaurant tags
    for restaurant in restaurants:
        # Extract the restaurant's name
        name = restaurant.find('a').text 
        # Write a row with the name and rating
        writer.writerow([name]) 

