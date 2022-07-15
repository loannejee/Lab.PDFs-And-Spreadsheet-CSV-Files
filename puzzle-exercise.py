# Task One: Grab the Google Drive Link from .csv File
import csv

data = open('find_the_link.csv', encoding="utf-8")

csv_data = csv.reader(data)

data_lines = list(csv_data) # list of rows with data

google_link = ''

colNum = 0

for line in data_lines:
    google_link += line[colNum] 
    colNum += 1

print(google_link) # https://drive.google.com/open?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q


# Task Two: Download the PDF from the Google Drive link and find the phone number that is in the document.