print("Welcome to BMI Calculator")

height = float(input("Enter your height in Meters:\n"))
weight = float(input("Enter your Weight in Kilograms:\n"))

bmi = (weight / (height ** 2))

print("Your BMI(Body Mass Indes) is:\n" + str(round(bmi)))