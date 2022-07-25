
#REQUIREMENTS --> INSTALE A BIBLIOTECA TKINTER E A BIBLIOTECA PYTUBE --> PARA INSTALAR, VÁ AO TERMINAL E DIGITE: pip install tkinter pytube


from pytube import YouTube
import tkinter as tk 

frame = tk.Tk() 
frame.title("Download de video do YouTube") 
frame.geometry('500x300') 
inp = 1
lbl = tk.Label(frame, text = "Cole o link do video") 
lbl.pack()
def salvar(): 
    global inp
    inp = link.get(1.0, "end-1c") 
    lbl.config(text = "Pronto! Pra cameçar a fazer o  download, por favor, feche esse aplicativo.\n Assim que o download terminar, o video aparecerá no seu diretório ")

link = tk.Text(frame, 
                   height = 1, 
                   width = 30) 
  
link.pack() 


lb = tk.Label(frame, text = "Qual resolução: 720p, 420p ou 360p") 
lb.pack() 



reso = 1
def resoluc():
    global reso
    reso = resotxt.get(1.0, "end-1c")
    lb.config(text = "Pronto! Agora clique em Iniciar download ")

    

resotxt = tk.Text(frame, height=1, width=10)
resotxt.pack()

resolucao = tk.Button(frame, 
                        text = "Pronto",  
                        command = resoluc) 
resolucao.pack()

salvarbutton = tk.Button(frame, 
                        text = "Iniciar Download",  
                        command = salvar) 
salvarbutton.pack() 


frame.mainloop()

yt = YouTube(f"{inp}")
yt.streams.get_by_resolution(f"{reso}").download()