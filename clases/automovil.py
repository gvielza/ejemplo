

from clases.vehiculo import Vehiculo


class Automovil(Vehiculo): #clase Automovil
  ruedas=4 #atributos de la clase
  def __init__(self,color, marca, aceleracion, velocidad):
    self.color=color
    self.marca=marca
    self.aceleracion=aceleracion
    self.velocidad=velocidad
  #Crear método acelera que aumentará la velocidad + aceleracion
  def acelera(self):
    self.velocidad=self.velocidad+self.aceleracion
  #método frena
  def frena(self):
    self.velocidad=self.velocidad-self.aceleracion
  #metodo que devuelve los datos para Automovil
  def datos(self):
    return f" Este es un vehículo de Tipo Automovil y tiene {self.ruedas}"

coche=Automovil("amarillo", "Audi", 50, 50)

print(coche.ruedas)
print(coche.aceleracion)


#coche.aceleracion=30
print(coche.aceleracion)

print( f"la velocidad es de {coche.aceleracion}")
coche.acelera()
print(f"La velocidad luego de acelerar es de {coche.velocidad}")
coche.frena()
print(coche.velocidad)







  
