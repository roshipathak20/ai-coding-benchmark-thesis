# Task: SQL query generation
# Write an SQL query that returns
# total purchase amount per customer.
#
# Tables:
# customers(id, name)
# orders(id, customer_id, amount)
#
# Output columns:
# customer_name
# total_spent
#
# Use JOIN and GROUP BY.

query = """
SELECT c.name AS customer_name, SUM(o.amount) AS total_spent
FROM customers c
JOIN orders o ON c.id = o.customer_id
GROUP BY c.name
"""