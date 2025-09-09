from typing import List

from tarea import Tarea
from usuario import Usuario


class GestorTarea():

  def __init__(self):
    self.usuarios: List[Usuario] = []
    self.tareas: List[Tarea] = []

  def agregarUsuario(self, nombre, correo, telefono):
    usuario = Usuario(nombre, correo, telefono)
    self.usuarios.append(usuario)
    return usuario

  def actualizarUsuario(self, id, nombre, correo, telefono):
    for usuario in self.usuarios:
      if usuario.id == id:
        usuario.nombre = nombre
        usuario.corre = correo
        usuario.telefono = telefono
        return usuario
    return None

  def buscarUsuario(self, nombre: str):
    return next((u for u in self.usuarios if u.nombre == nombre), None)
