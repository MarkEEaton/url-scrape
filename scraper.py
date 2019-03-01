import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from collections import Counter


# set the path for the html files
path = "./html/"
urllist = []
filesscraped = 0

# iterate through the directory of html files
for filename in os.listdir(path):
    filesscraped += 1

    # read each file
    try:
        html = open(path + filename, "r").read()
    except UnicodeDecodeError:
        pass

    # make the soup
    soup = BeautifulSoup(html, "lxml")

    # pick out the hrefs and add them to a list
    for a in soup.find_all("a", href=True):
        urllist.append((urlparse(a["href"]))[1])

# rank the most popular hrefs, and pick the top 20
ranking = Counter(urllist).most_common()
shortranking = []
for k, v in ranking[:21]:
    if len(shortranking) <= 20:
        if k != "":
            shortranking.append({k: v})

# print the results
print(str(filesscraped) + " files scraped:")
print("--------------------------------")
for item in shortranking:
    for i in item:
        print(
            str(shortranking.index(item) + 1)
            + ". "
            + i
            + " ("
            + str(item[i])
            + " hits)"
        )
