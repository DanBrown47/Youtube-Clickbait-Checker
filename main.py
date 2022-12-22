import json
import requests
import os
import sys
import argparse
from dotenv import load_dotenv

load_dotenv()

try:
    YOUTUBE_API_KEY = os.environ.get('API_KEY')
except KeyError:
    print("Did you forget to set API_KEY in .env ? Create a file .env and get the key from GCP")


parser =  argparse.ArgumentParser()



def fetch_youtube(url, *args):
    print(url)
    pass

def main():
    parser.add_argument('-y', '--youtube', help="Add the full link of Youtube video", required=True)

    if not len(sys.argv) > 1:
        parser.print_help()
        exit()

    if parser.parse_args().youtube is not None:
        fetch_youtube(parser.parse_args().youtube)



if __name__ == '__main__':
    main()
