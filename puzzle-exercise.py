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
# You should get this phone number
# 505 503 4455
import PyPDF2
import re

f = open('Find_the_Phone_Number.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
p = 0
pattern = r'[\d{3}]'
phone_number = ''

# Check every page for all the numbers
for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p)
    pdf_text = page.extractText()

    if re.search(pattern, pdf_text):
        phone_number = re.findall(pattern, pdf_text)
        print("Page {} - Found some numbers: ".format(p), phone_number)
    else:
        print("Page {} - No numbers here.".format(p))
