/*
Для каждой книги из таблицы book установим скидку следующим образом:
    если количество книг меньше 4, то скидка будет составлять 50% от цены, в противном случае 30%.
Цена по скидке должна отображаться с двумя знаками после запятой.
Результат:

+-----------------------+--------+--------+--------+
| title                 | amount | price  | sale   |
+-----------------------+--------+--------+--------+
| Мастер и Маргарита    | 3      | 670.99 | 335.50 |
| Белая гвардия         | 5      | 540.50 | 378.35 |
| Идиот                 | 10     | 460.00 | 322.00 |
| Братья Карамазовы     | 2      | 799.01 | 399.51 |
| Стихотворения и поэмы | 15     | 650.00 | 455.00 |
+-----------------------+--------+--------+--------+
 */
SELECT title, amount, price,
    ROUND(IF(amount<4, price*0.5, price*0.7),2) AS sale
FROM book;