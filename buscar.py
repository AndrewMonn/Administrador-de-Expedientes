from pathlib import Path
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
from PySide6.QtCore import Qt


p = Path('.')

extensiones = ['.docx']


# Funcion para buscar archivos

def buscar_Archivo(extension, CI, txt_Ubicacion):

    found = False

    for ext in extension:

        for archivo in p.glob('**/*' + ext):

            #Verifica si el archivo existe

            if archivo.stem == CI:

                found = True

                ruta_archivo = p / archivo                

                if ruta_archivo.is_file():
                    
                    ruta = Path(archivo)
                    
                    msg = QMessageBox()
                    msg.setWindowTitle("Operación Exitosa")
                    msg.setText(f'El expediente ha sido encontrado. ¿Desea abrir el expediente: {archivo}?')
                    msg.setFixedSize(200, 150)
                    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    
                    #Se imprime la ubicacion donde se ubica el archivo CI
                    
                    txt_Ubicacion.setPlainText(str(ruta.cwd()) + str('\\') + str(ruta))

                
                
                    # msg.exec() devuelve la constante del botón que ha pulsado el usuario
                    resultado = msg.exec()

                    # Comprobamos qué botón ha pulsado el usuario
                    if resultado == QMessageBox.Yes:
                        # Si el usuario ha pulsado "Sí", procedemos a abrir el archivo

                        msg = QMessageBox()
                        msg.setWindowTitle("")
                        msg.setText("El expediente será abierto.")
                        msg.setFixedSize(200, 150)
                        msg.exec()

                        os.startfile(str(archivo))

                    elif resultado == QMessageBox.No:
                        # Si el usuario ha pulsado "No", no abriremos el archivo
                        print('No se abrira el archivo')
                    break
                
    #En caso de no existir el archivo, mandara un mensaje de error
    
    if not found:

        msg = QMessageBox()
        msg.setWindowTitle("Operación Fallida")
        msg.setText("El expediente no existe")
        msg.setFixedSize(200, 150)
        msg.exec()
                    

# [ !!--

#   Aplicación de productividad creada por Andres Luna - Desarrollador Front-End. 

#   Redes y Contacto:

#     LinkedIn: https://www.linkedin.com/in/andrewmonn/
#     Github: https://github.com/AndrewMonn/
#     Email: andreslunacas2000@gmail.com

# --!! ]