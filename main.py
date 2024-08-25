from urllib.request import urlopen
import re

def printItemsReadable(group):
    for item in group:
        print(item)

def printToFile(file, string):
    with open (file, 'w', encoding='utf-8') as f:
        print(string, file=f, end="")

def scrapePage(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html

url = "https://aladin.fei.stuba.sk/rozvrh/"

stranka = scrapePage(url)

print(stranka, end='')
file = "output.txt"
printToFile(file, stranka)

#----------regex hladajuci linky na landing stranke--------------
#<a najde vsetky <a
#\b spravi ze najde len <a a nie <abbr>
#[^>]* hoci co okrem >
#> najde >
regex = "<a\\b[^>]*>"
regex_finds = re.findall(regex, stranka, re.MULTILINE)

# printItemsReadable(regex_finds)
# print(regex_finds)
#-----------------------------------------------------------------

strankaRozvrh = scrapePage("https://aladin.fei.stuba.sk/rozvrh/2bc_API_1.html")
printToFile("outputRozvrh.html", strankaRozvrh)


