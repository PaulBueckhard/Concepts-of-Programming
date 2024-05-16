class Order:
    def __init__(self):
        self._state = 'new'
        self._valid_states = {'new', 'paid', 'shipped', 'delivered', 'canceled'}

    def set_state(self, new_state):
        if new_state in self._valid_states:
            self._state = new_state
        else:
            raise ValueError(f"Invalid state: {new_state}")

    def get_state(self):
        return self._state

    def pay(self):
        if self._state == 'new':
            self.set_state('paid')
        else:
            raise ValueError("Order cannot be paid in its current state")

    def ship(self):
        if self._state == 'paid':
            self.set_state('shipped')
        else:
            raise ValueError("Order cannot be shipped in its current state")

    def deliver(self):
        if self._state == 'shipped':
            self.set_state('delivered')
        else:
            raise ValueError("Order cannot be delivered in its current state")

    def cancel(self):
        if self._state in {'new', 'paid'}:
            self.set_state('canceled')
        else:
            raise ValueError("Order cannot be canceled in its current state")

# Example usage
if __name__ == "__main__":
    order = Order()
    print("Initial State:", order.get_state())  # Initial State: new

    order.pay()
    print("State after payment:", order.get_state())  # State after payment: paid

    order.ship()
    print("State after shipping:", order.get_state())  # State after shipping: shipped

    order.deliver()
    print("State after delivery:", order.get_state())  # State after delivery: delivered

    # Uncommenting the following lines will raise exceptions due to invalid state transitions
    # order.cancel()  # Raises ValueError: Order cannot be canceled in its current state
    # order.ship()    # Raises ValueError: Order cannot be shipped in its current state
