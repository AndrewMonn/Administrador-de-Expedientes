from pathlib import Path
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
from PySide6.QtCore import Qt


p = Path('.')

extensiones = ['.docx']

plantilla_docx = Path('./plantilla/plantilla.docx')


# Funcion para Borrar archivos

def borrar_Archivo(extension, CI, txt_Ubicacion):
    
    found = False

    for ext in extension:

        for archivo in p.glob('**/*' + ext):

            if archivo.stem == CI:
                found = True

                ruta_archivo = p / archivo
                
                if ruta_archivo.is_file():
                    
                    msg = QMessageBox()
                    msg.setWindowTitle("Precaución")
                    msg.setText(f'¿Está seguro que desea eliminar el expediente: {ruta_archivo}?')
                    msg.setFixedSize(200, 150)
                    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)


                    # msg.exec() devuelve la constante del botón que ha pulsado el usuario
                    resultado = msg.exec()

                    # Comprobamos qué botón ha pulsado el usuario
                    if resultado == QMessageBox.Yes:
                        # Si el usuario ha pulsado "Sí", procedemos a eliminar el ruta_archivo
                        os.remove(ruta_archivo)

                        msg = QMessageBox()
                        msg.setWindowTitle("Operación Exitosa")
                        msg.setText("El expediente ha sido eliminado exitosamente.")
                        msg.setFixedSize(200, 150)
                        msg.exec()

                        txt_Ubicacion.setPlainText('')
                        break
                    
                    
                    elif resultado == QMessageBox.No:
                        # Si el usuario ha pulsado "No", cancelamos la operación de eliminación

                        ruta = Path(ruta_archivo)

                        msg = QMessageBox()
                        msg.setWindowTitle("Operación Fallida")
                        msg.setText("La operación de eliminación ha sido cancelada.")
                        msg.setFixedSize(200, 150)
                        msg.exec()

                        txt_Ubicacion.setPlainText(str(ruta.cwd()) + str('\\') + str(ruta))

                        break

    if not found:
    
    
        msg = QMessageBox()
        msg.setWindowTitle("Operación Fallida")
        msg.setText(f"El expediente {CI}{ext} no existe")
        msg.setFixedSize(200, 150)
        msg.exec()