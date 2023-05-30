from abc import ABC, abstractmethod

# Before
class StripePaymentHandler:
    ...
    def handle_payment(self, total: int):
        ...

def process_payment(price: int, payment_handler: StripePaymentHandler) -> None:
    logging.info(f"Order total is ${total/100:.2f}.")
    payment_handler = StripePaymentHandler()
    payment_handler.handle_payment(total)
    logging.info("Order completed.")

def main():
    ...
    stripe_payment_handler = StripePaymentHandler()
    process_payment(5000, stripe_payment_handler)

# After
class StripePaymentHandler:
    ...
    def handle_payment(self, total: int):
        ...

class PaymentHandler(ABC):
    @abstractmethod
    def handle_payment(self, total: int) -> None:
        """Handle payment."""


def process_payment(price: int, payment_handler: PaymentHandler) -> None:
    logging.info(f"Order total is ${total/100:.2f}.")
    payment_handler.handle_payment(total)
    logging.info("Order completed.")

def main():
    ...
    stripe_payment_handler = StripePaymentHandler()
    process_payment(5000, stripe_payment_handler)

