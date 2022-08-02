temperature = 59
forecast = "rainy"
"""if temperature > 80:
    print("It's too hot to go outside today.")
elif temperature < 50:
    print("It's too cold to go outside today.")"""
if temperature > 80 or temperature < 55:
    print("Don't go outside.")
else:
    print("You can go outside today.")
if forecast == "rainy" and temperature < 65:
    print("Just another day in Washington.")
if forecast == "sunny" and temperature < 65:
    print("Don't be fooled by the sun, it's just another day in Washington.")
