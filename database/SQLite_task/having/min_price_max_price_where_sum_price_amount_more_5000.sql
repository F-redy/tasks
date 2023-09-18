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
+----------------+----------------+-----------------+
|author          |Минимальная_цена|Максимальная_цена|
+----------------+----------------+-----------------+
|Достоевский Ф.М.|460             |799.01           |
|Есенин С.А.     |650             |650              |
+----------------+----------------+-----------------+

В запросы с групповыми функциями можно включать условие отбора строк,
    которое в обычных запросах записывается после WHERE.
В запросах с групповыми функциями вместо WHERE используется ключевое слово HAVING ,
    которое размещается после оператора GROUP BY.

Найти минимальную и максимальную цену книг всех авторов, общая стоимость книг которых больше 5000.
 */


SELECT author,
       MIN(price) AS Минимальная_цена,
       MAX(price) AS Максимальная_цена
FROM book
GROUP BY author
HAVING SUM(price * amount) > 5000;