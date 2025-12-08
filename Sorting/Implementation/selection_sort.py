
# Selection Sort: 

def selection_sort(arr:list)->list:
    for i in range(len(arr)-1): # To pass the entire array
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i] # For each ouer loop, only one swapping happens unlike bubble sort

    return arr

result=selection_sort([5,63,4,78,3,0,34,1])

print(result)
