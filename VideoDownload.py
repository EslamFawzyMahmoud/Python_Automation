from pafy import new
import youtube_dl

url=input("Enter your link here: ")
video = new(url)
SavePath=input("Put the path: ")
allstream=video.allstreams
audio=video.audiostreams

print("Video Information :")
print(video)

counter=0
for i in allstream:
    print(counter,"-",i)
    counter += 1

chose=int(input("Enter your choice: "))
if (chose < counter):
    print("Downloading....")
    allstream[chose].download(SavePath)
    print("Download Successfully")
else:
    print("This choice off limited.")

