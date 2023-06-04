# TODO: actually it's simillar to the 231 example. Maybe see if we can change the example here

def luhn_checksum(card_number: str) -> bool:
    ...


class Customer:
    def __init__(self, name, phone, cc_number, cc_exp_month, cc_exp_year, cc_valid= False) -> None:
        self.name = name
        self.phone = phone
        self.cc_number = cc_number
        self.cc_exp_month = cc_exp_month
        self.cc_exp_year = cc_exp_year
        self.cc_valid = cc_valid
        self.name = name
        self.valid = valid

def validate_card(customer: Customer) -> bool:
    customer.cc_valid = (
        luhn_checksum(customer.cc_number)
        and datetime(customer.cc_exp_year, customer.cc_exp_month, 1) > datetime.now()
    )
    return customer.cc_valid


def main():
    alice = Customer(name="Alice", phone="2341", cc_number="1249190007575069",
        cc_exp_month=1, cc_exp_year=2024
    )
    valid = validate_card(alice)
    print(f"Alice card is valid: {valid}")



# AFTER

def luhn_checksum(card_number: str) -> bool:
    ...


class Customer:
    def __init__(self, name, phone, cc_number, cc_exp_month, cc_exp_year, cc_valid= False) -> None:
        self.name = name
        self.phone = phone
        self.cc_number = cc_number
        self.cc_exp_month = cc_exp_month
        self.cc_exp_year = cc_exp_year
        self.cc_valid = cc_valid
        self.name = name
        self.valid = valid

def validate_card(customer: Customer) -> bool:
    return (
        luhn_checksum(customer.cc_number)
        and datetime(customer.cc_exp_year, customer.cc_exp_month, 1) > datetime.now()
    )

def main():
    alice = Customer(name="Alice", phone="2341", cc_number="1249190007575069",
        cc_exp_month=1, cc_exp_year=2024
    )
    alice.cc_valid = validate_card(alice)
    print(f"Alice card is valid: {alice.cc_valid}")