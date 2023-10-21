#!/usr/bin/python
from dublib.Methods import CheckPythonMinimalVersion, ReadJSON
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout

import os 
import sys
#==========================================================================================#
# >>>>> ИНИЦИАЛИЗАЦИЯ СКРИПТА <<<<< #
#==========================================================================================#

# Проверка поддержки используемой версии Python.
CheckPythonMinimalVersion(3, 11)

#==========================================================================================#
# >>>>> ЧТЕНИЕ НАСТРОЕК <<<<< #
#==========================================================================================#

# Чтение настроек.
# Settings = ReadJSON("Settings.json")

#==========================================================================================#
# >>>>> ОБРАБОТКА ДАННЫХ <<<<< #
#==========================================================================================#


# Создадим приложение наследующее функции класса QWidget.
class Window(QWidget):
    # Конструктор приложения.
    def __init__(self):
        super().__init__()
        # Размер окна приложения.
        self.resize(900, 650)
        # Название приложения.
        self.setWindowTitle("MediaOrganizer")
        # Фон приложения.
        layout = QVBoxLayout()
        self.setLayout(layout)
       

        
# Создаем экземпляр класса.
app = QApplication(sys.argv)
# Создаем виджет.
window = Window()
# Открытие окна приложения.
window.show()
# Выход из приложения.
sys.exit(app.exec())


PATH = "C:/Data storage/Photos/From phone/"

# Перемещение медиафайлов в папки.
def MovingMediaFiles():
    # Содержимое выбранной папки.
    Content = os.listdir(PATH)
    for UnitContent in Content:
        # Выбор элементов папки заканчивающихся на jpg/mp4.
        if UnitContent.endswith('jpg') or UnitContent.endswith('mp4'):
            # Создание данных файла.
            FileData = ParseFile(UnitContent)
            # Если папки с названиемм файла не найдено, то создать ее.
            if os.path.exists(PATH + FileData["date"]) == False:
                os.makedirs(PATH + FileData["date"])
            # Перемещение файла в папку. 
            os.replace(PATH + UnitContent, PATH + FileData["date"] + "/" + UnitContent)
   
              

# Хранение данных о файле.
def ParseFile(Filename: str)->dict:
    # Словарь с данными файла.
    Result = {
        'filename': None,
        "extension": Filename.split(".")[-1],
        "date": None,
        "time": None
    }
    # Получение данных для словаря.
    Result['filename'] = Filename.replace("." + Result['extension'], "")
    Result['date'] =  Result['filename'].split("_")[1]
    Result['time'] =  Result['filename'].split("_")[2]
    return Result


MovingMediaFiles()
