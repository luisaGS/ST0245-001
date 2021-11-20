import os
import numpy as np
import math
from time import time
def compresionConPerdidas(src_data, dst_height, dst_width):
      #comprimir...
      ori_height, ori_width = src_data.shape
      ratio_height = ori_height / dst_height
      ratio_width = ori_width / dst_width
      dst_data = np.zeros((dst_height, dst_width), np.uint8)

      for y in range(dst_height):
          for x in range(dst_width):
              x_ori = int(x * ratio_width)
              y_ori = int(y * ratio_height)          #Redondeo
              dst_data[y, x] = src_data[y_ori, x_ori]
      return dst_data
def vecinoDescompresion(archivo,tamano):  
    copia=np.copy(archivo) 
    filas,columnas=copia.shape 
    
    
    filaSalida=int(filas*tamano)  
    columnaSalida=int(columnas*tamano) 
 
    salida=np.zeros((filaSalida,columnaSalida)) 
    
    if tamano==1:  
        salida=copia
    else:   
        contadorFilas=0  
        for i in range(filaSalida): 
            contadorColumnas=0              #O(NM)
            for j in range(columnaSalida): 
                salida[i,j]=copia[int(math.floor(contadorFilas/tamano)),int(math.floor(contadorColumnas/tamano))]  
                contadorColumnas+=1 
                if j+1>=columnaSalida: 
                    break   
            contadorFilas+=1  
            if i+1>=filaSalida: 
                break  
    return salida  

    

def main():
  ruta = r"C:\Users\Luisa Garcia\OneDrive - Universidad EAFIT\Escritorio\Ingeniería matematica\2021-2\Estructura de datos y algoritmos\Proyecto\Compresion\Originales_csv"  #ruta relativa del archivo
  #ruta2= "..\csv\Comprimidos_VecinosCercanos" 
  #"C:\Users\Luisa Garcia\OneDrive - Universidad EAFIT\Escritorio\Ingeniería matematica\2021-2\Estructura de datos y algoritmos\Proyecto\Compresion\Comp_vecino"
  i=1
  j=0
  v=0
  b=1 
 # listaDeArchivo2 = os.listdir(ruta2) 
  f=str(i)
  listaDeArchivo = os.listdir(ruta)  #se ponen los archivos en una lista
  for archivo in listaDeArchivo: #se ejecuta el proceso en cada archivo de la lista
      ArchivoT = listaDeArchivo[j] #se crea un archivo temporal
      j+=1
      print(ArchivoT)     
      #se carga el archivo en una matriz numpy
      matriz2 = np.loadtxt(ruta+"/"+ArchivoT, delimiter = ",")
      print(matriz2)
      
      #se sacan las dimensiones de la matriz
      alto = matriz2.shape[0]
      ancho = matriz2.shape[1]
      #se ejecuta el escalamiento de imagen
      matrizC = compresionConPerdidas(matriz2,alto//2,ancho//2)
      print(matrizC)
      f=str(i)
      #se guarda la matriz como csv en la carpeta de destino
      #grabarEnUnArchivoCSV("prueba"+f+".csv",matriz2)
      np.savetxt("Comp_vecino\\"+"prueba"+f+".csv",matrizC.astype(int), fmt='%i', delimiter = ",")
      i += 1
'''
    for archivo in listaDeArchivo2:
      ArchivoT = listaDeArchivo2[v]
      v+=1      
      print(ArchivoT)
      matriz3 = np.loadtxt(ruta+"/"+ArchivoT, delimiter = ",")
      print(matriz3)      
      matrizD = vecinoDescompresion(matriz3,2)            
      c=str(b)
      np.savetxt("Descomprimidos_VecinosCercanos\\"+"prueba"+c+".csv",matrizD.astype(int), fmt='%i', delimiter = ",")
      b+=1  
'''
      
main()