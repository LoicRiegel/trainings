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
class PaymentHandler(ABC):
    @abstractmethod
    def handle_payment(self, total: int) -> None:
        """Handle payment."""

class StripePaymentHandler:
    ...
    def handle_payment(self, total: int):
        ...

def process_payment(price: int, payment_handler: PaymentHandler) -> None:
    logging.info(f"Order total is ${total/100:.2f}.")
    payment_handler.handle_payment(total)
    logging.info("Order completed.")

def main():
    ...
    stripe_payment_handler = StripePaymentHandler()
    process_payment(5000, stripe_payment_handler)


# After part 2
class PaymentHandler(ABC):
    @abstractmethod
    def handle_payment(self, total: int) -> None:
        """Handle payment."""

class StripePaymentHandler:
    ...
    def handle_payment(self, total: int):
        ...

class PayPalPaymentHandler:
    ...
    def handle_payment(self, total: int):
        ...


def process_payment(price: int, payment_handler: PaymentHandler) -> None:
    logging.info(f"Order total is ${total/100:.2f}.")
    payment_handler.handle_payment(total)
    logging.info("Order completed.")

def main():
    ...
    stripe_payment_handler = StripePaymentHandler()()
    process_payment(5000, stripe_payment_handler)


# After part 2
class PaymentHandler(ABC):
    @abstractmethod
    def handle_payment(self, total: int) -> None:
        """Handle payment."""

class StripePaymentHandler:
    ...
    def handle_payment(self, total: int):
        ...

class PayPalPaymentHandler:
    ...
    def handle_payment(self, total: int):
        ...


def process_payment(price: int, payment_handler: PaymentHandler) -> None:
    logging.info(f"Order total is ${total/100:.2f}.")
    payment_handler.handle_payment(total)
    logging.info("Order completed.")

def main():
    ...
    paypal_payment_handler = PayPalPaymentHandler()()
    process_payment(5000, paypal_payment_handler)


"""
Initial: where we left of after dependency injection.
process_payment is still depending of StripePaymentHandler specifically. So it can only work with it.
We can only use Stripe.

Step 1: create an abstration and use it in process_payment

Step 2: now we can have as many payment handlers as we want. As soon as they implement handle_payment
as specified in our interface, process_payment can use it.
For instance, create a PayPalPaymentHandler if users want to use PayPal now.

Step 3: in the main, it's as easy as changing the resources we create and supplying a different object.
"""
