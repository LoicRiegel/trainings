import string

CATALOGUE: dict[str, int]
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
        catalogue_price = CATALOGUE[model]

        # compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if model == "Tesla Model 3" or model == "Volkswagen ID3":
            tax_percentage = 0.02

        # compute the payable tax
        payable_tax = tax_percentage * catalogue_price
        
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