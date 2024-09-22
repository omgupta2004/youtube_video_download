from pytube import YouTube
lin=input("enter the url of the youtube video")
link=lin
youtube_1= YouTube(link)

print(youtube_1.title)
print(youtube_1.thumbnail_url)
#video= youtube_1.streams.filter(only_audio=True)
#gives only audio of the video
video= youtube_1.streams.all()
vid= list(enumerate(video))
for i in vid:
    print(i)
strm=int(input("enter : "))
video[strm].download()
print("successfullly!!")





