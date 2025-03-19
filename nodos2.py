from collections import deque

class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print("     Customer:", self.get_customer())
        print("     Quantity:", self.get_qtty())
        print("     ------------")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer


class OrderQueue:
    def __init__(self):
        self.queue = deque()  
    def add_order(self, order):
        self.queue.append(order)
        print(f"Pedido agregado para el cliente: {order.get_customer()}")

    def process_next_order(self):
        if self.queue:
            next_order = self.queue.popleft()
            print("Procesando pedido:")
            next_order.print()
        else:
            print("No hay pedidos pendientes para procesar.")

    def show_all_orders(self):
        if not self.queue:
            print("No hay pedidos en la cola.")
        else:
            print("Pedidos en la cola:")
            for order in self.queue:
                order.print()


if __name__ == "__main__":
    order_queue = OrderQueue()

    order1 = Order(10, "Cliente A")
    order2 = Order(5, "Cliente B")
    order3 = Order(20, "Cliente C")

    order_queue.add_order(order1)
    order_queue.add_order(order2)
    order_queue.add_order(order3)

    order_queue.show_all_orders()

    order_queue.process_next_order()
    order_queue.process_next_order()
    order_queue.process_next_order()

    order_queue.process_next_order()
