from pytube import YouTube
from tkinter import *
from tkinter.ttk import Combobox





def quality(types):
    global combo
    combo = Combobox(window)
    combo['values'] = (types)
    combo.current(0)
    combo.grid(column=0, row=1)


def download():
    qual = combo.get()

    pass


    print(link) #В переменной !link! хранится ссылка на видео
    print(qual) #В переменной !qual! хранится качество видео


# res = ['"144p', '360p"', '720p"', '"1080', '="108', '"1080', '"720p', '="720', '"720p', '"480p', 's="48', '="480', '="360', 's="36', '="360', '="240', 's="24', '="240', '="144', 's="14', '="144', '="48k', '="128', 'r="50', 'r="70', 'r="16']


def qualitization():
    global link
    global qualit
    link = txt.get()

    def downloading(link):
        my_video = YouTube(link)
        resolutions = my_video.streams
        vid = list(enumerate(resolutions))
        # print(my_video.title)
        # print(my_video.thumbnail_url)
        # Создание списка с качествами
        res = list()
        for i in vid:
            res.append(str(i)[50:55])
        # Переменная хранящая выбраное качество
        strm = int(input())
        # Cкачивание видео
        resolutions[strm].download()
        # Возвращение списка с качествами,
        return res

    res_1 = res

    qualit = [res_1[0][1:],res_1[1][:4],res_1[2][:4]] #Сюда укажите качества видео массивом

    quality(qualit)
    txt.destroy()
    lbl.configure(text = "Укажите качество видео:")
    btn.configure(command=download)



print(download())
window = Tk()
window.title("Youtube Downloader")
window.geometry('484x300')
lbl = Label(window, text="Вставьте ссылку на видео:", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)
txt = Entry(window,width=80)
txt.grid(column=0, row=1)
btn = Button(window, text="Скачать!", font=("Arial Bold", 10), command=qualitization)
btn.grid(column=0, row=2)
window.mainloop()
print(qualit)