from pytube import YouTube
from tqdm import tqdm,tqdm_gui,trange
from time import sleep

def download(url):
    try:
        my_video = YouTube(url)
        resolutions = my_video.streams
        vid = list(enumerate(resolutions))
        print(type(vid))
        #print(my_video.title)
        #print(my_video.thumbnail_url)
        #Создание списка с качествами
        res = list()
        for i in vid:
            res.append(str(i)[50:55])
        print(res)
        #Переменная хранящая выбраное качество
        strm = int(input())
        #Cкачивание видео
        o = res
        resolutions[strm].download()
        #Возвращение списка с качествами,
        return o
    except:
        error = ('Ошибка,проверьте ссылку')
        return error





def qualitization():
    global res
    global resolutions
    link_vid = txt.get()
    my_video = YouTube(link_vid)
    resolutions = my_video.streams.filter(progressive=True)
    res = list()
    for i in range(len(resolutions)):
        res.append(resolutions[i].resolution)
    print(resolutions)