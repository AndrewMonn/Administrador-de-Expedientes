from pathlib import Path
import os
import shutil

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
from PySide6.QtCore import Qt


p = Path('.')

extensiones = ['.docx']

plantilla_docx = Path('./plantilla/plantilla.docx')

fecha = ''


# Funcion para crear nuevos archivos con su respectiva carpeta

def crear_Archivo(extension, CI, fecha, plantilla, txt_Ubicacion):
    
    for ext in extension:

        for archivo in p.glob('**/*' + ext):

            directorio_nuevo = (p / fecha)
            
            archivo_nuevo_r = Path(directorio_nuevo / str(CI + ext))
    
            #Validacion para evitar que se creen archivos fuera de su carpeta de fecha
            
            if not fecha == '':
                
                #Comprobación de que no existe un archivo con el mismo numero de registro
                
                if not CI == archivo.stem:

                    #En caso de que no exista una carpeta con la fecha proporcionada, se creara una, y en caso de que si exista, se saltara al siguiente paso y solo copiara el archivo "plantilla.docx" en la carpeta correspondiente y lo renombrara al valor de la variable CI

                    if not ( p / fecha).is_dir():

                        (p / fecha).mkdir()

                    elif ( p / fecha).is_dir():

                        ruta = Path(archivo)

                        shutil.copy(plantilla, directorio_nuevo)
                        archivo_nuevo = Path(directorio_nuevo / 'plantilla.docx')
                        archivo_nuevo_r = archivo_nuevo.replace(directorio_nuevo / str(CI + ext))

                        msg = QMessageBox()
                        msg.setWindowTitle("Operación Exitosa")
                        msg.setText("El expediente ha sido creado exitosamente.")
                        msg.setFixedSize(200, 150)
                        msg.exec()

                        #Se imprime la ubicacion donde se ubica el archivo CI

                        txt_Ubicacion.setPlainText(str(ruta.cwd()) + str('\\') + str(fecha) + str('\\') + str(CI) + str(ext))

                        msg = QMessageBox()
                        msg.setWindowTitle("Precaución")
                        msg.setText(f'¿Desea abrir el expediente: {CI}{ext}?')
                        msg.setFixedSize(200, 150)
                        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)


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

                            os.startfile(str(archivo_nuevo_r))

                            break

                        elif resultado == QMessageBox.No:
                            
                            # Si el usuario ha pulsado "No", no abriremos el archivo
                            
                            print('No se abrira el archivo')
                            break

                #En caso de que si exista un archivo con el nombre del valor de la variable CI, alertara de esto y no creara uno nuevo
                
                elif CI == archivo.stem and archivo.is_file():

                    ruta = Path(archivo)

                    msg = QMessageBox()
                    msg.setWindowTitle("Operación Fallida")
                    msg.setText("El expediente ya existe.")
                    msg.setFixedSize(200, 150)
                    msg.exec()
                    
                    #Se imprime la ubicacion donde se ubica el archivo CI
                    
                    txt_Ubicacion.setPlainText(str(ruta.cwd()) + str('\\') + str(fecha) + str('\\') + str(CI) + str(ext))

                    msg = QMessageBox()
                    msg.setWindowTitle("")
                    msg.setText(f'¿Desea abrir el expediente: {archivo.stem}{ext}?')
                    msg.setFixedSize(200, 150)
                    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)


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

                        os.startfile(str(archivo_nuevo_r))

                    elif resultado == QMessageBox.No:
                        # Si el usuario ha pulsado "No", no abriremos el archivo
                        print('No se abrira el archivo')

                    break
                
            #Alerta en caso de no ingresar la fecha para la creacion de la carpeta o ubicacion del archivoen carpeta existente 
                
            elif fecha == '' :
                
                msg = QMessageBox()
                msg.setWindowTitle("Operación Fallida")
                msg.setText("Debe ingresar la fecha del expediente.")
                msg.setFixedSize(200, 150)
                msg.exec()
                break