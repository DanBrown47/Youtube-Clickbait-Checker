import os
import urllib.parse
import urllib.request
import argparse
from googleapiclient.discovery import build
from pytube import YouTube



# Change  these location to OS specific
parser =  argparse.ArgumentParser()

THUMB_FILE = './assets/thumbnails/thumbnail.jpg'
THUMB_LOC = './assets/thumbnails/'
VID_LOC = './assets/video/'


class Fetch():

    

    
    def __init__(self, url, key,  **kwargs):
        self.url = url
        self.key = key
        self.thumbnail_url = Fetch.get_thumbnail(self)
        # print("Thumbnail URL  
        Fetch.clean_assets(self, THUMB_LOC)
        Fetch.clean_assets(self, VID_LOC)
        Fetch.save_to_loc(self) 
        x = Fetch.download_video(self)
        

        
    def save_to_loc(self):
        with urllib.request.urlopen(self.thumbnail_url) as url_data:
            image_data = url_data.read()
        
        with open(THUMB_FILE, 'wb') as image_file:
            image_file.write(image_data)





    def get_thumbnail(self, **kwargs):
        
        parsed_url = urllib.parse.urlparse(self.url)
        query_string = parsed_url.query
        query_dict = urllib.parse.parse_qs(query_string)
        video_id = query_dict['v'][0]

        
        api_obj = build("youtube", "v3", developerKey=self.key)
        request = api_obj.videos().list(
                part="snippet",
                id=video_id
        )
        # Thumbnail is kept as a placeholder with High resolution
        response = request.execute()
        thumbnail_url = response["items"][0]["snippet"]["thumbnails"]["high"]["url"]
        return thumbnail_url

    def download_video(self):
        # Try to create object
        try:
            yts = YouTube(self.url)
            print(yts)
            yt = yts.streams.filter(progressive=True, file_extension='mp4').order_by('resolution') # Ability to change this resolution, Might need to get API
            yt = yt.desc().first()
            print("Got Hold of the stream")
        except:
            print("Connection Error") # Need to put a error handler here 

        try:
            # downloading the video 
            print("Downloading the video .....")
            yt.download(VID_LOC)
            print("Downloaded the video")
            return 1
        except:
            print("Some Error!")
            
        print('Task Completed!')

# Need to reimplement this
    def clean_assets(self, path):
        
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))



if __name__ == '__main__':
    print("Please run app.py as a flask server using the command python app.py")
