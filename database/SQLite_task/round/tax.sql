/*Задание
В конце года цену всех книг на складе пересчитывают – снижают ее на 30%.
Написать SQL запрос, который из таблицы book выбирает названия, авторов, количества и вычисляет новые цены книг.
Столбец с новой ценой назвать new_price, цену округлить до 2-х знаков после запятой.

Результат:

+-----------------------+------------------+--------+-----------+
| title                 | author           | amount | new_price |
+-----------------------+------------------+--------+-----------+
| Мастер и Маргарита    | Булгаков М.А.    | 3      | 469.69    |
| Белая гвардия         | Булгаков М.А.    | 5      | 378.35    |
| Идиот                 | Достоевский Ф.М. | 10     | 322.00    |
| Братья Карамазовы     | Достоевский Ф.М. | 2      | 559.31    |
| Стихотворения и поэмы | Есенин С.А.      | 15     | 455.00    |
+-----------------------+------------------+--------+-----------+
*/
SELECT title, author, amount,
        ROUND(price * 0.7, 2) AS new_price
FROM book