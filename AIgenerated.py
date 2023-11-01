from tkinter import *
from tkinter import ttk, Tk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text
def data():
    s=comb_sor.get() #s=source
    d=comb_dest.get() #d=destination
    masg=Sor_txt.get(1.0,END)
    #Translate
    textget=change(text=masg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)

# combo box will come
root: Tk=Tk() #object making
root.title("Translator")
root.geometry("700x600")
root.config(bg='aqua')
lab_txt=Label(root,text="Google Translator",font=("Time New Roman",20,"bold"),bg="white")
lab_txt.place(x=200,y=40,height=30,width=320)
frame=Frame(root).pack(side=BOTTOM)#varaiable creating
#text box--source

lab_txt=Label(root,text="Input Text",font=("Time New Roman",20,"bold"),fg="black")
lab_txt.place(x=200,y=90,height=30,width=320)

Sor_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
Sor_txt.place(x=180,y=130,height=130,width=350)

list_text=list(LANGUAGES.values())

comb_sor=ttk.Combobox(frame,value=list_text)
comb_sor.place(x=50,y=280,height=40,width=150)
comb_sor.set("english")

button_change=Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=270,y=280,height=40,width=150)

comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=490,y=280,height=40,width=150)
comb_dest.set("english")

lab_txt=Label(root,text="Output Text",font=("Time New Roman",20,"bold"),fg="black")
lab_txt.place(x=200,y=350,height=30,width=320)

dest_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=180,y=390,height=135,width=350)

root.mainloop()
