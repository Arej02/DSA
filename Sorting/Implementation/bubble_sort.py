
# Bubble Sort:

def bubble_sort(arr:list)->list:

    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

result=bubble_sort([5,63,4,78,3,0,34,1])

print(result)

# Adaptive Bubble Sort:

def bubble_sort(arr:list)->list:
    
    for i in range(len(arr)-1):
        flag=0
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=1

        if flag==0:
            return arr
    return arr

result=bubble_sort([5,63,4,78,3,0,34,1])

print(result)
