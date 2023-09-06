/*
Задание
Вывести автора, название  и цены тех книг, количество которых меньше 10.

Результат:

+------------------+--------------------+--------+
| author           | title              | price  |
+------------------+--------------------+--------+
| Булгаков М.А.    | Мастер и Маргарита | 670.99 |
| Булгаков М.А.    | Белая гвардия      | 540.50 |
| Достоевский Ф.М. | Братья Карамазовы  | 799.01 |
+------------------+--------------------+--------+
Структура и наполнение таблицы book:
+---------+-----------------------+------------------+--------+--------+
| book_id | title                 | author           | price  | amount |
+---------+-----------------------+------------------+--------+--------+
| 1       | Мастер и Маргарита    | Булгаков М.А.    | 670.99 | 3      |
| 2       | Белая гвардия         | Булгаков М.А.    | 540.50 | 5      |
| 3       | Идиот                 | Достоевский Ф.М. | 460.00 | 10     |
| 4       | Братья Карамазовы     | Достоевский Ф.М. | 799.01 | 2      |
| 5       | Стихотворения и поэмы | Есенин С.А.      | 650.00 | 15     |
+---------+-----------------------+------------------+--------+--------+
*/

SELECT author, title, price
FROM book
WHERE amount < 10;