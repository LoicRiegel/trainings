from dataclasses import dataclass


# BEFORE

@dataclass
class Cash:
    """Payment method using cash."""

    discount: float = 0.1


@dataclass
class CreditCard:
    """Payment method using credit card."""

    number: str
    tax: float = 0.1


class Sale:
    ...
    def total_discounted_price(self, payment_method: Cash | CreditCard) -> float:
        """Calculates the net price of sale."""
        if isinstance(payment_method, Cash):
            return self.total_price * (1 - payment_method.discount)
        else:
            return self.total_price * (1 + payment_method.tax)

"""
Lots of coupling here
directly coupled with the Cash and CreditCard class
"""

# Adding a new payment method

class PayPal: pass

class Sale:
    ...
    def total_discounted_price(self, payment_method: Cash | CreditCard | PayPal) -> float:
        """Calculates the net price of sale."""
        if isinstance(payment_method, Cash):
            return self.total_price * (1 - payment_method.discount)
        elif isinstance(payment_method, PayPal):
            return self.total_price * ...
        else:
            return self.total_price * (1 + payment_method.tax)

"""
Now even more coupled. We added coupling to the PayPal class.
"""
