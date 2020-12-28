from pytube import YouTube
import argparse

#Defines the arguments
parser = argparse.ArgumentParser(description="Terminal Based video/audio downloader.")
parser.add_argument("-u","--url", dest="url", type=str, required=True, help="Youtube video URL.")
parser.add_argument("-t","--type", dest="type", type=str, required=True, help="Download type: video/audio")
parser.add_argument("-r", "--res", dest="res", type=str, required=False, help="This parameter is for videos only. 144p,240p,360p,480p,720p,1080p.")
parser.add_argument("-na","--no-audio", dest="noaud", action='store_true', required=False, help="If you want download video without audio")
args = parser.parse_args()

#Assigns arguments received from the user to variables
url = args.url
rtype = args.type
reso = args.res
noaud = args.noaud

#Download audio
def DAudio(video):
    print("Downloading..") #TODO: change this with a dinamic download bar
    stream = video.streams.filter(type=rtype).first().download()
    print(f"Your audio is here: {stream}")

#Download video
def DVideo(video,reso,prog):
    print("Downloading..") #TODO: change this too
    if prog: #if video downloading with auido
        stream = video.streams.filter(type=rtype,res=reso,progressive=True).first().download()
    else: #if video downloading without audio
        stream = video.streams.filter(type=rtype,res=reso).last().download() #I dont use "progressive=False" bec its not working...
    print(f"Your video is here: {stream}")

#TODO: automatically download and merge video and audio
#controls the audio of the video
def AudioCheck(video,reso):
    if noaud: # if -na parameter used
        prog = False #TODO: you dont need "prog" variable. check this
        DVideo(video,reso,prog)
    elif video.streams.filter(type=rtype,res=reso,progressive=True): #elif video have audio in spesific reso value
        prog = True
        DVideo(video,reso,prog)
    elif video.streams.filter(type=rtype,progressive=True): #elif video have audio in any reso value
        ares = [stream.resolution for stream in video.streams.filter(type=rtype,progressive=True)] #resolutions with audio
        print(f"Sorry but this video haven't audio in {reso} resolution. The resolutions with audio:")
        for i in ares:
            print(i)
        print("Detailed information about this: https://python-pytube.readthedocs.io/en/latest/user/quickstart.html#dash-vs-progressive-streams")
        print("If you want download this video without audio use the '-na' parameter.")
    else: # if video haven't audio in any reso
        print("Sorry but this video haven't audio in all resolutions.")
        print("Detailed information about this: https://python-pytube.readthedocs.io/en/latest/user/quickstart.html#dash-vs-progressive-streams")
        print("If you want download this video without audio use the '-na' parameter.")
        

try:
    video = YouTube(url)
    if rtype == "audio":
        DAudio(video)
    elif rtype == "video":
        AudioCheck(video,reso)
    else:
        print("Type must be video or audio!")

except AttributeError:
    print("Check your video resolution.")
except:
    print("Check your URL.")
