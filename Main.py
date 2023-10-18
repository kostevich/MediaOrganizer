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


def MovingMediaFiles():
    NameMediaFiles = dict()
    NameFolders = list()
    for UnitContent in Content:
        if os.path.isdir(f'C:/Data storage/Photos/From phone/{UnitContent}'):
            NameFolders.append(UnitContent)
            print(NameFolders)
        if UnitContent.endswith('jpg') or UnitContent.endswith('mp4'):
            BreakdownUnitContent = UnitContent.split('.')
            NameDataMediaFiles = BreakdownUnitContent[0]
            SuffixesMediaFiles = BreakdownUnitContent[1]
            NameMediaFiles[NameDataMediaFiles]= SuffixesMediaFiles
            for NameFile in NameMediaFiles.keys():
                if NameFile in NameFolders:
                    print(f"{NameMediaFiles.keys}{NameMediaFiles.values}", f"{NameMediaFiles.keys}/{NameMediaFiles.keys}{NameMediaFiles.values}")
                    os.replace(f"{NameMediaFiles.keys}{NameMediaFiles.values}", f"{NameMediaFiles.keys}/{NameMediaFiles.keys}{NameMediaFiles.values}")
        


CreateNewFolder()
MovingMediaFiles()
