arr = [11,2,5,8,9,15,5]
n = len(arr)
def Selectionsort (arr):
    for i in range(0, n-1):
        smallvalindex = i
        for j in range(i+1, n):
            if arr[j] < arr[smallvalindex]:
                smallvalindex = j
        arr[i],arr[smallvalindex] = arr[smallvalindex],arr[i]

Selectionsort(arr)
print(arr)