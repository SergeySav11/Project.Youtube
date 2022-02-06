
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

res = ['"144p', '360p"', '720p"', '"1080', '="108', '"1080', '"720p', '="720', '"720p', '"480p', 's="48', '="480', '="360', 's="36', '="360', '="240', 's="24', '="240', '="144', 's="14', '="144', '="48k', '="128', 'r="50', 'r="70', 'r="16']


def qualitization():
    global link
    global qualit
    link = txt.get()

    pass

    qualit = [res[0][1:],res[1][:4],res[2][:4]] #Сюда укажите качества видео массивом

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
print(qualit)