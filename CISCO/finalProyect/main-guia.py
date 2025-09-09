import uuid
from datetime import datetime, timedelta
from typing import List, Optional


# -------------------------
# MODELOS
# -------------------------
class Usuario:
    def __init__(self, nombre: str):
        self.id = str(uuid.uuid4())
        self.nombre = nombre

    def __repr__(self):
        return f"{self.nombre} (ID: {self.id[:8]})"


class Tarea:
    ESTADOS = ["pendiente", "en progreso", "completada"]

    def __init__(self, titulo: str, descripcion: str, fecha_limite: datetime, responsable: Usuario):
        self.id = str(uuid.uuid4())
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_creacion = datetime.now()
        self.fecha_limite = fecha_limite
        self.estado = "pendiente"
        self.responsable = responsable

    def actualizar_estado(self, nuevo_estado: str):
        if nuevo_estado in Tarea.ESTADOS:
            self.estado = nuevo_estado
        else:
            raise ValueError("Estado no válido.")

    def dias_para_vencimiento(self) -> int:
        return (self.fecha_limite - self.fecha_creacion).days

    def __repr__(self):
        return f"[{self.estado}] {self.titulo} (Resp: {self.responsable.nombre}, vence: {self.fecha_limite.date()})"


# -------------------------
# GESTOR DEL SISTEMA
# -------------------------
class GestorTareas:
    def __init__(self):
        self.usuarios: List[Usuario] = []
        self.tareas: List[Tarea] = []

    def agregar_usuario(self, nombre: str) -> Usuario:
        usuario = Usuario(nombre)
        self.usuarios.append(usuario)
        return usuario

    def buscar_usuario(self, nombre: str) -> Optional[Usuario]:
        return next((u for u in self.usuarios if u.nombre == nombre), None)

    def agregar_tarea(self, titulo: str, descripcion: str, fecha_limite: datetime, responsable: Usuario) -> Tarea:
        tarea = Tarea(titulo, descripcion, fecha_limite, responsable)
        self.tareas.append(tarea)
        return tarea

    def buscar_tarea(self, titulo: str) -> Optional[Tarea]:
        return next((t for t in self.tareas if t.titulo == titulo), None)

    def filtrar_tareas(self, estado=None, usuario=None, fecha_limite=None) -> List[Tarea]:
        resultado = self.tareas
        if estado:
            resultado = [t for t in resultado if t.estado == estado]
        if usuario:
            resultado = [t for t in resultado if t.responsable == usuario]
        if fecha_limite:
            resultado = [t for t in resultado if t.fecha_limite.date() == fecha_limite.date()]
        return resultado

    def informe_pendientes(self) -> List[Tarea]:
        return [t for t in self.tareas if t.estado == "pendiente"]

    def informe_completadas(self) -> List[Tarea]:
        return [t for t in self.tareas if t.estado == "completada"]

    def informe_por_usuario(self, usuario: Usuario) -> List[Tarea]:
        return [t for t in self.tareas if t.responsable == usuario]

    def resumen_tiempos(self) -> List[str]:
        return [f"Tarea '{t.titulo}': {t.dias_para_vencimiento()} días de margen"
                for t in self.tareas]


# -------------------------
# MENÚ BUILDER
# -------------------------
class Menu:
    def __init__(self, titulo: str, prompt: str = "Seleccione una opción:"):
        self.titulo = titulo
        self.prompt = prompt
        self.items = []
        self.exit_label = "Salir"

    def add_item(self, label: str, action=None, submenu=None):
        self.items.append((label, action, submenu))

    def show(self):
        while True:
            print("\n" + "=" * len(self.titulo))
            print(self.titulo)
            print("=" * len(self.titulo))

            for i, (label, _, _) in enumerate(self.items, start=1):
                print(f"{i}. {label}")
            print(f"0. {self.exit_label}")

            choice = input(self.prompt + " ").strip()
            if not choice.isdigit():
                print("Ingrese un número válido.")
                continue

            idx = int(choice)
            if idx == 0:
                break
            if 1 <= idx <= len(self.items):
                _, action, submenu = self.items[idx - 1]
                if submenu:
                    submenu.show()
                elif action:
                    try:
                        action()
                    except Exception as e:
                        print(f"Error: {e}")
            else:
                print("Opción no válida.")


# -------------------------
# APLICACIÓN
# -------------------------
def main():
    gestor = GestorTareas()

    # Acciones
    def crear_usuario():
        nombre = input("Nombre de usuario: ")
        u = gestor.agregar_usuario(nombre)
        print(f"Usuario creado: {u}")

    def listar_usuarios():
        if not gestor.usuarios:
            print("No hay usuarios.")
        for u in gestor.usuarios:
            print(u)

    def crear_tarea():
        if not gestor.usuarios:
            print("Primero debe crear un usuario.")
            return
        titulo = input("Título de la tarea: ")
        desc = input("Descripción: ")
        dias = int(input("Días hasta el vencimiento: "))
        responsable = gestor.usuarios[int(input("Seleccione usuario (índice): "))]
        fecha_limite = datetime.now() + timedelta(days=dias)
        t = gestor.agregar_tarea(titulo, desc, fecha_limite, responsable)
        print(f"Tarea creada: {t}")

    def listar_tareas():
        if not gestor.tareas:
            print("No hay tareas.")
        for t in gestor.tareas:
            print(t)

    def cambiar_estado():
        listar_tareas()
        titulo = input("Título de la tarea a modificar: ")
        tarea = gestor.buscar_tarea(titulo)
        if not tarea:
            print("Tarea no encontrada.")
            return
        print("Estados posibles:", Tarea.ESTADOS)
        nuevo = input("Nuevo estado: ")
        tarea.actualizar_estado(nuevo)
        print("Estado actualizado.")

    def informes():
        print("\n--- Tareas pendientes ---")
        print(gestor.informe_pendientes())
        print("\n--- Tareas completadas ---")
        print(gestor.informe_completadas())
        print("\n--- Resumen tiempos ---")
        for linea in gestor.resumen_tiempos():
            print(linea)

    # Menús
    menu_usuarios = Menu("Gestión de Usuarios")
    menu_usuarios.add_item("Crear usuario", crear_usuario)
    menu_usuarios.add_item("Listar usuarios", listar_usuarios)

    menu_tareas = Menu("Gestión de Tareas")
    menu_tareas.add_item("Crear tarea", crear_tarea)
    menu_tareas.add_item("Listar tareas", listar_tareas)
    menu_tareas.add_item("Cambiar estado", cambiar_estado)

    menu_principal = Menu("Gestor de Tareas")
    menu_principal.add_item("Usuarios", submenu=menu_usuarios)
    menu_principal.add_item("Tareas", submenu=menu_tareas)
    menu_principal.add_item("Generar informes", informes)

    menu_principal.show()
    print("Saliendo del sistema...")


if __name__ == "__main__":
    main()
