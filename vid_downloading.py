from pytube import YouTube
from tqdm import tqdm,tqdm_gui,trange
from time import sleep

def download(url):
    my_video = YouTube(url)
    resolutions = my_video.streams
    vid = list(enumerate(resolutions))
    #print(my_video.title)
    #print(my_video.thumbnail_url)

    #Создание списка с качествами
    res = []
    for i in vid:
         print(i)
    print()
    #Переменная хранящая выбраное качество
    strm = int(input())
    #Cкачивание видео
    resolutions[strm].download()
    #Возвращение списка с качествами,
    # return int(res)



download('https://www.youtube.com/watch?v=LmEcyQnfpDA')