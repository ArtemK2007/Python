def show_all(magazines):
    for name, data in magazines.items():
        print(f"{name}: ціна {data['price']} грн, тираж {data['copies']} прим.")

def avg_price_small_copies(magazines):
    prices = [data["price"] for data in magazines.values() if data["copies"] < 10000]
    if prices:
        return sum(prices) / len(prices)
    return None

magazines = {
    "Magazine1": {"price": 120, "copies": 8000},
    "Magazine2": {"price": 90, "copies": 15000},
    "Magazine3": {"price": 100, "copies": 9500},
    "Magazine4": {"price": 150, "copies": 7000},
    "Magazine5": {"price": 80, "copies": 20000}
}

show_all(magazines)

avg = avg_price_small_copies(magazines)
print(f"\nСередня ціна журналів з тиражем < 10000: {avg:.2f} грн")

