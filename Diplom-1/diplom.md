!['python'](https://yandex.ru/images/search?pos=2&from=tabbar&img_url=https%3A%2F%2Fblog.hyperiondev.com%2Fwp-content%2Fuploads%2F2017%2F11%2FPython_logo.jpg&isize=small&text=Python&rpt=simage)

# Дипломный проект «Резервное копирование» первого блока «Основы языка программирования Python»

## Задание:

- Нужно написать программу, которая будет:

  - Получать фотографии с профиля. Для этого нужно использовать метод photos.get.
  - Сохранять фотографии максимального размера(ширина/высота в пикселях) на Я.Диске.
  - Для имени фотографий использовать количество лайков, если количество лайков одинаково,
    то добавить дату загрузки.
  - Сохранять информацию по фотографиям в json-файл с результатами.

## Входные данные:

- Пользователь вводит:

  - id пользователя vk;
  - токен с Полигона Яндекс.Диска. Важно: Токен публиковать в github не нужно!

* Как пользоваться:

  - в файл token.txt положить токен VK.com

  * в файл ya_token положить токен YaDisk
  * в файле diplom.py указать id пользователя и количество фото и исполнить код

* Результат работы:
  - фотографии лежат в папке вида "Имя_Фамилия" на YaDisk
  - результат в json-формате в файле vk.json
  - debug.log - журнал