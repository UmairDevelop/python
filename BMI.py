name = input("Enter name:\n")
age = input("Enter age:\n")
height = input("Enter height in feet:\n")
weight = input("Enter weight in kg:\n")

height_meters = float(height) * 0.3048
bmi = float(weight) / (height_meters ** 2)
print(f"{name}, your BMI is {bmi:.2f}")