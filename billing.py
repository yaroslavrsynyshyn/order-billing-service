
class CustomerProfile:
    def __init__(self, user_id, email, password_hash, city, loyalty_points):
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
        self.city = city
        self.loyalty_points = loyalty_points
        
def calculate_delivery_cost(city: str, weight_kg: float) -> float:
    if city == "Ivano-Frankivsk":
        base_rate = 50.0
    elif city == "Kyiv":
        base_rate = 80.0
    else:
        base_rate = 110.0
    return base_rate + (weight_kg * 12.0)

def process_standard_invoice(amount: float, city: str, weight_kg: float, tax_rate: float = 0.20) -> dict:
    delivery = calculate_delivery_cost(city, weight_kg)
    total = (amount * (1 + tax_rate)) + delivery
    return {"status": "PROCESSED", "total": round(total, 2)}


def process_tax_exempt_invoice(amount: float, city: str, weight_kg: float) -> dict:
    delivery = calculate_delivery_cost(city, weight_kg)
    total = amount + delivery
    return {"status": "TAX_EXEMPT", "total": round(total, 2)}
