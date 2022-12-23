import json
import requests
import os
import sys
import urllib.parse
import urllib.request
import argparse
import re
from dotenv import load_dotenv
from googleapiclient.discovery import build
from pytube import YouTube

load_dotenv()

try:
    YOUTUBE_API_KEY = os.environ.get('API_KEY')
except KeyError:
    print("Did you forget to set API_KEY in .env ? Create a file .env and get the key from GCP")


parser =  argparse.ArgumentParser()
THUMB_LOC = './assets/thumbnails/thumbnail.jpg'
VID_LOC = './assets/video/'

def save_to_loc(url):
    with urllib.request.urlopen(url) as url_data:
        image_data = url_data.read()
    
    with open(THUMB_LOC, 'wb') as image_file:
        image_file.write(image_data)



def is_youtube_url(url):
    # Compile the regular expression
    pattern = re.compile(r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)')

    # Check if the string matches the pattern
    return pattern.match(url) is not None


def get_thumbnail(url, **kwargs):
    parsed_url = urllib.parse.urlparse(url)
    query_string = parsed_url.query
    query_dict = urllib.parse.parse_qs(query_string)
    video_id = query_dict['v'][0]

    pass
    api_obj = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = api_obj.videos().list(
            part="snippet",
            id=video_id
    )
    # Thumbnail is kept as a placeholder with High resolution
    response = request.execute()
    thumbnail_url = response["items"][0]["snippet"]["thumbnails"]["high"]["url"]
    return thumbnail_url

def download_video(url):
    # Try to create object
    try:
        yt = YouTube(url)
    except:
        print("Connection Error")

    # filters out all the files with "mp4" extension 
    mp4files = yt.filter('mp4')

    #to set the name of the file
    yt.set_filename('Video.mp4')
    # get the video with the extension and
    # resolution passed in the get() function 
    d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
    
    try:
        # downloading the video 
        d_video.download(VID_LOC)
    except:
        print("Some Error!")
        git
    print('Task Completed!')

def fetch_youtube(url, **kwargs):
    # Testing if the url given is a youtube link
    if is_youtube_url(url):
        thumbnail_url = get_thumbnail(url)
        print(thumbnail_url)
        save_to_loc(thumbnail_url)
        download_video(url)
        
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
