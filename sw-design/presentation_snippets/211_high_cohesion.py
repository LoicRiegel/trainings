def generate_vehicle_id(length: int) -> str:
    return ''.join(random.choices(string.ascii_uppercase, k=length))

def generate_vehicle_license(id: str) -> str:
    return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"
