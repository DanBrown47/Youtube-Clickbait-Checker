import json
import requests
import os
import sys
import argparse
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = 
parser =  argparse.ArgumentParser()



def fetch_youtube(url, *args):
    pass

def main():
    parser.add_argument('-y', '--youtube', help="Add the full link of Youtube video", required=True)

    if not len(sys.argv) > 1:
        parser.print_help()
        exit()

    if parser.parse_args().youtube is not None:
        fetch_youtube(parser)






if __name__ == '__main__':
    main()
