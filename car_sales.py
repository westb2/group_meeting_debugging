import random
from random_word import RandomWords
import json

def generate_random_dealership_fee():
    word_generator = RandomWords()
    # Return a single random word
    referral_code = word_generator.get_random_word()
    return random.random() * 50.0

def calculate_car_price():
    TAX_RATE = 1.1
    with open("secret_car_stuff.json") as file:
        config = json.load(file)
        base_price = config["base_price"]
        after_market_products_price = config["after_market_products_price"]
        total_price = (base_price + after_market_products_price + generate_random_dealership_fee())*TAX_RATE
        print(f"I'll sell you a car for {total_price}. Deal?\n")

calculate_car_price()