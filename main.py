import json
import requests
import os
import sys
import argparse
import re
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

try:
    YOUTUBE_API_KEY = os.environ.get('API_KEY')
except KeyError:
    print("Did you forget to set API_KEY in .env ? Create a file .env and get the key from GCP")


parser =  argparse.ArgumentParser()


def is_youtube_url(url):
    return True
    # Compile the regular expression
    pattern = re.compile(r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)')

    # Check if the string matches the pattern
    return pattern.match(url) is not None


def get_thumbnail(url, **kwargs):
    api_obj = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = api_obj.videos().list(
            part="snippet",
            id=url
    )

    response = request.execute()
    thumbnail_url = response["items"][0]["snippet"]["thumbnails"]["high"]["url"]
    print(thumbnail_url)
    return thumbnail_url

    # return res_url


def fetch_youtube(url, **kwargs):
    # Testing if the url given is a youtube link
    if is_youtube_url(url):
        thumbnail_url = get_thumbnail(url)
    else:
        print("Not a youtube url")


def main():
    parser.add_argument('-y', '--youtube', help="Add the full link of Youtube video", required=True)

    if not len(sys.argv) > 1:
        parser.print_help()
        exit()

    if parser.parse_args().youtube is not None:
        fetch_youtube(parser.parse_args().youtube)



if __name__ == '__main__':
    main()
