from pytube import YouTube
try:
    url = str(input())
    my_video = YouTube(url)
    resolutions = my_video.streams
    vid = list(enumerate(resolutions))
    for i in vid:
        print(str(i)[:100])
    print()
    strm = int(input())
    resolutions[strm].download()
    print('Загрузка завершена')
except:
    print('Ошибка,проверьте целестность вышей ссылки')
