hotels = [
    {"name": "Nile Ritz", "rating": 4.8, "city": "Cairo", "available": True},
    {"name": "Four Seasons", "rating": 4.9, "city": "Cairo", "available": False},
    {"name": "Steigenberger", "rating": 4.2,
        "city": "Alexandria", "available": True},
    {"name": "Kempinski", "rating": 3.8, "city": "Cairo", "available": True},
    {"name": "Marriott", "rating": 4.5, "city": "Alexandria", "available": False},
]


names = [hotel["name"] for hotel in hotels]
print((names))


for hotel in hotels:
    if hotel["city"] == "Cairo" and hotel["available"]:
        print(hotel)

ratings = [hotel["rating"] for hotel in hotels]
highest_rating = max(ratings)
for hotel in hotels:
    if hotel["rating"] == highest_rating:
        print(f"Highest rated: {hotel['name']} with {highest_rating}")


for hotel in hotels:
    if hotel["rating"] >= 4.5:
        hotel["price_category"] = "Luxury"
    else:
        hotel["price_category"] = "standard"

print(hotels)
