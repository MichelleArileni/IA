arr = [9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]
lista = []
for i in arr:
    if i not in lista:
        lista.append(i)
cont = 0;
n = lista[0]
for i in lista:
    a = arr.count(i)
    if a > cont:
        cont = a
        n = i
print ("Moda: ")
print (n)
    