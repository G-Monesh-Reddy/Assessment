class Product:
    def __init__(self, product_id, name, stock, restock_threshold = 10):
        self.product_id = product_id
        self.name = name
        self.stock = stock
        self.restock_threshold = restock_threshold

    def __str__(self):
        return f"Product(name={self.name}, stock={self.stock})"


def process_orders(products, orders):
    
    restock_alerts = []

    for product_id, quantity_ordered in orders.items():
        if product_id not in products:
            print(f"Error: Product with ID {product_id} does not exist.")
            continue

        product = products[product_id]

        
        if product.stock >= quantity_ordered:
            product.stock -= quantity_ordered
            print(f"Processed order for {product.name}, new stock: {product.stock}")
            
            
            if product.stock < product.restock_threshold:
                restock_alerts.append(product_id)
                print(f"Alert: {product.name} stock below threshold. Restock needed.")
        else:
            print(f"Error: Insufficient stock for {product.name}. Order not processed.")
    
    return restock_alerts


def restock_items(products, restock_list):
    
    for product_id, restock_qty in restock_list.items():
        if product_id not in products:
            print(f"Error: Product with ID {product_id} does not exist.")
            continue
        
        product = products[product_id]
        product.stock += restock_qty
        print(f"Restocked {product.name}, new stock: {product.stock}")

# Example Usage
if __name__ == "__main__":
    
    products = {
        101: Product(product_id=101, name="Laptop", stock=15),
        102: Product(product_id=102, name="Phone", stock=8),
        103: Product(product_id=103, name="Tablet", stock=12),
    }

    
    orders = {
        101: 5,  # Order 5 laptops
        102: 3,  # Order 3 phones
        103: 1,  # Order 1 tablet
        104: 2   # Invalid product
    }

    
    products_needing_restock = process_orders(products, orders)

    
    restock_list = {product_id: 10 for product_id in products_needing_restock}
    restock_items(products, restock_list)
