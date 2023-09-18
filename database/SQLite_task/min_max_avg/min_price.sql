/*
 Вывести минимальную цену книги каждого автора

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
 +----------------+---------+
|author          |min_price|
+----------------+---------+
|Бехтерев С.С.   |460      |
|Булгаков М.А.   |540.5    |
|Гумилев Н.С.    |460      |
|Достоевский Ф.М.|460      |
|Есенин С.А.     |650      |
|Иванов С.С.     |50       |
|Пушкин А.С.     |520.5    |
|Рушди Салман    |950      |
+----------------+---------+

 */

SELECT author, MIN(price) as min_price
FROM book
GROUP BY author;