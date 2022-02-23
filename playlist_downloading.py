from pytube import YouTube
from tkinter import *
from tkinter.ttk import Combobox


def quality(types):
    global combo
    # Добавить изменение название кнопки
    btn.configure(text="Скачать")
    combo = Combobox(window)
    combo['values'] = types
    combo.current(0)
    combo.grid(column=0, row=1)

    # combo.current() - получение идекса под которым стоит качество
    # Почему то программа начинает загрузку видео по нажатию самой первой кнопки,сразу берет 144p



def download():
    qual = combo.current()
    qual = int(qual)
    # Cкачивание видео
    resolutions[qual].download()
    # Возвращение списка с качествами,

    # print(link)  # В переменной !link! хранится ссылка на видео
    # print(qual)  # В переменной !qual! хранится качество видео


def qualitization():
    global res
    global resolutions
    link_vid = txt.get()
    my_video = YouTube(link_vid)
    resolutions = my_video.streams.filter(progressive=True)
    # Создание списка с качествами
    res = list()
    for i in range(len(resolutions)):
        res.append(resolutions[i].resolution)
    # Возвращение списка с качествами,
    qualit = [res[0], res[1], res[2]]

    # Посмотри в функии quality и download


    quality(qualit)
    txt.destroy()
    lbl.configure(text="Укажите качество видео:")
    btn.configure(command=download)


window = Tk()
window.title("Youtube Downloader")
window.geometry('484x300')
lbl = Label(window, text="Вставьте ссылку на видео:", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)
txt = Entry(window, width=80)
txt.grid(column=0, row=1)
btn = Button(window, text="Выбрать качество", font=("Arial Bold", 10), command=qualitization)
btn.grid(column=0, row=2)
window.mainloop()
