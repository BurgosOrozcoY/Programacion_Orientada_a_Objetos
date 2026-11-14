from estudiantes import estudiantes
from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de Estudiantes")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0)
        self.main()

    def borrarPantalla(self):
        for witget in self.ventana.winfo_children():
            witget.destroy()

    def menu_acciones(self):
        self.borrarPantalla()
        tipo = "Estudiantes"
        Label(self.ventana, text = f"\n...::: Menu de {tipo} :::...").pack(pady=10)
        Button(self.ventana, text = "1.- Agregar", command = self.insertar_view).pack(pady=5)
        Button(self.ventana, text = "2.- Borrar", command = self.eliminar_view).pack(pady=5)
        Button(self.ventana, text = "3.- Modificar", command = self.modificar_view).pack(pady=5)
        Button(self.ventana, text = "4.- Mostrar", command = self.consultar_view).pack(pady=5)
        Button(self.ventana, text = "5.- Regresar", command = self.main).pack(pady=5)

    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "...Ingresar los datos del estudiante...").pack(pady = 10)
        Label(self.ventana, text = "Nombre:").pack(pady = 5)
        self.nombre = Entry(self.ventana)
        self.nombre.focus()
        self.nombre.pack(pady = 5)
        Label(self.ventana, text = "Nota:").pack(pady = 5)
        self.nota = Entry(self.ventana)
        self.nota.pack(pady = 5)
        Button(self.ventana, text = "Guardar", command = self.insertar_controller).pack(pady = 10)
        Button(self.ventana, text = "Regresar", command = self.menu_acciones).pack(pady = 5)

    def eliminar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "...Ingresar el ID del estudiante a eliminar...").pack(pady = 10)
        Label(self.ventana, text = "ID:").pack(pady = 5)
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady = 5)
        Button(self.ventana, text = "Guardar", command = self.eliminar_controller).pack(pady = 10)
        Button(self.ventana, text = "Regresar", command = self.menu_acciones).pack(pady = 5)

    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "...Ingresar el ID del estudiante a modificar...").pack(pady = 10)
        Label(self.ventana, text = "ID:").pack(pady = 5)
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady = 5)

        Label(self.ventana, text = "Nuevo nombre:").pack(pady = 5)
        self.nombre = Entry(self.ventana)
        self.nombre.pack(pady = 5)
        Label(self.ventana, text = "Nueva nota:").pack(pady = 5)
        self.nota = Entry(self.ventana)
        self.nota.pack(pady = 5)
        Button(self.ventana, text = "Guardar", command = self.modificar_controller).pack(pady = 10)
        Button(self.ventana, text = "Regresar", command = self.menu_acciones).pack(pady = 5)

    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Consultar los estudiantes...").pack(pady=10)
        filas = ""
        filas = self.consultar_controller(filas)
        Label(self.ventana, text=f"{'No.':<20}{'ID':<20}{'Nombre':<20}{'Nota':<20}").pack(pady=5)
        Label(self.ventana, text=f"{"-"*100}").pack(pady=5)
        Label(self.ventana, text=f"{filas}").pack(pady=5)
        Label(self.ventana, text=f"{"-"*100}").pack(pady=5)
        Button(self.ventana, text= "Regresar", command= self.menu_acciones).pack(pady=5)

    #   CONTROLADOR del SISTEMA
    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="... Exitoso ...", message="...Accion realizada con exito...")
        else:
            messagebox.showerror(title="... Verifica por favor ...", message="...Esta accion no puede realizarse...")

    def insertar_controller(self):
        estudiante1=estudiantes.Estudiantes(self.nombre.get(), self.nota.get())
        respuesta = estudiante1.insertar()
        self.respuesta_sql(respuesta)

    def eliminar_controller(self):
        id = self.id.get()
        respuesta = estudiantes.Estudiantes.eliminar(id)
        self.respuesta_sql(respuesta)

    def consultar_controller(self, filas):
        registros = estudiantes.Estudiantes.consultar()
        if len(registros) > 0:
            num_estudiantes = 1
            for fila in registros:
                 filas = filas + (f"{num_estudiantes:<20}{fila[0]:<20}{fila[1]:<20}{fila[2]:<20}")
                 num_estudiantes += 1
        else:
            filas = ("\n\n\t NO existen datos que mostrar por el momento")
        return filas

    def modificar_controller(self):
        id = self.id.get()
        estudiante1=estudiantes.Estudiantes(self.nombre.get(), self.nota.get())
        respuesta = estudiante1.actualizar(id)
        self.respuesta_sql(respuesta)
        del estudiante1

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text = "\n...::: M E N U  P R I N C I P A L :::...").pack(pady=10)
        Button(self.ventana, text = "1.- Coches", command = self.menu_acciones).pack(pady=5)
        Button(self.ventana, text = "2.- Salir", command = self.ventana.quit).pack(pady=5)


if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()