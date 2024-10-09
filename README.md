# Assessment
Overview
This project is a simplified e-commerce system implemented in Python. It models the core components of an e-commerce platform, including Users, Products, Orders, and Payments. The system allows users to create orders, add multiple products to their orders, and process payments.

Components
1. User
Represents a user of the e-commerce platform.

Attributes:

user_id: Unique identifier for the user.
name: Name of the user.
email: Email address of the user.
orders: List of orders placed by the user.
Methods:

place_order(order): Allows the user to place an order.
2. Product
Represents a product available for purchase.

Attributes:
product_id: Unique identifier for the product.
name: Name of the product.
price: Price of the product.
3. Order
Represents an order placed by a user.

Attributes:

order_id: Unique identifier for the order.
user: The user who placed the order.
products: List of products included in the order (with quantities).
total_amount: Total cost of the order.
Methods:

add_product(product, quantity): Adds a product to the order with a specified quantity.
calculate_total(): Calculates the total amount for the order.
4. Payment
Represents a payment made for an order.

Attributes:

payment_id: Unique identifier for the payment.
order: The order associated with the payment.
amount: The amount to be paid.
status: The current status of the payment (e.g., Pending, Completed, Failed).
Methods:

process_payment(): Processes the payment and updates the status based on whether the payment amount matches the order total.
To run Python file:
python eCommerce.py
python inventory.py
