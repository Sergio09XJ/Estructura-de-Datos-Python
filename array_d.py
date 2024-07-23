from array_u import Array #Importamos el módulo array_u 
import random #Igualmente importamos la biblioteca random. 

class Array_d: #Creamoas la clase Array_d para la matriz/aray de 2da dimesión. 
    def __init__(self, columns, filas, item = None):  #Pedimos las filas y columnas de este. 
        self.data = Array(columns) #Creamos un array en donde por cada index tendra otro array. 
        for column in range(columns): #Iteramos por cada valor de la columna. 
            self.data[column] = Array(filas, item) #En cada indice creamos otro array del tamaño de las filas. 

    def __getitem__(self,  row): #Método __getitem__ -> Retornamos cada fila. 
       return self.data[row]   
    8
    def __setitem__(self,col, row, value): #Método __setitem__ -> Cambiamos el valor en especifico de una fila 
        self.data[col][row] = value 
    
    def __len__(self): #Método __len__ -> Retornamos la longitud de la columna. 
        return len(self.data[0]) 
            
    def __height__(self): #Método __height__ -> Retornamos la longitud de la columna. 
        return len(self.data) 

    def __width__(self): #Método __width__ -> Retornamos la longitud de la fila. 
        return len(self.__getitem__(0)) 

    def __str__(self): #Método __str__ -> Retornamos la matriz como un str. 
      guarda = ""
      for col in range(self.__height__()): 
          for fila in range(self.__width__()):
             guarda += str(self.data[col][fila]) + " "
          guarda  += "\n"
      return guarda   
    
    def __iter__(self): # Método __iter__ -> Retornamos un iterador de la matriz.
        return iter(self.data)
    
   
    
    def __replace_item__(self):  #Método __replace_item__ -> Replazamos los valores de la matriz 
       value = input("¿Como prefieres remplazar tus valores? Aleatorios -> A o Secuenciales -> S: ") #Le damos 2 opciones al usuario a cambiar los valores y los guardamos. 
       print(" ") #Salto de Linea 
       value = value.upper()#Este valor lo pasamos a Mayuscula para evitar problemas.
       while value != "A" and value != "S": #Iterador en caso de que el usuario ponga un valor erroneo. 
            value = input("\nLos valores que me diste no son correctos; A para Aleatorios o S para Secuenciales: ")#Pedimos el valor de nuevo. 
            print(" ") #Salto de Linea
            value = value.upper() #Lo volvemos a pasar a mayuscula. 
       if value == "A":  #Si el valor es A...
          for colum in range(self.__height__()):
             for row in range(self.__width__()): 
                  self.data[colum][row] = random.randint(1,100)             
       elif value == "S": #Si el valor es S  
           cont = 1 #Lo inicializamos con 1
           for colum in range(self.__height__()):
             for row in range(self.__width__()): 
                  self.data[colum][row] = cont 
                  cont += 1#Sumamos 1 al valor para la siguiente iteración 
    


if __name__ == "__main__":

 matrix = Array_d(5,3)
 print(matrix.__height__())
 print(matrix.__width__())
 print(matrix.__str__())

 matrix.__setitem__(1,1,2)
 print(matrix.__str__())
 print("\n ----------------------- ")
 matrix.__replace_item__()
 print(matrix.__str__())
 matrix.__setitem__(0,0,4)
 print(matrix.__str__())