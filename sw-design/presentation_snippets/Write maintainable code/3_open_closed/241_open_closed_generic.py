"""
Think about the Open-closed principle in a more generic way:
how much effort (diff) does it require to add a new feature?
"""


# BEFORE


import string

MODELS: list[str] = [
    "Volkswagen Golf",
    "Fiat 500",
    "Opel Corsa",
    "Tesla Model 3",
    "Volkswagen ID3",
]
MODELS_CATALOGUE_PRICE: dict[str, int] = {
    "Volkswagen Golf": 30_000,
    "Fiat 500": 17_500,
    "Opel Corsa": 20_000,
    "Tesla Model 3": 45_000,
    "Volkswagen ID3": 40_000,
}


class VehicleApplication:

    def __init__(self) -> None:
        self.vehicle_registry: list = []

    def register_vehicle(self, model: str):
        # generate a vehicle id of length 12
        vehicle_id = ''.join(random.choices(string.ascii_uppercase, k=12))

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        license_plate = f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

        # get the catalogue price
        catalogue_price = MODELS_CATALOGUE_PRICE[model]

        # compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if model == ("Tesla Model 3", "Volkswagen ID3"):
            tax_percentage = 0.02

        # Apply special discouts on certain models (all VW and certain other)
        if "Volkswagen" in model or model == ("Fiat 500"):
            discount_percentage = 0.10
        elif model == "Volkswagen ID3":
            discount_percentage = 0.06
        else:
            discount_percentage = 0.0
        price_after_discount = (1 - discount_percentage) * catalogue_price

        # compute the payable tax
        payable_tax = tax_percentage * price_after_discount

        # register the vehicle
        self.vehicle_registry.append({
            "model": model,
            "catalogue_price": catalogue_price,
            "payable_tax": payable_tax
        })

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"Brand: {model}")
        print(f"Id: {vehicle_id}")
        print(f"License plate: {license_plate}")
        print(f"Payable tax: {payable_tax}")

"""Here everything is scattered
- definition of all models and their catalogue price at the top
- special discounts
- electric or not --> tax_percentage
"""

# AFTER

class FuelType(Enum):
    """Types of fuel used in a vehicle."""

    ELECTRIC = auto()
    PETROL = auto()

TAXES = {
    FuelType.ELECTRIC: 0.02,
    FuelType.PETROL: 0.05,
}

@dataclass
class VehicleModelInfo:
    """Class that contains basic information about a vehicle model."""

    brand: str
    model: str
    catalogue_price: int
    fuel_type: FuelType = FuelType.PETROL
    discount_percentage: int = 0.0

    @property
    def tax(self) -> float:
        """Tax to be paid when registering a vehicle of this type."""
        price_after_discount = (1 - self.discount_percentage) * self.catalogue_price
        tax_percentage = TAXES[self.fuel_type]
        return tax_percentage * self.price_after_discount


AVAILABLE_MODELS = [
    VehicleModelInfo("Tesla", "Model 3", 50000, FuelType.ELECTRIC, discount_percentage=0.02),
    VehicleModelInfo("Volkswagen", "ID3", 35000, FuelType.ELECTRIC),
    VehicleModelInfo("BMW", "520e", 60000, FuelType.PETROL),
    VehicleModelInfo("Tesla", "Model Y", 55000, FuelType.ELECTRIC),
]

"""
- Adding a new vehicle model is super easy, it's done in one line!
- Adding a new fuel type is very easy

WARNING: here there is way too many responsibilities!! SRP is not applied!
"""
