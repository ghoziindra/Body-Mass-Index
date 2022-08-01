weight = float(input("Please Enter your Weight: "))
height = float(input("Please Enter your Height: "))

BMI = weight / (height/100)**2

if BMI <= 18.4:
    print("You are Under weight.")
elif BMI <= 24.9:
    print("You are Healthy.")
elif BMI <= 29.9:
    print("You are Over weight.")
elif BMI <= 34.9:
    print("You are Severely Over weight.")
elif BMI <= 39.9:
    print("You are Obese.")
else:
    print("You are Obese.")


print(f"Your BMI is {BMI}")