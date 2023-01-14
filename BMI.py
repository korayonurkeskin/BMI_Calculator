"""Body Mass Index Calculator, classifies your weight status!"""

WEIGHT = float(input("What is your weight (in kilograms): "))
HEIGHT = float(input("What is your height (in meters): "))

BMI = WEIGHT / (HEIGHT * HEIGHT)

if BMI <= 18.4:
    print("You are UNDERWEIGHT! Your BMI:", BMI)
elif BMI <= 24.9:
    print("You are NORMAL! Your BMI:", BMI)
elif BMI <= 39.9:
    print("You are OVERWEIGHT! Your BMI:", BMI)
else:
    print("You are OBESE! Your BMI:", BMI)