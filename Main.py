import os

# Содержимое выбранной папки.
Content = os.listdir("C:/Data storage/Photos/From phone")

# Создание новой папки.
def CreateNewFolder():

    for UnitContent in Content:
        # Выбор элементов папки заканчивающихся на jpg/mp4.
        if UnitContent.endswith('jpg') or UnitContent.endswith('mp4'):
            # Разделение названия медиафайла по _.
            BreakdownUnitContent = UnitContent.split('_')
            # Выбор части названия с датой.
            NameNewFolder = BreakdownUnitContent[1]
            # Создание папки, если таковой не имеется.
            if not os.path.exists(f'C:/Data storage/Photos/From phone/{NameNewFolder}'):
                os.makedirs(f'C:/Data storage/Photos/From phone/{NameNewFolder}')

CreateNewFolder()

