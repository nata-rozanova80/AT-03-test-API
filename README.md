# AT-03-test-API   
(Учебный проект для Zerocoder)
Мокирование и тестирование API

Задание
- Напишите функцию, которая делает запрос к TheCatAPI для получения случайного изображения кошки.

https://api.thecatapi.com/v1/images/search

- Напишите тест, который проверяет успешный запрос и возвращает правильный URL.

- Напишите тест, который проверяет неуспешный запрос (например, статус код 404) и возвращает `None`.

# Cat Image Fetcher

## Описание
Cat Image Fetcher — это простое приложение на Python, которое делает запрос к TheCatAPI для получения случайного изображения кошки. Приложение включает в себя функцию для получения изображения и тесты для проверки правильности работы функции.

## Установка

1. Убедитесь, что у вас установлен Python 3.
2. Установите необходимые библиотеки:

pip install requests


3. Сохраните код функции в файл, например cat_image.py.
4. Сохраните тесты в файл, например test_cat_image.py.

## Использование

Чтобы получить случайное изображение кошки, используйте функцию get_random_cat_image():

from cat_image import get_random_cat_image

url = get_random_cat_image()
print(url)  # Выводит URL изображения кошки


## Тестирование

Для запуска тестов, выполните следующую команду в терминале:

python -m unittest test_cat_image.py


## Функции

- get_random_cat_image(): делает запрос к TheCatAPI и возвращает URL случайного изображения кошки или None, если запрос не удался.

## Тесты

- test_successful_request: проверяет, что функция возвращает правильный URL при успешном запросе.
- test_unsuccessful_request: проверяет, что функция возвращает None при неуспешном запросе (например, статус код 404).

## Лицензия

Этот проект лицензирован на условиях MIT License.
