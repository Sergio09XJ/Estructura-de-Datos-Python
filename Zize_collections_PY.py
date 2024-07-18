import sys 

collections = {"List":list(),"Tuple":tuple(),"Set":set(),"Dict":{}}

for keys, values in collections.items():
    print(f"{keys} : {sys.getsizeof(values)} bytes")

