'''1-Separar clases en archivos independientes en carpeta clases e importar desde archivo main
2-Crear clase Vehiculo con año(protegido) y modelo(privado)
3-Reestructurar el ejercicio de la clase anterior para que hereden de la clase Vehiculo
4-Importar clase desde main crear un Vehículo y mostrar sus atributos de manera separada
5-Realizar get y set
6-Mostrar por consola año y modelo, modificarlos y mostrar nuevamente
7-Subir cambios al git y versión v1 (clase 8)
'''
from clases.vehiculo import Vehiculo
vehiculo1=Vehiculo(2020,"A4")
print(vehiculo1._anno)
vehiculo1._anno=2022

print(vehiculo1._anno)

print(vehiculo1.get_modelo())
vehiculo1.set_modelo('A3')
print(vehiculo1.get_modelo())
