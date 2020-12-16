#code 

for i in range(0,9):
    for j in range(0,5):
        if i-j>=0:
            if i+j<=8:
                print("*",end="")
            
        else:
            print(" ",end="")
    print("\n")
    
    
    ##OUTPUT
    
*    

**   

***  

**** 

*****

****

***

**

*
