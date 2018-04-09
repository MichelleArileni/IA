import matplotlib.pyplot as mat
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import numpy as num

iris = datasets.load_iris()

especies = iris.target_names
caracteristicas = iris.data

mat.figure(1)
mat.scatter(0.1*num.random.randn(49,1),caracteristicas[0:49,2])
mat.scatter(1+0.1*num.random.randn(49,1),caracteristicas[50:99,2])
mat.scatter(2+0.1*num.random.randn(49,1),caracteristicas[100:149,2])
mat.ylabel('Longitud de Pétalo (cm)')
mat.show()

mat.figure(2)
mat.scatter(0.1*num.random.randn(49,1),caracteristicas[0:49,3])
mat.scatter(1+0.1*num.random.randn(49,1),caracteristicas[50:99,3])
mat.scatter(2+0.1*num.random.randn(49,1),caracteristicas[100:149,3])
mat.ylabel('Anchura de Pétalo (cm)')
mat.show()

mat.figure(3)
mat.scatter(0.1*num.random.randn(49,1),caracteristicas[0:49,0])
mat.scatter(1+0.1*num.random.randn(49,1),caracteristicas[50:99,0])
mat.scatter(2+0.1*num.random.randn(49,1),caracteristicas[100:149,0])
mat.ylabel('Longitud de Sépalo (cm)')
mat.show()

mat.figure(4)
mat.scatter(0.1*num.random.randn(49,1),caracteristicas[0:49,1])
mat.scatter(1+0.1*num.random.randn(49,1),caracteristicas[50:99,1])
mat.scatter(2+0.1*num.random.randn(49,1),caracteristicas[100:149,1])
mat.ylabel('Anchura de Sépalo (cm)')
mat.show()

#Longitud de pétalo y anchura de pétalo. Aparentemente es la mejor relación
mat.figure(5)
mat.scatter(caracteristicas[0:49,2],caracteristicas[0:49,3])
mat.scatter(caracteristicas[50:99,2],caracteristicas[50:99,3])
mat.scatter(caracteristicas[100:149,2],caracteristicas[100:149,3])
mat.xlabel('Longitud de Pétalo (cm)')
mat.ylabel('Anchura de Pétalo (cm)')
mat.show()

#tablas generadas para hacer pruebas, seleccionadas aleatoriamente
mat.figure(6)
mat.scatter(caracteristicas[0:49,0],caracteristicas[0:49,1])
mat.scatter(caracteristicas[50:99,0],caracteristicas[50:99,1])
mat.scatter(caracteristicas[100:149,0],caracteristicas[100:149,1])
mat.xlabel('Longitud de Sépalo (cm)')
mat.ylabel('Anchura de Sépalo (cm)')
mat.show()

mat.figure(7)
mat.scatter(caracteristicas[0:49,2],caracteristicas[0:49,0])
mat.scatter(caracteristicas[50:99,2],caracteristicas[50:99,0])
mat.scatter(caracteristicas[100:149,2],caracteristicas[100:149,0])
mat.xlabel('Longitud de Pétalo (cm)')
mat.ylabel('Longitud de Sépalo (cm)')
mat.show()

mat.figure(8)
mat.scatter(caracteristicas[0:49,3],caracteristicas[0:49,1])
mat.scatter(caracteristicas[50:99,3],caracteristicas[50:99,1])
mat.scatter(caracteristicas[100:149,3],caracteristicas[100:149,1])
mat.xlabel('Anchura de Pétalo (cm)')
mat.ylabel('Anchura de Sépalo (cm)')
mat.show()
