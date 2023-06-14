# Before
class StripePaymentHandler:
    ...
    def handle_payment(self, total: int):
        ...

def process_payment(amount: int) -> None:
    logging.info(f"Order total is ${amount/100:.2f}.")
    payment_handler = StripePaymentHandler()
    payment_handler.handle_payment(amount)
    logging.info("Order completed.")

def main():
    ...
    process_payment(5000)


# After


class StripePaymentHandler:
    ...
    def handle_payment(self, amount: int):
        ...

def process_payment(amount: int, payment_handler: StripePaymentHandler) -> None:
    logging.info(f"Order total is ${amount/100:.2f}.")
    payment_handler.handle_payment(amount)
    logging.info("Order completed.")

def main():
    ...
    stripe_payment_handler = StripePaymentHandler()
    process_payment(5000, stripe_payment_handler)

