/*
    Структура и наполнение таблицы book
+--+---------------------+----------------+------+------+
|id|title                |author          |price |amount|
+--+---------------------+----------------+------+------+
|1 |Мастер и Маргарита   |Булгаков М.А.   |670.99|3     |
|2 |Белая гвардия        |Булгаков М.А.   |540.5 |5     |
|3 |Идиот                |Достоевский Ф.М.|460   |10    |
|4 |Братья Карамазовы    |Достоевский Ф.М.|799.01|2     |
|5 |Стихотворения и поэмы|Есенин С.А.     |650   |15    |
|6 |Дети полуночи        |Рушди Салман    |950   |5     |
|7 |                     |Иванов С.С.     |50    |10    |
|8 |Лирика               |Гумилев Н.С.    |460   |10    |
|9 |Поэмы                |Бехтерев С.С.   |460   |10    |
|10|Капитанская дочка    |Пушкин А.С.     |520.5 |7     |
+--+---------------------+----------------+------+------+

 Результат
 +----------------+-----------------+------------+
|Минимальная_цена|Максимальная_цена|Средняя_цена|
+----------------+-----------------+------------+
|50              |950              |580.13      |
+----------------+-----------------+------------+
Вывести  цену самой дешевой книги, цену самой дорогой и среднюю цену уникальных книг на складе.
    Названия столбцов Минимальная_цена, Максимальная_цена, Средняя_цена соответственно.
    Среднюю цену округлить до двух знаков после запятой.
 */

SELECT MIN(price) AS  Минимальная_цена,
       MAX(price) AS Максимальная_цена,
       ROUND(AVG(DISTINCT price), 2) AS Средняя_цена
FROM book;