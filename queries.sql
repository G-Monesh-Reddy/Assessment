--1.	Write a SQL query to retrieve the top 5 customers who have purchased the most books (by total quantity) over the last year
SELECT Customers.customer_id, Customers.name, SUM(OrderDetails.quantity) AS total_books_purchased
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id
JOIN OrderDetails ON Orders.order_id = OrderDetails.order_id
WHERE YEAR(Orders.order_date) = 2023
GROUP BY Customers.customer_id, Customers.name
ORDER BY total_books_purchased DESC
LIMIT 5;
--2.	Write a SQL query to calculate the total revenue generated from book sales by each author.
SELECT Books.author, SUM(OrderDetails.quantity * Books.price) AS total_revenue
FROM Books
JOIN OrderDetails ON Books.book_id = OrderDetails.book_id
GROUP BY Books.author
ORDER BY total_revenue DESC;
--3.	Write a SQL query to retrieve all books that have been ordered more than 10 times, along with the total quantity ordered for each book.
SELECT Books.author, SUM(OrderDetails.quantity * Books.price) AS total_revenue
FROM Books
JOIN OrderDetails ON Books.book_id = OrderDetails.book_id
GROUP BY Books.author
ORDER BY total_revenue DESC;
