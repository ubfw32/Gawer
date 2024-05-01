import re
import os
import datetime
import shutil
import time
from collections import Counter

#shutil.unpack_archive('Proyecto+Dia+9.zip')

dir = 'D:\\PROGRAMAR\\PYTHON\\Clases notas\\CLASES\\DIA 9\\Mi_Gran_Directorio'#\carpetas\subcarpetas

#lista = os.listdir(dir)
#print(lista)

def buscador(dir):
    for carpetas, subcarpetas, archivos in os.walk(dir):
        for archivo in archivos:
            codigo = re.findall(r'^\w\w{3}\d{5}', archivo)
            print(codigo)
            if codigo is not None:
                listc = list(Counter(codigo))
                print(f"Fecha de búsqueda: [{datetime.date.today()}]")
                print(f"ARCHIVO        NRO.SERIE\n"
                      f"-------        ----------\n"
                      f"{archivos}     {codigo}\n")
                print(f"\n\nNumeros encontrados: {archivo}")



buscador(dir)

'''inicio = time.time()
buscador(directorio)
final = time.time()
duracion = final - inicio
print(f"Duración de la búsqueda: {duracion}")



        for archivo in archivos:
            ruta_archivo = os.path.join(subcarpeta, archivo)
            op = open(ruta_archivo, 'r' )
            leer = op.read()
            codigo = re.findall(r'^\w\w{3}\d{5}', leer)
            if codigo is not None:
                listc = list(Counter(codigo))
                print(f"Fecha de búsqueda: [{datetime.date.today()}]")
                print(f"ARCHIVO        NRO.SERIE\n"
                      f"-------        ----------\n"
                      f"{archivos}     {codigo}\n")
                print(f"\n\nNumeros encontrados: {codigo.count(codigo)}")

carpetas = re.search(r'D\w{9}_\d')
re.search(r'\w{10}_\d\w')
'''







