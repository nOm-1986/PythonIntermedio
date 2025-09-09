from datetime import datetime, timedelta
from typing import List, Optional

from usuario import Usuario


class Tarea:
  ESTADOS = ["pendiente", "en progreso", "completada"]

  def __init__(self, id: int, titulo: str, descripcion: str, fecha_limite:datetime, responsable: Usuario, estado='pendiente'):
    self.id = id
    self.titulo = titulo
    self.descripcion = descripcion
    self.fecha_creacion = datetime.now()
    self.fecha_limite = fecha_limite
    self.id_responsable = responsable
    self.estado = estado

  def actualizarEstado(self, nuevo_estado: str):
    if nuevo_estado in Tarea.ESTADOS:
      self.estado = nuevo_estado
    else:
      raise ValueError("Estado no válido")

  def diasParaVencimiento(self):
    return(self.fecha_limite - self.fecha_creacion).days

  def __str__(self):
    return f"Estado de la tarea: [{self.estado}]. \n Titulo: {self.titulo}. \n Responsable: {self.responsable.nombre}, vence: {self.fecha_limite.date()}. \n Días para vencimiento: {self.diasParaVencimiento()}"
