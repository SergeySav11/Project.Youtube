from pytube import YouTube


url = str(input())
my_video = YouTube(url)
resolutions = my_video.streams
vid = list(enumerate(resolutions))

b = 1
for i in vid:
    print(str(i)[46:58])
    b += 1
print()
strm = int(input())

resolutions[strm].download()
print('Загрузка завершена')
