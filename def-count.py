value = input('Enter a value: ')

lst = [1,2,3,5,8,10,6,8,4,8,7,'s',0.5,-1,'s',0.5,'m',-2,0.5]

def countt(lst : list ,value : (int,str,float)) -> int :
    x = []
    for i in lst :
        if str(i) == value :
            x = x + [i]
    print(len(x))

countt(lst,value)    
