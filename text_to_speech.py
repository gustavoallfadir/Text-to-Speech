from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from gtts import gTTS
from pygame import mixer
import os



#MAIN---------------------------------------
def main():

    root=Tk()
    root.title("Text to speech")
    root.geometry("600x500+300+50")
    root.minsize(400,200)
   

    #CAJA DE TEXTO--------------------------
    boxframe=Frame(root)
    boxframe.pack(fill="both", expand="true", padx=10,pady=10)

    textbox=Text(boxframe, height=3, width=20, wrap=WORD)
    textbox.pack(fill="both",expand="true", side="left")

    scrollvert=Scrollbar(boxframe, command=textbox.yview)
    scrollvert.pack(side="left",fill="y")

    textbox.config(yscrollcommand=scrollvert.set)

    #LISTA DE IDIOMAS------------------------

    idiomas=['Español','Inglés','Italiano','Francés','Alemán','Portugués']

    lang_box=Listbox(boxframe, height=5)
    lang_box.pack( side="left",fill="y")

    scrollvert2=Scrollbar(boxframe, command=lang_box.yview)
    scrollvert2.pack(side="left",fill="y")

    lang_box.config(yscrollcommand=scrollvert2.set)


    for item in idiomas:
        lang_box.insert(END, item)


    #BOTONES--------------------------------
    buttonframe=Frame(root)
    buttonframe.pack()

    button_play=Button(buttonframe,text="Reproducir",bd=3, command=lambda:reproducir())
    button_play.grid(row=0, column=0, padx=20, pady=10)

    button_export=Button(buttonframe, text="Exportar",bd=3, command=lambda:exportar())
    button_export.grid(row=0,column=1, padx=20, pady=10)

    #--------Barra de menu----------
    
    barramenu=Menu(root)
    root.config(menu=barramenu)


    menuArchivo=Menu(barramenu, tearoff=0)
    menuArchivo.add_command(label="Salir     ", command=lambda:salir())


    menuAyuda=Menu(barramenu,tearoff=0)
    menuAyuda.add_command(label="Acerca de     ",command=lambda:acerca_de())

    #-----------Textos de la barra menu----------

    barramenu.add_cascade(label="Archivo     ",menu=menuArchivo)
    barramenu.add_cascade(label="Ayuda     ",menu=menuAyuda)


    codes={'Español':'es','Inglés':'en','Italiano':'it','Francés':'fr','Alemán':'de','Portugués':'pt'}

        #---------------Funciones--------------------
    def reproducir():
     
        lang=lang_box.get(ACTIVE)

        lang_code=codes.get(lang)

        texto=textbox.get(1.0,END)
        tts=gTTS(texto, lang=lang_code)
        tts.save('tmp.mp3')
        mixer.init()
        mixer.music.load('tmp.mp3')
        mixer.music.play()

    def exportar():
        filename=filedialog.asksaveasfilename(filetypes =[('Audio mp3', '*.mp3')])
        
        lang=lang_box.get(ACTIVE)
        lang_code=codes.get(lang)

        texto=textbox.get(1.0,END)

        tts=gTTS(texto, lang=lang_code)
        
        tts.save(filename)


        


    def acerca_de():
        messagebox.showinfo("Text to speech","Creado por Gustavo Allfadir\nTodos los derechos reservados.\n©2020")
        
    #función para salir
    def salir():
        try:
            os.remove('temp.mp3')
        except:
            pass

        root.destroy() 
        

    #MAINLOOP
    root.mainloop()




main()