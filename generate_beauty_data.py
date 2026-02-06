# import pandas as pd
# import random

# # Number of rows you want
# NUM_ROWS = 500   # change to 1000 if needed

# ages = list(range(18, 45))
# genders = ["Female", "Male"]
# skin_tones = ["Fair", "Medium", "Dark"]
# skin_types = ["Oily", "Dry", "Combination", "Normal"]
# skin_problems = ["Acne", "Pigmentation", "Dryness", "Wrinkles", "Dullness", "None"]
# sensitivity = ["Yes", "No"]
# climates = ["Humid", "Dry", "Cold", "Moderate", "Hot"]

# product_types = ["Face Wash", "Moisturizer", "Serum", "Face Cream"]
# brands = ["Lakme", "Plum", "Minimalist", "Cetaphil", "Neutrogena", "Nivea", "The Ordinary"]
# ingredients_types = ["Natural", "Chemical"]
# price_ranges = ["Budget", "Mid", "Premium"]

# recommended_products = [
#     "Salicylic Acid Cleanser",
#     "Vitamin C Serum",
#     "Oil Free Moisturizer",
#     "Hydrating Face Cream",
#     "Niacinamide Serum",
#     "Acne Control Face Wash",
#     "Anti Aging Cream"
# ]

# data = []

# for _ in range(NUM_ROWS):
#     row = {
#         "age": random.choice(ages),
#         "gender": random.choice(genders),
#         "skin_tone": random.choice(skin_tones),
#         "skin_type": random.choice(skin_types),
#         "skin_problem": random.choice(skin_problems),
#         "sensitivity": random.choice(sensitivity),
#         "climate": random.choice(climates),
#         "product_type": random.choice(product_types),
#         "brand": random.choice(brands),
#         "ingredients_type": random.choice(ingredients_types),
#         "price_range": random.choice(price_ranges),
#         "recommended_product": random.choice(recommended_products)
#     }
#     data.append(row)

# df = pd.DataFrame(data)

# df.to_csv("beauty_product_data.csv", index=False)

# print("CSV file created successfully with", NUM_ROWS, "rows")

def recommend_product(skin_problem, skin_type):
    if skin_problem == "Acne":
        return random.choice([
            "Minimalist Salicylic Acid Cleanser",
            "Plum Green Tea Face Wash",
            "La Roche-Posay Effaclar Duo+"
        ])

    elif skin_problem == "Pigmentation":
        return random.choice([
            "The Ordinary Vitamin C Suspension",
            "Lakme 9 to 5 Vitamin C+ Serum",
            "Dot & Key Vitamin C Serum"
        ])

    elif skin_problem == "Wrinkles":
        return random.choice([
            "Olay Regenerist Micro-Sculpting Cream",
            "Neutrogena Rapid Wrinkle Repair",
            "Forest Essentials Soundarya Cream"
        ])

    elif skin_problem == "Dryness" or skin_type == "Dry":
        return random.choice([
            "Cetaphil Moisturizing Cream",
            "Simple Hydrating Light Moisturizer",
            "Nivea Soft Moisturizing Cream"
        ])

    else:
        return random.choice([
            "Neutrogena Hydro Boost Gel",
            "Cetaphil Daily Facial Moisturizer",
            "Minimalist Marula Oil Moisturizer"
        ])

