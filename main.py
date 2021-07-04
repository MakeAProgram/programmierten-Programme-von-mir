from tkinter import*
import pickle
h = Tk()
h.title("Echtzeit-Notizbuch")
h.geometry("400x200")
a = Entry(h)
a.pack()

def saving():
    with open("pickle-test.dat", "wb") as f:
        pickle.dump(a.get(), f)

def looad():    
    with open("pickle-test.dat", "rb") as f:
        l = Label(text=pickle.load(f), height=1000, width=1000, bg="white")
        l.pack()

def info():
    t = Tk()
    t.title("Info")
    o = Label(t, text="""Autor: MakeAProgram
                         Veröffentlicht am 04.07.2021
                        Sinn: Zum Zwischenspeichern von Gedanken kreiert""")
    o.pack()
j = Button(text="In Datei speichern", command=saving)
j.pack()
b = Button(text="Aus Datei laden", command=looad)
b.pack()

i = Button(text="Info von Echtzeit-Notizbuch", command=info)
i.pack()
