from pytube import YouTube
from tkinter import *
from tkinter.ttk import Combobox




def quality(types,res):
    global combo
    lbl.configure(text="Укажите качество видео:")
    # Добавить изменение название кнопки
    combo = Combobox(window)
    combo['values'] = types
    combo.current(0)
    combo.grid(column=0, row=1)
    btn.destroy()
    btn_2 = Button(window, text="Скачать", font=("Arial Bold", 10), command=download(combo.get()))
    btn_2.grid(column=0, row=2)
    # btn.configure(command=download(combo.get(),resolutions))


def download(qual):
    print(qual)
    # Cкачивание видео
    resolution = resolutions.get_by_resolution(qual)
    print(resolution)
    # Возвращение списка с качествами,


    # print(link)  # В переменной !link! хранится ссылка на видео
    # print(qual)  # В переменной !qual! хранится качество видео



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

    # Возвращение списка с качествами,
    # Написать код который будет получать оригинальные качества
    qualit = [res[0], res[1], res[2]]
    quality(qualit,res)

    txt.destroy()


window = Tk()
window.title("Youtube Downloader")
window.geometry('484x300')
lbl = Label(window, text="Вставьте ссылку на видео:", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)
txt = Entry(window,width=80)
txt.grid(column=0, row=1)
btn = Button(window, text="Выбрать качество", font=("Arial Bold", 10), command=qualitization)
btn.grid(column=0, row=2)
window.mainloop()
