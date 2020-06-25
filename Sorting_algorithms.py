def mergeSort(a,start,end):
    '''This function performs Merge Sort in place on the given array'''
    if start<end:
        mid=(start+end)//2
        mergeSort(a,start,mid)
        mergeSort(a,mid+1,end)
        merge(a,start,mid,end)

def merge(a,start,mid,end):
    i=start
    j=mid+1
    b=[0]*((end-start)+1)
    k=0
    while i<=mid and j<=end:
        if a[i]<a[j]:
            b[k]=a[i]
            k+=1
            i+=1
        else:
            b[k]=a[j]
            j+=1
            k+=1
    if i<=mid:
        for h in range(i,mid+1):
            b[k]=a[h]
            k+=1
    elif j<=end:
        for h in range(j,end+1):
            b[k]=a[h]
            k+=1
    k=0;
    for h in range(start,end+1):
        a[h]=b[k]
        k+=1


def quickSort(a,start,end):
    '''This function performs Quick Sort in place for the given array'''
    if start<end:
        pivot=quick(a,start,end)
        quickSort(a,start,pivot-1)
        quickSort(a,pivot+1,end)


def quick(a,start,end):
    i=start+1
    j=end
    pivot=a[start]
    while i<=end and j>=start:
        while a[i]<=pivot and i<end:
            i+=1
        while a[j]>pivot and j>start:
            j-=1
        if i<j:
            a[i],a[j]=a[j],a[i]
        else:
            break
    a[start],a[j]=a[j],a[start]
    return j



def insertionSort(arr,n):
    '''This function performs Insertion Sort in place'''
    i=1
    j=0
    while i<n:
        pivot=arr[i]
        k=j
        while k>=0 and pivot<arr[k]:
            arr[k+1]=arr[k]
            k-=1
        arr[k+1]=pivot
        j+=1
        i+=1



if __name__=='__main__':
    a=[5,1,2,3,7,4,11]
    le=6
    import timeit as t
    s=t.default_timer()
    insertionSort(a,len(a))
    q=t.default_timer()
    print(q-s)
    print(*a)