"""
Получаем ссылку для скачивания файла, которую "переваривает" Power BI в качестве
источника Web.Contents(). Шлюз при обновлении не нужен
"""
import os.path as os
import requests


def get_url_yadisk(token: str, file_url: str) -> str:
    """
    :param token: токен Яндекс.Диск API. Например 'EREEVEXXXXXXXSD474FF'.
           Если нет - получить под своим аккаунтом https://yandex.ru/dev/disk/poligon/
    :param file_url: ссылка на файл. Например 'https://disk.yandex.ru/i/MxeZNFh36Gxxxxx'
           ("Поделиться файлом" - на Яндекс.Диске)
    :return: возвращаем ссылку на файл
    """
    # В ссылке ставим limit=100000, т.к. по умолчанию идет limit=20.
    url = 'https://cloud-api.yandex.net/v1/disk/resources/files?limit=100000'
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Authorization': f'OAuth {token}'}
    # Меняем формат ссылки.
    public_url = os.join('https://yadi.sk/i/', os.basename(file_url))
    download_url = 0
    #  Получим данные.
    res = requests.get(f'{url}', headers=headers).json()
    # Заберем значения первого ключа (массив)
    array = res['items']

    for i, item in enumerate(array):
        keys = list(item.keys())
        for key in keys:
            if key == 'public_url' and item['public_url'] == public_url:
                download_url = item['file']
                break

    return download_url
