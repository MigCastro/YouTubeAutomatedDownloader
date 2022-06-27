from pytube import YouTube
import os

linkFile = open("/Users/miguelcastro/Documents/YouTubeMP3Automation-main/links.txt", "r")
print("Welcome to the YouTube Video/Audio downloader.")
print("Enter the destination address (leave blank to save in current directory)")
destination = str(input(" ")) or '.'
print("Please enter the type of media you will be downloading.")
print("Video or Audio?")
media = str(input(" "))
if media == str("Audio") or media == str("audio"):
    print("Downloading Audio.")
    for line in linkFile:
        for line in line.split():
            yt = YouTube(str(line.split()))
            video = yt.streams.get_highest_resolution()
            out_file = video.download(destination)
            if os.path.exists(destination): 
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.replace(out_file, new_file)
            print("Downloaded " + yt.title)        
            linkFile.close
    print("All Files have been successfully downloaded.")
elif media == str("Video") or media == str("video"):
    print("Downloading Video.")
    for line in linkFile:
        for line in line.split():
            yt = YouTube(str(line.split()))
            video = yt.streams.get_highest_resolution()
            out_file = video.download(destination)
            if os.path.exists(destination):
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp4'
                os.replace(out_file, new_file)
            print("Downloaded " + yt.title)
            linkFile.close
    print("All files have been successfully downloaded.")
else:
    print("Incorrect response")            

