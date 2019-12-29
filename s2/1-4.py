import pytube
import os
import subprocess


youtubeurl = input("url:")
yt = pytube.YouTube(youtubeurl)
videos = yt.streams.all()

for i in range(len(videos)):
    print(i, videos[i])

cnum = int(input("select the video quility(0~16)"))

down_dir = "C:\\Users\\moon2\\Desktop\\file\\py\\s2"

videos[cnum].download(down_dir)

newfilename = input("new file name?")
orifilename = videos[cnum].default_filename

subprocess.call(['ffmpeg','-i',
os.path.join(down_dir, orifilename),
os.path.join(down_dir, newfilename)
])
