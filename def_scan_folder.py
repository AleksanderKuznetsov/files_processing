"""
Программа для получения папок и файлов верхнего уровня каталога.
"""

import os.path


def scan_top_level(path=os.getcwd()) -> list:
    """
    :param path: путь
    :return: массив с двумя массивами: папки и файлы отдельно
    """
    mass_file = []
    mass_dir = []
    mass = os.listdir(path)  # Получаем содержимое папки.
    for i, mas in enumerate(mass):  # Проходим циклом по содержимому
        join_path = os.path.abspath(mas)
        if os.path.isdir(join_path):
            mass_dir.append(mas)  # Добавим в массив каталоги.
        elif os.path.isfile(join_path):
            mass_file.append(mas)  # Добавим в массив файлы.
    return [mass_dir, mass_file]
