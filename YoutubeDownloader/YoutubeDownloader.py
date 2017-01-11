#You need to have os, urllib and BeautifulSoup installed on yur device
import os       #this library is used to download the video from the webpage
import urllib   #ths is used to open the url from the and access its content
import urllib2
from bs4 import BeautifulSoup
import webbrowser   #for opening the youtube video link
#you also need o install youtube-dl file which is used for downloading youtube videos
textToSearch = raw_input("Enter the video to be download : ")
query = urllib.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html,"lxml")
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    s2= 'https://www.youtube.com' + vid['href']
    print s2
    yn=raw_input("Do you want to open the link(y/n) : ")
    if(yn=="y"):
        webbrowser.open(s2)
    yn1=raw_input("Do you want to download(y/n) : ")
    if(yn1=="y"):
        os.system("youtube-dl -citk --buffer-size 100000 "+s2)
    else:
        print "Bye"
        break