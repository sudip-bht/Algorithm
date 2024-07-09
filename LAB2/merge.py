import math
def merge_sort(arr,p,r):
    if(p<r):
        q=math.floor((p+r)/2)   #calculates the midpoint of the array
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r) 
        merge(arr,p,q,r)    
  

def merge(arr,p,q,r):
    n1=q-p+1
    n2=r-q
    #initailzing left and right array with all zeros
    L=[0]*(n1+1)
    R=[0]*(n2+1)
    for i  in range(0,n1):
        L[i]=arr[p+i]
    for j in range(0,n2):
        R[j]=arr[q+j+1]
    L[n1]=math.inf
    R[n2]=math.inf
    i=0
    j=0
    for k in range(p,r+1):
        if(L[i]<=R[j]):
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1



   
   




