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
  * в файле diplom.py указать id пользователя, тип альбома, количество фото и исполнить код

* Результат работы:
  - фотографии лежат в папке вида "Имя_Фамилия" на YaDisk
  - результат в json-формате в файле vk.json
  - файл журнала в виде "datetime.log" создается в корне каждый раз при запуске программы
