
def insertion_sort(arr:list):

    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
    return arr

result=insertion_sort([34,89,67,1,2,45,90])
print(result)

