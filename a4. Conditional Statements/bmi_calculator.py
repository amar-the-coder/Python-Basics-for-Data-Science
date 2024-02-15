weight = float(input("enter weight in kg: "))
height = float(input("enter the height in meter: "))

bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi} & you are underweight ")
elif bmi < 25:
    print(f"your BMI is {bmi} & you are normal weight ")
elif bmi < 30:
    print(f"your BMI is {bmi} & you are overweight ")
elif bmi < 35:
    print(f"your BMI is {bmi} & you are obese ")
else:
    print(f"your BMI is {bmi} & you are clinically obese")
