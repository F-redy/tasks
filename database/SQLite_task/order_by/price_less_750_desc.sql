/*
Вывести автора, название и количество книг, в отсортированном в алфавитном порядке по автору и по убыванию количества,
для тех книг, цены которых меньше 750 грн.

Результат:

+------------------+-----------------------+------------+
| author           | title                 | Количество |
+------------------+-----------------------+------------+
| Булгаков М.А.    | Белая гвардия         | 5          |
| Булгаков М.А.    | Мастер и Маргарита    | 3          |
| Достоевский Ф.М. | Идиот                 | 10         |
| Есенин С.А.      | Стихотворения и поэмы | 15         |
+------------------+-----------------------+------------+
 */

SELECT title, author, price, amount
FROM book
WHERE price < 750
ORDER BY author, amount DESC;

/*
 Можно использовать другие варианты записи запроса:

SELECT author, title, amount AS Количество
FROM book
WHERE price < 750
ORDER BY author, Количество DESC;

SELECT author, title, amount AS Количество
FROM book
WHERE price < 750
ORDER BY 1, 3 DESC;
 */