


liste = [[["ahmet","mehmet","azra"],"turgut"],"azra","zeynep","azra"]

def myFunc(degisken,seen=None):
    if seen is None:
        seen = set()
    for x in degisken:
        if(type(x)==list):
            myFunc(x)
        else:
            bos = []
            bos.append(x)
            t = set(bos)
            a = list(t)
            print(a)  
      

myFunc(liste)
    
