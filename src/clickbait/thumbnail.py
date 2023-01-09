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
THUMB_FILE = './assets/thumbnails/thumbnail.jpg'
THUMB_LOC = './assets/thumbnails/'
VID_LOC = './assets/video/'

def save_to_loc(url):
    with urllib.request.urlopen(url) as url_data:
        image_data = url_data.read()
    
    with open(THUMB_FILE, 'wb') as image_file:
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
        yt = yt.streams.get_highest_resolution()
    except:
        print("Connection Error")

    try:
        # downloading the video 
        yt.download(VID_LOC)
    except:
        print("Some Error!")
        
    print('Task Completed!')


def clean_assets(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def fetch_youtube(url, **kwargs):
    # Testing if the url given is a youtube link
    if is_youtube_url(url):
        thumbnail_url = get_thumbnail(url)
        print(thumbnail_url)
        clean_assets(VID_LOC)
        clean_assets(THUMB_LOC)
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
