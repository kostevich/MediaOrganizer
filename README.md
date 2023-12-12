# MediaOrganizer 
**MediaOrganizer** – скрипт на python, который организует фото и видео по отдельным папкам на каждый день.

# Порядок установки и использования
1. Загрузить репозиторий. Распаковать. 
2. Установить [Python](https://www.python.org/downloads/) версии не старше 3.11. Рекомендуется добавить в PATH.
3. В среду исполнения установить следующие пакеты: [dublib](https://github.com/DUB1401/dublib).
```
pip install git+https://github.com/DUB1401/dublib
```
Либо установить сразу все пакеты при помощи следующей команды, выполненной из директории скрипта.
```
pip install -r requirements.txt
```
4. Настроить скрипт путём редактирования [_Settings.json_](#Settings).
5. Запустить файл _main.py_.
```
python main.py
```
6. Проверить результат выполнения скрипта.

# Settings.json

<a name="Settings"></a> 

```JSON
"PATH": ""
```
Сюда необходимо занести путь к папке, где содержаться медиафайлы.

# Пример работы
**Папка, требующая реорганизации:**

![image](https://github.com/kostevich/RegistrationFromApp/assets/109979502/a854ec74-d0a5-4f44-9980-f16717a994c7)

**Результат работы скрипта:**

![image](https://github.com/kostevich/RegistrationFromApp/assets/109979502/98d634fa-6f54-418d-b562-fe081a18a125)

_Copyright © Kostevich Irina. 2023._
