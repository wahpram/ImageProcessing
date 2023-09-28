from tkinter import *
import PIL.Image
from PIL import ImageTk
import tkinter.filedialog
from array import *
from pathlib import Path

# Kelas : Pengolahan Citra Digital - C

# Nama Anggota Kelompok :
# 1. I Komang Cleon Kalea                   (2105551090)
# 2. Made Wahyu Adwitya Pramana             (2105551092)
# 3. Made Marshall Vira Deva                (2105551093)
# 4. I Gusti Ngurah Picessa Kresna Mandala  (2105551097)

# Membuat window dengan tkinter
root = Tk()
root.title("DIGITAL IMAGE PROCESSING (RGB/CMY)")
root.configure(background='#242424')
root.geometry("815x620")

# Fungsi blank untuk membuat gambar berwarna solid
def blank():
    blank_open = PIL.Image.new('RGB', (204,204), (255,255,255))
    blank_image = PIL.ImageTk.PhotoImage(blank_open)
    label_blank_open = Label(root, image = blank_image)
    label_blank_copy = Label(root, image = blank_image)
    label_blank_rgb = Label(root, image = blank_image)
    label_blank_open.place(x= 50, y=100)
    label_blank_copy.place(x= 300, y=100)
    label_blank_rgb.place(x= 550, y=100)

# Fungsi untuk menginput gambar dan membaca pixel dari gambar
def koordinat():
    global arr, w, h, rvalue, gvalue, bvalue,x, y, file_name
    
    x = 0
    y = 0
    arr = []
    
    file_path = tkinter.filedialog.askopenfilename()
    file_name = Path(file_path).stem
    pics = PIL.Image.open(file_path)
    pics = pics.convert('RGB')
    sizing = pics.resize((204,204))
    
    photo = PIL.ImageTk.PhotoImage(sizing)
    my_label = Label(image=photo)
    my_label.image = photo
    my_label.place(x= 50, y=100)
    
    w, h = pics.size
    
    for i in range(w):
        for j in range(h):
            
            rvalue = pics.getpixel((x,y))[0]
            gvalue = pics.getpixel((x,y))[1]
            bvalue = pics.getpixel((x,y))[2]
            arr.append([x, y, rvalue, gvalue, bvalue])
            j += 1
            y += 1
            # print("Koordinat x : {}, y : {}, r : {}, g : {}, b : {}".format(x,y,rvalue,gvalue,bvalue))
        x += 1
        i += 1
        y = 0
        j = 0
    

# Fungsi untuk menampilkan kembali hasil copy gambar
def hasil_copy():
    size = w, h
    print(arr)
    
    pics2 = PIL.Image.new('RGB', size)
    load = pics2.load()
    
    for cr in arr:
        x, y, rvalue, gvalue, bvalue = cr     
        load[x,y] = (rvalue, gvalue, bvalue)
    
    sizing2 = pics2.resize((204,204))
    photo2 = PIL.ImageTk.PhotoImage(sizing2)
    my_label2 = Label(image=photo2)
    my_label2.image = photo2
    my_label2.place(x=300, y=100)

# Fungsi untuk menampilkan gambar RGB dan CMYK
def sel(x):
    global pics3, name
    size = w, h
    
    pics3 = PIL.Image.new('RGB', size)
    load2 = pics3.load()
    
    match x:
        case 1:
            for cr in arr:
                x, y, rvalue, gvalue, bvalue = cr
                load2[x,y] = (rvalue, 0, 0)    
                name = 'Red'     
        case 2:
            for cr in arr:
                x, y, rvalue, gvalue, bvalue = cr
                load2[x,y] = (0, gvalue, 0)  
                name = 'Green'      
        case 3:
            for cr in arr:
                x, y, rvalue, gvalue, bvalue = cr
                load2[x,y] = (0, 0, bvalue)
                name = 'Blue'
        case 4:
            for cr in arr:
                x, y, rvalue, gvalue, bvalue = cr
                load2[x,y] = (0, gvalue, bvalue)
                name = 'Cyan'
        case 5:
            for cr in arr:
                x, y, rvalue, gvalue, bvalue = cr
                load2[x,y] = (rvalue,0, bvalue)
                name = 'Magenta'
        case 6:
            for cr in arr:
                x, y, rvalue, gvalue, bvalue = cr
                load2[x,y] = (rvalue, gvalue, 0)
                name = 'Yellow'

    sizing3 = pics3.resize((204,204))  
    photo3 = PIL.ImageTk.PhotoImage(sizing3)
    my_label2 = Label(image=photo3)
    my_label2.image = photo3
    my_label2.place(x= 550, y=100)

# Fungsi untuk menyimpan gambar
def save():
    pics3.save(f"Hasil/{file_name}_{name}.png")

# Fungsi untuk keluar dari window
def exitl():
    root.destroy()

# Pemanggilan fungsi blank
blank()

# Deklarasi radio button                  
var = IntVar()

# Radio button
R1 = Radiobutton(root, text="RED", variable=var, value=1, height=1, width=6, command= lambda: sel(1))
R1.place(x = 550,y = 320)

R2 = Radiobutton(root, text="GREEN", variable=var, value=2, height=1, width=8, command= lambda: sel(2))
R2.place(x = 610,y = 320)

R3 = Radiobutton(root, text="BLUE", variable=var, value=3, height=1, width=6, command= lambda: sel(3))
R3.place(x = 690,y = 320)

R4 = Radiobutton(root, text="CYAN", variable=var, value=4, height=1, width=5, command= lambda: sel(4))
R4.place(x = 550,y = 345)

R5 = Radiobutton(root, text="MAGENTA", variable=var, value=5, height=1, width=8, command= lambda: sel(5))
R5.place(x = 610,y = 345)

R6 = Radiobutton(root, text="YELLOW", variable=var, value=6, height=1, width=6, command= lambda: sel(6))
R6.place(x = 690,y = 345)

# Button open image
tombol = Button(root, text='OPEN IMAGE', command=koordinat, height=1, width=28)
tombol.place(x = 50,y = 320)

# Button copy
tombol2 = Button(root, text="COPY", command=hasil_copy, height=1, width=28)
tombol2.place(x = 300,y = 320)

# Button save image
tombol3 = Button(root, text="SAVE IMAGE", command=save, height=1, width=28)
tombol3.place(x = 550,y = 390)

# Button reset
tombol4 = Button(root, text="RESET", command=blank, height=1, width=28)
tombol4.place(x = 550,y = 420)

# Button exit
tombol5 = Button(root, text="EXIT", command=exitl, height=1, width=28)
tombol5.place(x = 550,y = 450)

# Mainloop window tkinter
root.mainloop()

