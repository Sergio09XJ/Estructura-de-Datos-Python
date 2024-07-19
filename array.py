import random 

class Array:
    def __init__(self, capacidad, item = None): 
        self.items = list()
        for i in range(capacidad):
            self.items.append(item)
   
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__ (self): 
        return iter(self.items)
    
    def __getitem__(self, index): 
        return  self.items[index]
    
    def __setitem__(self, index, value):
         self.items[index] = value 
         return self.items
    
    def __replace_item__(self):
        value = input("¿Como prefieres remplazar tus valores? Aleatorios -> A o Secuenciales -> S: ")
        value = value.upper()
        while value != "A" and value != "S":
            value = input("\nLos valores que me diste no son correctos; A para Aleatorios o S para Secuenciales: ")
            value = value.upper()
        if value == "A": 
            for i in range(self.__len__()):
                self.items[i] = random.randint(1,100)
            return self.items    
        elif value == "S": 
            valor = 1 
            for i in range(self.__len__()):
                self.items[i] = valor
                valor += 1
            return self.items
            

    def __sum_items__(self): 
     iterator = self.__iter__()
     primer_v =  next(iterator)
     if isinstance(primer_v,int):
         for elemento in iterator: 
             primer_v += elemento
         return primer_v 
     elif isinstance(primer_v,str): 
         for elemento in iterator: 
             primer_v += elemento
         return primer_v 
     else:
         raise ValueError ("Todos los elementos deben ser del mismo tipo para ser sumados. ")



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




