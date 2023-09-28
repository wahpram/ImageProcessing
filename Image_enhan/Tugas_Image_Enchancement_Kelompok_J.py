# Kelas : Pengolahan Citra Digital - C

# Nama Anggota Kelompok :
# 1. I Komang Cleon Kalea                   (2105551090)
# 2. Made Wahyu Adwitya Pramana             (2105551092)
# 3. Made Marshall Vira Deva                (2105551093)
# 4. I Gusti Ngurah Picessa Kresna Mandala  (2105551097)

from tkinter import *
import tkinter as tk
import PIL.Image
from PIL import ImageTk
import tkinter.filedialog
from array import *
from tkinter import simpledialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.scrolledtext as st

root = Tk()
root.title("IMAGE ENHANCEMENT APPLICATION (Grayscale, Brightness Adjustment, Negation)")
root.geometry("1310x800")

def histo1(pics):
    histogram = pics.histogram()

    l1 = histogram[0:255]

    fig = Figure(figsize=(4,4))
    a = fig.add_subplot(111)

    a.plot(l1)

    a.set_title ("HISTOGRAM CITRA GRAYSCALE", fontsize=8)
    a.set_ylabel("hg", fontsize=8)
    a.set_xlabel("g", fontsize=8)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x = 20, y = 300)
    canvas.draw()

def histo(pics):
    histogram = pics.histogram()

    l1 = histogram[0:256]

    fig = Figure(figsize=(4,4))
    a = fig.add_subplot(111)

    a.plot(l1)

    a.set_title ("HISTOGRAM CITRA HASIL", fontsize=8)
    a.set_ylabel("hg", fontsize=8)
    a.set_xlabel("g", fontsize=8)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x = 750, y = 300)
    canvas.draw()

def pixel(pics):
    global arr, arr_text, arr_gray
    
    x = 0
    y = 0
    arr = []
    arr_text = []
    arr_gray = []
    
    for i in range(w):
        for j in range(h):
            rvalue = pics.getpixel((x,y))[0]
            gvalue = pics.getpixel((x,y))[1]
            bvalue = pics.getpixel((x,y))[2]
            arr.append([x, y, rvalue, gvalue, bvalue])
            arr_text.append([rvalue])
            arr_gray.append([x, y, rvalue])
            j += 1
            y += 1
        x += 1
        i += 1
        y = 0
        j = 0 
    
    print(arr)

def text():
    label1 = Label(root, text = "CITRA ASLI")
    label1.grid(row= 0, column= 1)
    label2 = Label(root, text = "CITRA GRAYSCALE")
    label2.grid(row = 0, column= 2)
    label3 = Label(root, text = "CITRA HASIL")
    label3.grid(row = 0, column=3)

def frame():
    frame1 = Frame(root, width=206, height=206, background="#242424")
    frame1.grid(row= 1, column= 1, padx= 20, pady= 2)
    frame2 = Frame(root, width=206, height=206, background="#242424")
    frame2.grid(row= 1, column= 2, padx= 20, pady= 2)
    frame3 = Frame(root, width=206, height=206, background="#242424")
    frame3.grid(row= 1, column= 3, padx= 20, pady= 2)

def open_file():
    global w, h, pics
    
    file_path = tkinter.filedialog.askopenfilename()
    pics = (PIL.Image.open(file_path))
    pics = pics.convert('RGB')
    
    sizing = pics.resize((204,204))
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo
    my_label.grid(row= 1, column= 1, pady= 2)
    
    w, h = pics.size

def grayscale ():
    global pics2 
    
    size = w, h
    
    pixel(pics)
    
    pics2 = PIL.Image.new('RGB', size)
    load = pics2.load()

    for cr in arr:
        x, y, rvalue, gvalue, bvalue = cr   
        gray = (rvalue + gvalue +bvalue)//3
        load[x,y] = (gray, gray, gray)
    
    sizing = pics2.resize((204,204))
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo        
    my_label.grid(row= 1, column= 2, pady= 2)
    
    text_area.delete(1.0, END)
    pixel(pics2)
    text_area.insert(tk.INSERT, arr_text)
    
    histo1(pics2)

def bradj():
    size = w, h
    
    pixel(pics2)
    
    userinput = simpledialog.askinteger(title="Input", prompt="Nilai Peningkatan")
    
    pics3 = PIL.Image.new('RGB', size)
    load = pics3.load()
    
    for cr in arr_gray:
        x, y, gray = cr  
        adj = gray + userinput
        load[x,y] = (adj, adj, adj)
    
    sizing = pics3.resize((204,204))
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo
    my_label.grid(row= 1, column= 3)
    
    text_area2.delete(1.0, END)
    pixel(pics3)
    text_area2.insert(tk.INSERT, arr_text)
    
    histo(pics3)

def negation():
    size = w, h
    
    pixel(pics2)
    
    pics4 = PIL.Image.new('RGB', size)
    load = pics4.load()

    for cr in arr_gray:
        x, y, gray = cr
        ntn = 255 - gray
        load[x,y] = (ntn, ntn, ntn)
    
    sizing = pics4.resize((204,204))
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo
    my_label.grid(row= 1, column= 3, pady= 2)
    
    text_area2.delete(1.0, END)
    pixel(pics4)
    text_area2.insert(tk.INSERT, arr_text)
    
    histo(pics4)

text()
frame()

text_area = st.ScrolledText(root, width = 40, height = 14, font = ("Times New Roman",10))
text_area.grid(row=1, column = 5, pady = 10, padx = 10)

text_area2 = st.ScrolledText(root, width = 40, height = 14, font = ("Times New Roman",10))
text_area2.grid(row=1, column = 6, pady = 10, padx = 10)

tombol1 = Button(root, text="Buka Gambar", command=open_file, height=1, width=20)
tombol1.grid(row=3, column=1, pady= 2)

tombol2 = Button(root, text="Grayscale", command=grayscale, height=1, width=20)
tombol2.grid(row=3, column=2, pady= 2)

tombol3 = Button(root, text="Brightness Adjustment", command=bradj, height=1, width=20)
tombol3.grid(row=3, column=3, pady= 2)

tombol4 = Button(root, text="Negation", command=negation, height=1, width=20)
tombol4.grid(row=4, column=3, pady= 2)

root.mainloop()