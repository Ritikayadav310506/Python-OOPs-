def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

# Example
w = float(input("Enter weight (kg): "))
h = float(input("Enter height (m): "))
bmi, cat = bmi_calculator(w, h)
print(f"BMI: {bmi:.2f}, Category: {cat}")
