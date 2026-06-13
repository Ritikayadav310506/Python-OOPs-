# Program to give weather-based recommendations

weather = input("Enter weather condition (Sunny/Rainy/Cold): ").lower()

if weather == "sunny":
    print("Output: Wear sunglasses ")
elif weather == "rainy":
    print("Output: Carry an umbrella ")
elif weather == "cold":
    print("Output: Wear a jacket ")
else:
    print("Output: Unknown weather condition.")
