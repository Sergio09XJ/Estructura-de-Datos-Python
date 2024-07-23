
import random #Importamos random para su uso posterior. 

class Array: #Creamos la clase Array, tendra métodos y atributos para un array. 
    def __init__(self, capacidad, item = None): #El constructor, pedimos la capacidad del array. 
        self.items = list() #Cremamos el array como una lista en python. 
        for i in range(capacidad): #Usamos este for para iterar hasta el valor dado en el objeto. 
            self.items.append(item) #Agregamos item a los valores del array self.items

    def __getitem__(self, index):  #Método __getitem__ -> Retornamos el valor que nos pida el usuario con el index del array. 
        return  self.items[index] #Retorno. 
    
    def __setitem__(self, index, value): #Método __setitem__ -> Cambiamos el valor de uno de los array al que nos pida el usuario. 
         self.items[index] = value  #Cambio 
         return self.items     #Retorno con el cambio    
   
    def __len__(self):#Método __len__ -> Retornamos la longitud del array.
        return len(self.items)
    
    def __str__(self):#Método __str__ -> Retornamos el array como un str. 
        return str(self.items)
    
    def __iter__ (self): # Método __iter__ -> Retornamos un iterador del array. 
        return iter(self.items)
    
    def __replace_item__(self): #Método __replace_item__ -> Replazamos los valores del array. 
        value = input("¿Como prefieres remplazar tus valores? Aleatorios -> A o Secuenciales -> S: ") #Le damos 2 opciones al usuario a cambiar los valores y los guardamos. 
        value = value.upper() #Este valor lo pasamos a Mayuscula para evitar problemas. 
        while value != "A" and value != "S": #Iterador en caso de que el usuario ponga un valor erroneo. 
            value = input("\nLos valores que me diste no son correctos; A para Aleatorios o S para Secuenciales: ")#Pedimos el valor de nuevo. 
            value = value.upper() #Lo volvemos a pasar a mayuscula. 
        if value == "A":  #Si el valor es A...
            for i in range(self.__len__()): #Ietador para cambia  pasar por cada valor del array. 
                self.items[i] = random.randint(1,100) #Usando la función randint de la biblioteca randomo con un intervalo de 1 a 100, guardamos números al azar. 
            return self.items  #Retornamos el array. 
        elif value == "S": #Si el valor es S
            valor = 1 #Lo inicializamos con 1
            for i in range(self.__len__()): #Iteramos cada valor del array. 
                self.items[i] = valor #Guardamos valor en el array
                valor += 1 #Sumamos 1 al valor para la siguiente iteración 
            return self.items #Retornamos el array terminado la iteración. 
            

    def __sum_items__(self): #Método __sum_items__ -> Suma los valores del array. 
     iterator = self.__iter__() #Creamos un iterador con el método iter. 
     primer_v =  next(iterator) #Guardamos el primer valor del array 
     if isinstance(primer_v,int): #Si el primer valor es entero
         for elemento in iterator:  #Itermamos el array con el iterador. 
             primer_v += elemento #Sumamos al primer_v
         return primer_v #Retoransmo la suma. 
     elif isinstance(primer_v,str): #Si el primer valor es un caracter o string.  
         for elemento in iterator: #Iteramos el array con el iterador. 
             primer_v += elemento #Vamos sumando al iterado. 
         return primer_v #Retornamos la cadena. 
     else: #En caso de que el array tenga distintos tipos de valores 
         raise ValueError ("Todos los elementos deben ser del mismo tipo para ser sumados. ")
         #Lanzamos un ValueError... 

if __name__ == "__main__": 
 array = Array(5)
 print(array.__len__())
 print(array.__str__())
 print(array.__getitem__(4))
 print(array.__setitem__(3,"a"))
 print(array.__replace_item__())
 print(array.__sum_items__())

 iterador = array.__iter__()

 array[0] = "H"
 array[1] = "o"
 array[2] = "l"
 array[3] = "a"
 array[4] = "a"

 print(array.__str__())
 print(array.__sum_items__())



