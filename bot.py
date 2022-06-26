from pytube import YouTube
import os

linkFile = open("/Users/miguelcastro/Documents/YouTubeMP3Automation-main/links.txt", "r")

print("Enter the destination address (leave blank to save in current directory)")
destination = str(input(" ")) or '.'
for line in linkFile:
    for line in line.split():
        yt = YouTube(str(line.split()))
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=destination)
        if os.path.exists(destination): 
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.replace(out_file, new_file)
        print("Downloaded " + yt.title)        
        linkFile.close
print("All Files have been successfully downloaded.")

