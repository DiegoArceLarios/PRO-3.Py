import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#ReceptorPNG= 'D:/Receptores/ReceptorPNG'
#ReceptorLNK= 'D:/Receptores/ReceptorLNK'
#ReceptorWEBP= 'D:/Receptores/ReceptorWEBP'
Receptores='D:/Receptores'
#Emisor= 'D:/Descargas generales'
#Busqueda1 = os.listdir(Emisor)


class FileEventHandler (FileSystemEventHandler):
    def on_move(self, event):
        print(f"¡Alerta, alquien ha movido {event.src_path} de su carpeta original")
        
    def on_created(self, event):
        print(f"¡Alerta, alquien ha creado {event.src_path} en su carpeta original")

    def on_deleted(self, event):
        print(f"¡Alerta, alquien ha borrado {event.src_path} de su carpeta original")

    def on_modified(self, event):
        print(f"¡Alerta, alquien ha modificado {event.src_path} de su carpeta original")    

eventos= FileEventHandler
ver = Observer()
ver.schedule(eventos, Receptores, recursive=True)
ver.start()
try:
    while True:
        time.sleep(2)
        print('Buscando')
except KeyboardInterrupt:
    print('El watchdog se ha detenido')
    ver.stop


#for i in Busqueda1:
 #   n,path= os.path.splitext(i)
  #  if path == '.png':
   #     doc = Emisor+'/'+i 
    #    shutil.move(doc,ReceptorPNG)
    #if path == '.lnk':
    #    doc = Emisor+'/'+i
     #   shutil.move(doc,ReceptorLNK)
    #if path == '.webp':
     #   doc = Emisor+'/'+i
      #  shutil.move(doc,ReceptorWEBP)
    #else:
     #   print('')
    #print('hi')





