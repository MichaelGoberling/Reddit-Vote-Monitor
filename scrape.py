# import libraries
import urllib2
import csv
from datetime import datetime
from bs4 import BeautifulSoup
import time

count = 0
score_num = 0
score_last_hour = 0
exitmsg = "This should have been changed!"

quote_page = "nothing"
filename = "score"
looking_for = "https://www.reddit.com/r"

while quote_page.find(looking_for) == -1:
    quote_page = raw_input("Enter post URL: ")
    type(quote_page)


print("Monitoring!")
req = urllib2.Request(quote_page, headers={ 'User-Agent': 'Mozilla/5.0' })
page = urllib2.urlopen(req).read()
soup = BeautifulSoup(page, 'html.parser')


title_box = soup.find('a', attrs={'title'})
title = title_box.text.strip()
title = title.replace("/", "")
title = title.replace("?", "")

#print title
#print score

# open and store in a csv fileC:\Users\micha\PycharmProjects\untitled\score.csv
while count < 360 or (score_num - 200 > score_last_hour):
    with open("./spreadsheets/" + title + ".csv", 'a') as csv_write:
        writer = csv.writer(csv_write)
        req = urllib2.Request(quote_page, headers={'User-Agent': 'Mozilla/5.0'})
        page = urllib2.urlopen(req).read()
        soup = BeautifulSoup(page, 'html.parser')
        score_count = soup.find('span', attrs={'class': 'number'})
        score = score_count.text
        score_num = int(score.replace(",", ""))

        print "Minute: ", count
        print "Score: ", score
        writer.writerow([title, datetime.now(), score])
        count = count + 1
        exitmsg = "Exited after six hours."

        if count > 300:
            with open(title + ".csv", 'rb') as csv_read:
                reader = csv.reader(csv_read)
                reader = list(reader)
                score_last_hour = reader[(2*(count - 60) - 1)][2]
                score_last_hour = score_last_hour.replace(",", "")
                int(score_last_hour)
                exitmsg = "Exited after " + str(count/60) + " hours."

    time.sleep(60)

print("Done!")
print exitmsg




