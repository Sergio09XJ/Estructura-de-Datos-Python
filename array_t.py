import random #Importamos random 
from array_u import Array #Importamos el módulo para crear array´s
from array_d import Array_d #Importamos el módulo para crear matrices. 


class Array_T:#Creamos la clase para crear array´s de 3 dimesiones. 
    def __init__(self, depth, row, column, item = None): #Recibimos 3 datos, la profundidad, las columnas, y las filas. 
        self.data = Array(depth) #Usando array_u creamos un array en self.data
        for dept in range(depth):#Usamos un iterador para crear matrices por cada valor del array. 
            self.data[dept] = Array_d(row, column, item) #En cada valor del array -> self.data creamos una matriz con Array_d.

    def __getitem__(self,depth, column, row): #Este método nos permite retornar el valor de este array tridimmencional. 
         return  self.data[depth][column][row]

    def __setitem__(self, depth, column, row, value): #Este método nos permite cambiar el valor de este array tidimencional. 
         self.data[depth][column][row] = value


    def __depth__(self): #Nos retorna la profundidad del array. 
        return len(self.data)
   
    #Cantidad de filas(Para este caso son 5) Pisos que construyen el edificio
    def __height__(self): #Nos retorna la cantidad de filas 
         return (len(self.data[0][0]))
         
          
    #Cantidad de columnas(para este caso son 2)#Hanchura del edificio. 
    def __width__(self): #nos retorna la cantidad de columnas. 
        return len(self.data[0].data)
       
    def __str__(self):#Este método nos retorna un string de todo el array. 
        matriz_t = "" #En esta variable guardamos el array Tridimencional. 
        for dept in range(self.__depth__()): #Ciclo para iterar por la profundidad. 
          for fila in range(self.__width__()): #Ciclo para iterar por cada fila. 
              for  columna in range(self.__height__ ()): #Ciclo para iterar cada columan
                  matriz_t += str(self.data[dept][fila][columna]) + " " #En matriz_t guardamos cada valor. 
              matriz_t += "\n" #Salto de liena por fila 
          matriz_t += "\n" #Salto de linea por columnas(matriz)
        return matriz_t   #Cuando termine retornamos la matriz.        
    
    def __replace_item__(self):  #Este método nos ayuda a cambiar los valores del array tri. en base a la decisión del usuario. 
        value = input("¿Como prefieres remplazar tus valores? Aleatorios -> A o Secuenciales -> S: ") #Guardamos la decion en una variable. 
        value = value.upper() #La pasamos a mayuscula para que sea legible. 
        while value != "A" and value != "S":#Mientras el valor no sea el indicado, iteraremos constantemente hasta que lo sea. 
            value = input("\nLos valores que me diste no son correctos; A para Aleatorios o S para Secuenciales: ") #Pedimos el valor de nuevo. 
            value = value.upper() #Lo hacemos legible. 
        if value == "A":#Si el valor es A
             for dept in range(self.__depth__()): #Iteramos por profundidad.
               for fila  in range(self.__width__()):#Iteramos cada fila 
                 for columna in range(self.__height__()):#Iteramos cada columna 
                     self.data[dept][fila][columna] = (random.randint(1,10)) #En cada valor, guardamos un número random. 
        elif value == "S":  #SI el valor es S
             cont = 1 #Inicializamos cont con 1
             for dept in range(self.__depth__()): #Profundidad
               for fila  in range(self.__width__()):#Fila
                 for columna in range(self.__height__()):#Columna
                     self.data[dept][fila][columna] = cont  #Guardamos el valor 
                     cont += 1    #Sumamos 1          
                    
 
                 
if __name__ == "__main__": 
 matrix_t = Array_T(3,5,2)

 print(matrix_t.__depth__())
 print(matrix_t.__height__())
 print(matrix_t.__width__())
 print(matrix_t.__str__())
 print(" ")

 matrix_t.__replace_item__()
 print(matrix_t.__str__())
 
 print(" ---------------------- ")
 print(matrix_t.__getitem__(1, 4, 0))
 print(" ---------------------- ")
 matrix_t.__setitem__(2, 1, 1, 909)
 print(matrix_t.__str__())
  