import tkinter as tk
import tkinter.ttk as ttk

from MedidasSenseHat import *


class Aplicacion:
    def __init__(self, Periodo):
        
        self.Periodo=Periodo
        self.midiendo=True
    
        self.ventana=tk.Tk()
        self.ventana.title("Práctica GUI SenseHat")

        #---------PRIMER CUADRO----------
        self.labelframe1=ttk.LabelFrame(self.ventana, text="Control")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)        


        #button
        self.boton=tk.Button(self.labelframe1, text="Para", bg="red", command=self.estado_boton)
        self.boton.grid(column=0,row=2)

        #texto
        self.label=ttk.Label(self.labelframe1,text="Periodo: ")
        self.label.grid(column=0, row=3)
        self.label2=ttk.Label(self.labelframe1,text= self.Periodo)
        self.label2.grid(column=1, row=3)
        
        #---------SEGUNDO CUADRO----------
        self.labelframe2=ttk.LabelFrame(self.ventana, text="Medidas")        
        self.labelframe2.grid(column=0, row=4, padx=5, pady=10)


        #Intro textvariable
        self.label3=ttk.Label(self.labelframe2,text="", width=15)
        self.label3.config(background="white")
        self.label3.grid(column=1,row=5)
        
        #radiobutton
        self.seleccion=tk.IntVar()
        self.seleccion.set(3)

        self.radio1=tk.Radiobutton(self.labelframe2,text="Temperatura", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=6)
        self.radio2=tk.Radiobutton(self.labelframe2,text="Presión", variable=self.seleccion, value=2)
        self.radio2.grid(column=1, row=6)
        self.radio3=tk.Radiobutton(self.labelframe2,text="Humedad", variable=self.seleccion, value=3)
        self.radio3.grid(column=2, row=6)   

        self.label3.after(self.Periodo,self.medir)
        self.ventana.mainloop()


    def medir(self):
        
        self.sense=medida()
        if self.midiendo:

            if self.seleccion.get()==1:
                self.label3.config(text=self.sense[0])
                #print(self.sense[0])

            elif self.seleccion.get()==2:
                self.label3.config(text=self.sense[1])
                #print(self.sense[1])

            else :
                self.label3.config(text=self.sense[2])
                #print(self.sense[2])
            
        
        self.label3.after(self.Periodo,self.medir)
            

    def estado_boton(self):

        if self.midiendo==True:
            self.boton.configure(bg="green")
            self.boton.configure(text="Sigue")
            self.midiendo=False
        else:
            self.boton.configure(bg="red")
            self.boton.configure(text="Para")
            self.midiendo=True
            self.medir()



 

aplicacion1=Aplicacion(1000)