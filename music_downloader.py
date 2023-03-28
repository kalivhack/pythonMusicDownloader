#!/bin/bash
import sys
import os
import getopt
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.request import urlretrieve
from urllib.parse import quote
from json import loads


# System Like Verables
downlaodFolder = os.getcwd() + "/"
us = UserAgent()
user_agent = us.chrome
headers = {
    "User-Agent": user_agent
}

errors = {
    "ArgError": """
    Script Usage:
    python main.py -n <SONG NAME> -a <ARTIST NAME>

    [ SYS ] Not Correct Argument Usage ABORTING!
    """,

    "Usage": 'Usage: python main.py -n <SONG NAME>',

    "NoArg": 'Error no argument gived'
}

# Verables
baseurl = "https://now.morsmusic.org"
url = baseurl + '/search/{}'
tit = ''
findWithName = False

# Functions


def printOutput(artist, name, url, N):
    data = f"""
        "ID": {N}
        "title": {name},
        "artist": {artist},
        "url": {url}
    """

    print(data)


def get_arg(args=sys.argv):
    global url, findWithName, tit

    try:
        opts, args = getopt.getopt(args[1:], "hn:a:", ['help'])

        if not opts:
            print(errors['NoArg'])
            exit()

        for n, a in opts:
            if n in ('-h', '--help'):
                print(errors['Usage'])
                exit()

            elif n in ('-n'):
                url = url.format(quote(a))

            elif n in ('-a'):
                print('finding with artist name: {}'.format(a))
                tit = a.lower()
                findWithName = True
                # print(findWithName, tit )

    except getopt.GetoptError as err:
        print(errors['ArgError'])
        exit()


def get_songs(page):
    content = BeautifulSoup(page, "html.parser")

    try:
        global N
        N = 0

        songs = content.find_all(
            'div', attrs={'class': 'track mustoggler __adv_list_track'})

        for song in songs:
            song = loads(song.attrs['data-musmeta'])

            N += 1

            url = baseurl + song['url']
            title = song['title']
            artist = song['artist']

            if not findWithName:
                printOutput(artist, title, url, N)

            elif findWithName and (artist.lower().find(tit.lower())) >= 0:
                printOutput(artist, title, url, N)

        if not findWithName:
            chose = int(input('Please enter the id of song to donwload: '))
            downlaod(url, title)

    except Exception as ex:
        print(ex)


def downlaod(url, title):
    loc = downlaodFolder + title + ".mp3"
    urlretrieve(url, title + ".mp3")

    print("File saved in {}".format(loc))


def main():
    r = requests.get(url, headers=headers)
    get_songs(r.content)


# Done...
if __name__ == "__main__":
    get_arg()
    main()
