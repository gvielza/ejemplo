'''1-Separar clases en archivos independientes en carpeta clases e importar desde archivo main
2-Crear clase Vehiculo con año(protegido) y modelo(privado)
3-Reestructurar el ejercicio de la clase anterior para que hereden de la clase Vehiculo
4-Importar clase desde main crear un Vehículo y mostrar sus atributos de manera separada
5-Realizar get y set
6-Mostrar por consola año y modelo, modificarlos y mostrar nuevamente
7-Subir cambios al git y versión v1 (clase 8)'''
import sqlite3
from clases.automovil import Automovil
from clases.automovilvolador import AutomovilVolador
from clases.vehiculo import Vehiculo
from base_datos.conexion import Conexion
vehiculo1=Vehiculo(2020,"A4")
print(vehiculo1._anno)
vehiculo1._anno=2022

print(vehiculo1._anno)

print(vehiculo1.get_modelo())
vehiculo1.set_modelo('A3')
print(vehiculo1.get_modelo())


from clases.automovil import Automovil


print("*************Polimorfismo**************")
def datos_vehiculo(auto):
  return auto.datos()
auto_ej=Automovil("verde", "Ford", 20,40)
print(datos_vehiculo(auto=auto_ej))
auto_v=AutomovilVolador("azul", "Audi", 50,50)
print(datos_vehiculo(auto=auto_v))

print("*******conectar a la bd ******* ")
#conexion=sqlite3.connect("base_datos/datos.db")
conexion=Conexion(nombre_bd="base_datos/datos.db")
#cursor=conexion.cursor()
conexion.crear_tabla_vehiculos()

vehiculo=Vehiculo(2023,"K4")

#conexion.insertar_vehiculo(vehiculo=vehiculo)

vehiculos=conexion.obtener_vehiculos()
for vehiculo in vehiculos:
  print(vehiculo)

conexion.eliminar_vehiculo(3)
print("modificando bd")
vehiculos=conexion.obtener_vehiculos()
for vehiculo in vehiculos:
  print(vehiculo)

conexion.cerrar_conexion()
