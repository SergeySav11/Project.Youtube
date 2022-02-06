
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


def qualitization():
    global link
    link = txt.get()

    pass

    qualit = [480,560,1080,2500,1000,800] #Сюда укажите качества видео массивом

    quality(qualit)
    txt.destroy()
    lbl.configure(text = "Укажите качество видео:")
    btn.configure(command=download)




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