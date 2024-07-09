def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

def partition(arr,p,r):
    pivot=arr[r]
    i=p-1
    for  j in range(p,r):
        if(arr[j]<=pivot):
            i+=1
            swap(arr,i,j)
    swap(arr,i+1,r)
    return  i+1

def quick_sort(arr,p,r):
    if(p<r):
        q=partition(arr,p,r)
        quick_sort(arr,p,q-1)
        quick_sort(arr,q+1,r)

