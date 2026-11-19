# Дефект 1 (Common Coupling): глобальна змінна змінюється та читається напряму
GLOBAL_TAX_RATE = 0.20

class CustomerProfile:
    def __init__(self, user_id, email, password_hash, city, loyalty_points):
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
        self.city = city
        self.loyalty_points = loyalty_points

# Дефект 2 (Stamp Coupling): передається весь об'єкт CustomerProfile замість потрібного поля city
def calculate_delivery_cost(customer: CustomerProfile, weight_kg: float) -> float:
    base_rate = 50.0 if customer.city == "Ivano-Frankivsk" else 110.0
    return base_rate + (weight_kg * 12.0)

# Дефект 3 (Control Coupling): параметр mode_flag керує внутрішнім розгалуженням функції
def process_invoice(amount: float, customer: CustomerProfile, weight_kg: float, mode_flag: int) -> dict:
    global GLOBAL_TAX_RATE
    if mode_flag == 1:
        # Звичайний розрахунок замовлення
        delivery = calculate_delivery_cost(customer, weight_kg)
        total = (amount * (1 + GLOBAL_TAX_RATE)) + delivery
        return {"status": "PROCESSED", "total": round(total, 2)}
    elif mode_flag == 2:
        # Розрахунок зі скасуванням податку (псує глобальний стан!)
        GLOBAL_TAX_RATE = 0.0
        total = amount + calculate_delivery_cost(customer, weight_kg)
        return {"status": "TAX_EXEMPT", "total": round(total, 2)}
    else:
        return {"status": "CANCELLED", "total": 0.0}
