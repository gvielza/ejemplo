##Crear clase Vehiculo con año(protegido) y modelo(privado)
class Vehiculo:
  def __init__(self,anno, modelo):
    self._anno=anno
    self.__modelo=modelo

  def get_anno(self):
    return self._anno

  def set_anno(self,nuevo_anno):
    self._anno=nuevo_anno
    
  def get_modelo(self):
    return self.__modelo
          
  def set_modelo(self,nuevo_modelo):
    self.__modelo=nuevo_modelo



 