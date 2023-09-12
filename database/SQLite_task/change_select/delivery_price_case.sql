/*
Определить стоимость доставки:
- для книг стоимостью 500 и менее, установить в размере 99,99
- при количестве книг на складе менее 5, установить в размере 149.99
- для остальных случаев доставка должна быть бесплатной
Определить новую стоимость для книг:
- для книг, совокупной стоимостью более 5000, добавить 20% к стоимости за экземпляр
- для остальных случаев снизить стоимость одного экземпляра на 20%
Настроить фильтр при выборке:
- только позиции творчества авторов: Булгаков и Есенин, при количестве экземпляров на складе: от 3 до 14 включительно.
Сортировку выполнить:
- по имени автора в порядке возрастания
- затем по названию в порядке убывания
- по стоимости доставки (от меньшей к большей)
В таблице должны быть отображены данные:
- автора
- название
- цену, как real_price
- количество
- новую цену, как new_price
- стоимость доставки, как delivery_price


Структура и наполнение таблицы book:
+---------------------+----------------+------+------+
|title                |author          |amount|price |
+---------------------+----------------+------+------+
|Мастер и Маргарита   |Булгаков М.А.   |3     |670.99|
|Белая гвардия        |Булгаков М.А.   |5     |540.5 |
|Идиот                |Достоевский Ф.М.|10    |460   |
|Братья Карамазовы    |Достоевский Ф.М.|2     |799.01|
|Стихотворения и поэмы|Есенин С.А.     |15    |650   |
|Дети полуночи        |Рушди Салман    |5     |950   |
|                     |Иванов С.С.     |10    |50    |
|Лирика               |Гумилев Н.С.    |10    |460   |
|Поэмы                |Бехтерев С.С.   |10    |460   |
|Капитанская дочка    |Пушкин А.С.     |7     |520.5 |
+---------------------+----------------+------+------+

Результат:
+---------------+-----------------------+------------+--------+-----------+----------------+
| author        | title                 | real_price | amount | new_price | delivery_price |
+---------------+-----------------------+------------+--------+-----------+----------------+
| Булгаков М.А. | Мастер и Маргарита    | 670.99     | 3      | 536.79    | 149.99         |
| Булгаков М.А. | Белая гвардия         | 540.50     | 5      | 432.40    | 0.00           |
+---------------+-----------------------+------------+--------+-----------+----------------+
 */

SELECT author,
       title,
       price   AS real_price,
       amount,
       CASE
           WHEN (amount * price) > 5000 THEN ROUND(price * 1.20, 2)
           ELSE ROUND(price - (price * 0.20), 2)
           END AS new_price,
       CASE
           WHEN price < 500 THEN 99.9
           WHEN amount < 5 THEN 149.9
           ELSE ROUND(0.00, 2)
           END AS delivery_price
FROM book
WHERE (author LIKE 'Булгаков %' OR author LIKE 'Есенин %')
  AND amount BETWEEN 3 AND 14
ORDER BY author, title DESC, delivery_price;