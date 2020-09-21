from pytube import YouTube
import argparse

parser = argparse.ArgumentParser(description="Terminal Based video/audio downloader.")
parser.add_argument("-u","--url", dest="url", type=str, required=True, help="Youtube video URL.")
parser.add_argument("-t","--type", dest="type", type=str, required=True, help="Download type: video/audio")
parser.add_argument("-r", "--res", dest="res", type=str, required=False, help="This parameter is for videos only. 144p,240p,360p,480p,720p,1080p.")
args = parser.parse_args()

url = args.url
rtype = args.type
reso = args.res

try:
    video = YouTube(url)
    if rtype == "audio":
        print("Downloading...")
        stream = video.streams.filter(type=rtype).first().download()
        print(f"Your audio is here: {stream}")
    elif rtype == "video":
        print("Downloading...")
        stream = video.streams.filter(type=rtype,res=reso).first().download()
        print(f"Your video is here: {stream}")
    else:
        print("Type must be video or audio!")

except AttributeError:
    print("Check your video resolution.")
except:
    print("Check your URL.")
