import uuid


class Usuario:

  def __init__(self, nombre: str, correo, telefono: int):
    self.id = uuid.uuid4()
    self.nombre = nombre
    self.corre = correo
    self.telefono = telefono

  def actualizarUsuario(self, nombre, correo, telefono):
    self.nombre = nombre
    self.corre = correo
    self.telefono = telefono

  def __str__(self):
    return f"ID: {self.id}.\nNombre: {self.nombre}. \nTelefono: {self.telefono}"

