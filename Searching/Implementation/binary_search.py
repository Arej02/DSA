
def binary_search(arr,low,high,value):

    if low>high:
        return -1
    
    mid=(low+high)//2

    if arr[mid]==value:
        return mid
        
    elif arr[mid]>value:
        return binary_search(arr,low,mid-1,value)

    return binary_search(arr,mid+1,high,value)



arr=[1,2,3,4,5,6,7,8,100]
result=binary_search(arr,0,len(arr)-1,8)
print(result)