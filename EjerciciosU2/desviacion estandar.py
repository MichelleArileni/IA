import math
arr = [13,14,15,15,15,16,17,18,20]
media = 0;
for i in arr:
    media+=i
media/=len(arr)
s=0;
n=len(arr)
for i in arr:
    s+= ((i-media)*(i-media))/(n-1)
print ("Desviación estandar:")
print (math.sqrt(s))
