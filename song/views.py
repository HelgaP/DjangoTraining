from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.

def getSong(request, songName):

    address = f"https://www.amalgama-lab.com/songs/j/john_lennon/{songName}.html"
    req = requests.get(address)
    if req.status_code == 200:
        print("everything's ok")
    soup = BeautifulSoup(req.text, 'html.parser')
    a = soup.select(".string_container > .original")
    songText = []

    for count, value in enumerate(a):
        valueSoup = BeautifulSoup(str(value), 'html.parser')
        songLine = valueSoup.div.string
        if not songLine:
            break
        songText.append(songLine)

    print("song text is ", songText)

    return render(request, "song/templates/songText.html", {
        "text": songText,
        "songName": songName.capitalize()
    })
