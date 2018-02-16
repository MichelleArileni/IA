arr = [9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]
arr.sort()
print("Mediana: ")
if len(arr)%2!=0:
    print (arr[len(arr)//2])
else:
    a = arr[len(arr)//2]
    b = arr[len(arr)//2-1]
    print((a+b)/2)
 
