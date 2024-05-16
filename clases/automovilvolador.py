
from clases.automovil import Automovil


class AutomovilVolador(Automovil):
  ruedas=6
  def __init__(self, color, marca, aceleracion, velocidad, esta_volando=True):
    super().__init__(color,marca,aceleracion,velocidad)
    self.esta_volando=esta_volando
  def vuela(self):
    self.esta_volando=True
  def frena(self):
    self.esta_volando=False
  def datos(self):
    return f" Este vehículo es de tipo Automovil Volador y tiene {self.ruedas}"
    
automovilVoladors=AutomovilVolador("verde","Audi",50,50)
print(automovilVoladors.ruedas)



