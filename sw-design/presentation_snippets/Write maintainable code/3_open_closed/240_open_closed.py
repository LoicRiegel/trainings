# BEFORE

class PaymentProcessor:
    def pay_visa(self, order: Order, security_code: str):
        print("Processing payment with VISA")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

    def pay_mastercard(self, order: Order, security_code: str):
        print("Processing payment with Mastercard")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

def main():
    ...
    payment_processor = PaymentProcessor()
    payment_processor.pay_visa(order: Order, "0372846")


"""
Here if we want to add a new payment method (e.g. allow the users to pay via PayPal),
we would have to change the existing code of PaymentProcessor class.
"""

# AFTER

from abc import ABC, abstractmethod   # don't show on slide


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order, security_code: str):
        """Handle the payment."""


class VisaPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str):
        print("Processing payment with VISA")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


class MastercardPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str):
        print("Processing payment with Mastercard")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

def main():
    ...
    payment_processor = VisaPaymentProcessor()
    payment_processor.pay_visa(order: Order, "0372846")


"""Now it's way easier to add a new payment type and we can do this without touching the
existing code
"""

# AFTER - after adding a PayPal WITOUT TOUCHING the existing code


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order, security_code: str):
        """Handle the payment."""


class VisaPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str):
        print("Processing payment with VISA")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


class MastercardPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str):
        print("Processing payment with Mastercard")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class PayPalPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str):
        print("Processing payment with PayPal")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


def main():
    ...
    payment_processor = PayPalPaymentProcessor()
    payment_processor.pay_visa(order: Order, "0372846")