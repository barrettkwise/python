height = float(input("Please enter your height in inches."))
weight = float(input("Please enter your weight in pounds."))
metersHeight = height * 0.0254
kilosWeight = weight * 0.45359
bmi = kilosWeight / (metersHeight * metersHeight)
print(f"Your bmi is {bmi}.")

if bmi > 25:
    print("You need to lose some weight.")
if bmi < 20:
    print("You need to gain some weight.")
if 25 < bmi < 20:
    print("Your are a healthy bmi.")
