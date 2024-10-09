
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.orders = []  

    def place_order(self, order):
        self.orders.append(order)


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class Order:
    def __init__(self, order_id, user):
        self.order_id = order_id
        self.user = user
        self.products = []  
        self.total_amount = 0

    def add_product(self, product, quantity):
        self.products.append((product, quantity))
        self.total_amount += product.price * quantity

    def calculate_total(self):
        return self.total_amount


class Payment:
    def __init__(self, payment_id, order, amount):
        self.payment_id = payment_id
        self.order = order
        self.amount = amount
        self.status = "Pending"

    def process_payment(self):
        
        if self.amount == self.order.calculate_total():
            self.status = "Completed"
        else:
            self.status = "Failed"




user1 = User(user_id=1, name="Alice", email="alice@example.com")


product1 = Product(product_id=101, name="Laptop", price=1000)
product2 = Product(product_id=102, name="Mouse", price=50)


order1 = Order(order_id=201, user=user1)
order1.add_product(product1, quantity=1)
order1.add_product(product2, quantity=2)


payment1 = Payment(payment_id=301, order=order1, amount=1100)
payment1.process_payment()


print(f"Payment status: {payment1.status}")
