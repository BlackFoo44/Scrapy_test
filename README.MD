# Scrapy Test

Тестовое задание: 
Тестовое задание

Первое: Со страницы https://krasn.russcvet.ru/catalog/enamels/ используя Scrapy выбрать из первых 16 товаров Название и Цену
и выгрузить эти данные используя openpyxl в xls файл с двумя столбцами Name, Price

Второе: Выгрузить все товары из категории Эмали

Третее: Спроектировать код так, чтобы можно было его использовать для других категорий и сайтов



## Как запустить:
Установка виртуального окружения 
-
- 
  ```bash
  pip install poetry 
  poetry shell
  poetry install
  ```
- Запуск из терминала. Нужно перейти в папку с пауками:
- 
  ```bash
  cd path/EmalesParser
  scrapy crawl first_16_enamels -O first_16_enamels.csv
  scrapy crawl all_enamels -O all_enamels.csv
  scrapy crawl all_items -O all_items.csv
  ```
  
Далее необходимо запустить файл reformator.py
  ```bash
  python reformator.py
  ```