import sqlite3

class Conexion:
  def __init__(self, nombre_bd):
    self.conexion=sqlite3.connect(nombre_bd)
    self.cursor=self.conexion.cursor()
  def crear_tabla_vehiculos(self):
    self.cursor.execute('''CREATE TABLE IF NOT EXISTS vehiculo(id INTEGER PRIMARY KEY AUTOINCREMENT,
    anno INTEGER,
    modelo TEXT)''')
    self.conexion.commit()
  def insertar_vehiculo(self,vehiculo):
    self.cursor.execute('''INSERT INTO vehiculo(anno,modelo) VALUES (?,?)''',
       (vehiculo.get_anno(),
       vehiculo.get_modelo()))
    self.conexion.commit()
    
  def obtener_vehiculos(self):
    vehiculos=self.cursor.execute('''SELECT * FROM vehiculo''')
    return vehiculos

  def eliminar_vehiculo(self,id):
    self.cursor.execute('''DELETE FROM vehiculo WHERE id=?''',(id,))
    self.conexion.commit()
    
  def editar_vehiculo(self,id):
    self.cursor.execute('''UPDATE vehiculo SET anno=?,modelo=? WHERE id=?''',(id,))
    self.conexion.commit()




  def cerrar_conexion(self):
    self.cursor.close()
    self.conexion.close()



 