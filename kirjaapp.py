import sys

import tkinter
import tkinter.font
import tkinter.filedialog
#from tkinter import *

pohja = tkinter.Tk()

entries = []

clicked = 0

kindex = 0
kirjat = []


# About binary file handling:
# website: https://www.tutorialsteacher.com/python/python-read-write-file?utm_content=cmp-true
# reading under "Reading Binary File"
# writing under "Writing to a Binary File"

# https://www.w3schools.com/python/python_json.asp

def addbut(event):
    global kindex
    # add current selection
    name = entries[0].get()
    author = entries[1].get()
    year = entries[2].get()
    pages = entries[3].get()
    publisher = entries[4].get()
    genre = clicked.get()
    obj = [name,author,year,pages,publisher,genre]
    kirjat.append(obj)
    j = 0
    while (j<5):
        entries[j].delete(0,last=len(entries[j].get()))
        #entries[j].insert(0,"")
        j += 1
    clicked.set("Excitement")
    kindex += 1
    print("save")

def SaveFile():
    #selection = clicked.get()
    fname = tkinter.filedialog.asksaveasfilename(master=pohja,title="Save file")
    # same as savebut, but to file
    try:
        f = open(fname, 'w+')
    except:
        tkinter.messagebox.showerror("Error","Can't save file.")
        pohja.destroy()
        sys.exit(0)
    j = 0;
    while (j<len(kirjat)):
        obj = kirjat[j]     
        try:
            f.write(obj[0]+";"+obj[1]+";"+obj[2]+";"+obj[3]+";"+obj[4]+";"+obj[5]+";"+"\n")
        except:
            tkinter.messagebox.showerror("Error","Error writing file.")
            pohja.destroy()
            sys.exit(0)
        j += 1
    f.close()
    print("File saved");

def LoadFile():
    global kindex
    global kirjat
    fname = tkinter.filedialog.askopenfilename(master=pohja,title="Load file")
    try:
        f = open(fname, 'r')
    except:
        tkinter.messagebox.showerror("Error","Can't load file.")
        pohja.destroy()
        sys.exit(0)
    j = 0
    kirjat = []
    kindex = 0
    while (True):
        try:
            rivi = f.readline()
        except:
            tkinter.messagebox.showerror("Error","Error reading file.")
            pohja.destroy()
            sys.exit(0)
        if (len(rivi)==0):
            break
        rivi = rivi[:-1]
        sarakkeet = rivi.split(';')
        obj = [sarakkeet[0],sarakkeet[1],sarakkeet[2],sarakkeet[3],sarakkeet[4],sarakkeet[5]]
        kirjat.append(obj)
        k = 0
        while (k<5):
            entries[k].delete(0,last=len(entries[k].get()))
            entries[k].insert(0,sarakkeet[k])
            k += 1
        j += 1
        kindex += 1
    
    clicked.set(sarakkeet[5])
    print(rivi)
    f.close()
    print("File loaded")

def Exit():
    pohja.destroy()
    sys.exit(0)

def view():
    # what was purpose of this
    print("view")

def about():
    tkinter.messagebox.showinfo("Information","This was made by gameguys.")

def up(event):
    global kindex
    global kirjat
    if (kindex>0):
        kindex -= 1
        #print(kindex)
        #print(kirjat)
        obj = kirjat[kindex]
        k = 0
        while (k<5):
            entries[k].delete(0,last=len(entries[k].get()))
            entries[k].insert(0,obj[k])
            k += 1
        clicked.set(obj[5])

def down(event):
    global kindex
    if (kindex<len(kirjat)-1):
        kindex += 1
        obj = kirjat[kindex]
        k = 0
        while (k<5):
            entries[k].delete(0,last=len(entries[k].get()))
            entries[k].insert(0,obj[k])
            k += 1
        clicked.set(obj[5])

pohja.title("Books I've Read")
#pohja.columnconfigure(0,minsize=600)
#pohja.rowconfigure([0,1,2,3],minsize=100)

#f = tkinter.font.Font
f = tkinter.font.Font(family="times", size=20, weight=tkinter.NORMAL)
f2 = tkinter.font.Font(family="helvetica",size=12,weight=tkinter.NORMAL)
#print(f2.metrics("linespace", displayof=pohja))

kehys = tkinter.Frame(master=pohja, width=600, height=600)
kehys.pack()

stitle = "Books I've Read"
labeli = tkinter.Label(text=stitle,font=f)
labeli.place(x=10,y=5)

ypos = 5

values = []
values.append("Name:")
values.append("Author:")
values.append("Year:")
values.append("Pages:")
values.append("Publisher:")
labels = []

i = 0
while (i<5):
    labels.append(tkinter.Label(text=values[i]))
    entries.append(tkinter.Entry(master=pohja))   
    i += 1

i = 0
ypos += 40
while (i<5):
    labels[i].place(x=50,y=ypos)
    entries[i].place(x=200,y=ypos)
    i += 1
    ypos += 40

genre = [
    "Excitement",
    "Crime",
    "Scifi"
]

lgenre = tkinter.Label(text="Genre")
lgenre.place(x=50,y=ypos)

# datatype of menu text
clicked = tkinter.StringVar()
# initial menu text
clicked.set("")
# Create Dropdown menu
drop = tkinter.OptionMenu(pohja, clicked, *genre)
drop.place(x=200,y=ypos)

sbut = "Add"
buts = tkinter.Button(text=sbut,master=pohja,width=10,height=1,font=f2)
buts.bind("<Button-1>",addbut)
buts.place(x=40,y=ypos+50)

sbutu = "Up"
butsu = tkinter.Button(text=sbutu,master=pohja,width=10,height=1,font=f2)
butsu.bind("<Button-1>",up)
butsu.place(x=40,y=ypos+100)

sbutd = "Down"
butsd = tkinter.Button(text=sbutd,master=pohja,width=10,height=1,font=f2)
butsd.bind("<Button-1>",down)
butsd.place(x=40,y=ypos+150)

#4) Menu on upper left corner (windows edge)
#a) File
#i) Save
#ii) Load
#iii) Exit
#b) View
#c) About
#i) information about the application

menu = tkinter.Menu(pohja)
pohja.config(menu=menu)
filemenu = tkinter.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save", command=SaveFile)
filemenu.add_command(label="Load", command=LoadFile)
filemenu.add_command(label="Exit", command=Exit)

viewmenu = tkinter.Menu(menu)
menu.add_cascade(label="View", menu=viewmenu)
viewmenu.add_command(label="View",command=view)

aboutmenu = tkinter.Menu(menu)
menu.add_cascade(label="About", menu=aboutmenu)
aboutmenu.add_command(label="About",command=about)

pohja.mainloop()
