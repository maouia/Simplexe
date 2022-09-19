import numpy as np
import os
os.system('cls')


#max in array
def maxT(t) :
    max = t[0]
    index=0
    for i in range(1,len(t)):
        if t[i] > max:
            max = t[i]
            index = i
    return index 
#min in array
def minT(t) :
    min = t[0]
    index=0
    for i in range(1,len(t)):
        if t[i] < min:
            min = t[i]
            index = i
    return index 

#retourner l'indice de variable a chonger
def variableSmin():
    min=100
  
    indexMin=[0,minT(Fobject)]
    for i in range(m.shape[0]):
        if m[i][minT(Fobject)]>0:
            
            if b[i]/m[i][minT(Fobject)]<min :
                min =b[i]/m[i][minT(Fobject)]
                indexMin[0]=i
                indexMin[1]=minT(Fobject)
    
    return indexMin


#retourner l'indice de variable a changer
def variableS():
    min=100
  
    indexMin=[0,maxT(Fobject)]
    for i in range(m.shape[0]):
        if m[i][maxT(Fobject)]>0:
            
            if b[i]/m[i][maxT(Fobject)]<min :
                min =b[i]/m[i][maxT(Fobject)]
                indexMin[0]=i
                indexMin[1]=maxT(Fobject)
    
    return indexMin


#permet de faire le pivotage a 1
def pivotage1Matrix(variableSort):
    pivotageLine=[]
    variable=m[variableSort[0]][variableSort[1]]
    for j in range(m.shape[1]):
        m[variableSort[0]][j]=m[variableSort[0]][j]/variable
        pivotageLine.append(m[variableSort[0]][j])
    b[variableSort[0]]=b[variableSort[0]]/variable
    return pivotageLine

#permet de faire le pivotage a 0
def pivotage0Matrix(pivotageLine,variableSort) :
    i=0
    print(z)
    while i < m.shape[0]: 
        if i != variableSort[0] :
            variable=m[i][variableSort[1]]
            for j in range(m.shape[1]):
                m[i][j]=m[i][j]-(pivotageLine[j]*variable)
            b[i]=b[i]-(b[variableSort[0]]*variable)
                
        i+=1
    




def pivotageLignePivo(Fobject,pivotageLine,variableSort,z):
    variable= Fobject[variableSort[1]]
    for i in range(Fobject.shape[0]):
        Fobject[i]=Fobject[i]-(pivotageLine[i]*variable)
    z=z-(b[variableSort[0]]*variable)
    return z

    



#inicial matice
J=[2,3,4,5]

m = np.array([
  [2.0  ,1.0  ,1.0  ,0.0  ,0.0  ],
  [1.0  ,2.0  ,0.0  ,1.0  ,0.0  ],  
  [1.0  ,0.0  ,0.0  ,0.0  ,1.0  ]])

b= np.array([8.0  ,7.0  ,3.0  ])
Fobject=np.array([4.0, 5.0, 0.0, 0.0, 0.0])
z=0
print(m)
print(b)
print(Fobject)
print(J)

a= input("click 1 pour maximiser et 2 minimiser")


if(a=="1"):
    while(Fobject[maxT(Fobject)] >0):
        
        variableSort=variableS()
        
        J[variableSort[0]]=variableSort[1]

        pivotageLine=pivotage1Matrix(variableSort)
                    
        pivotage0Matrix(pivotageLine,variableSort)

        z=pivotageLignePivo(Fobject,pivotageLine,variableSort,z)



        print(m)
        print(b)
        print(Fobject)
        print(z)    
        print(J)

else :
    while(Fobject[minT(Fobject)] <0):
        
        variableSort=variableSmin()
        
        J[variableSort[0]]=variableSort[1]

        pivotageLine=pivotage1Matrix(variableSort)
                    
        pivotage0Matrix(pivotageLine,variableSort)

        z=pivotageLignePivo(Fobject,pivotageLine,variableSort,z)

        print(m)
        print(b)
        print(Fobject)
        print(z)    
        print(J)










