from pytube import YouTube
import os

#Opens your /links.txt file.
linkFile = open("/Users/miguelcastro/Documents/YouTubeMP3Automation/links.txt", "r")
print("Welcome to the YouTube Video/Audio downloader.")

#This is where you type in your destination folder for the media you want to download.
print("Enter the destination address (leave blank to save in current directory)")
destination = str(input(" ")) or '.'

#Input the media you would like to download.
print("Please enter the type of media you will be downloading.")
print("Video or Audio?")
media = str(input(" "))
#Audio encoder
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

#Video encoder
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

#If NOT Video or Audio, error.
else:
    print("Incorrect response")

