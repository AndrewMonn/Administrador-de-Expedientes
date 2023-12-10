
# Importamos los módulos necesarios
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
from PySide6.QtCore import Qt
from buscar import buscar_Archivo
from crear import crear_Archivo
from borrar import borrar_Archivo
from pathlib import Path
import os
import shutil

p = Path('.')

extensiones = ['.docx']

plantilla_docx = Path('./plantilla/plantilla.docx')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuramos la ventana principal
        self.setWindowTitle("Administrador de Expedientes")
        self.setFixedSize(450, 550)  # Tamaño fijo de la ventana
        self.setStyleSheet("font-family: 'Helvetica', 'Tahoma', 'Ubuntu Mono'; font-size: 14px; font-weight: 600; color: rgb(6, 40, 61)")  # Estilo general de la GUI

        # Creamos y configuramos los widgets
        self.title = QLabel("Administrador de Expedientes", self)
        self.title.setGeometry(65, 25, 291, 51)
        self.title.setStyleSheet("font-family: Tahoma; font-size: 18px; font-weight: 800")

        self.label_CI = QLabel("Número de Registro", self)
        self.label_CI.setGeometry(65, 100, 200, 16)

        self.inp_CI = QLineEdit(self)
        self.inp_CI.setPlaceholderText("ej: V-5892464")
        self.inp_CI.setGeometry(65, 130, 231, 21)
        self.inp_CI.setStyleSheet("border-radius: 4px")

        self.label_Fechas = QLabel("Fecha", self)
        self.label_Fechas.setGeometry(65, 190, 200, 16)

        self.inp_Fechas = QLineEdit(self)
        self.inp_Fechas.setPlaceholderText("ej: 23_11_1962")
        self.inp_Fechas.setGeometry(65, 220, 231, 21)
        self.inp_Fechas.setStyleSheet("border-radius: 4px")

        self.btn_Buscar = QPushButton("Buscar", self)
        self.btn_Buscar.setGeometry(65, 290, 75, 24)
        self.btn_Buscar.clicked.connect(lambda: buscar_Archivo(extensiones, self.inp_CI.text(), txt_Ubicacion))

        self.btn_Crear = QPushButton("Crear", self)
        self.btn_Crear.setGeometry(185, 290, 75, 24)
        self.btn_Crear.clicked.connect(lambda: crear_Archivo(extensiones, self.inp_CI.text(), self.inp_Fechas.text(), plantilla_docx, txt_Ubicacion))

        self.btn_Borrar = QPushButton("Borrar", self)
        self.btn_Borrar.setGeometry(310, 290, 75, 24)
        self.btn_Borrar.clicked.connect(lambda: borrar_Archivo(extensiones, self.inp_CI.text(), txt_Ubicacion))

        self.label_Ubicacion = QLabel("Ubicación del Archivo", self)
        self.label_Ubicacion.setGeometry(65, 360, 200, 16)

        self.txt_Ubicacion = QTextEdit(self)
        self.txt_Ubicacion.setGeometry(65, 390, 321, 120)
        self.txt_Ubicacion.setStyleSheet("border: none; font-family: 'Ubuntu Mono'; font-size: 16px; font-weight: 600")
        self.txt_Ubicacion.setReadOnly(True)
        
        txt_Ubicacion = self.txt_Ubicacion

      

# Creamos la aplicación y la ventana principal
app = QApplication([])
window = MainWindow()
window.show()

# Ejecutamos la aplicación
app.exec()


# [ !!--

#   Aplicación de productividad creada por Andres Luna - Desarrollador Front-End. 

#   Redes y Contacto:

#     LinkedIn: https://www.linkedin.com/in/andrewmonn/
#     Github: https://github.com/AndrewMonn/
#     Email: andreslunacas2000@gmail.com

# --!! ]