height = float(input("Enter a height in cm"))
weight = float(input("Enter a weight in kg"))
BMI = weight/ (height/100)**2
print("ypur Bmi is" , BMI)
if BMI <= 18.4:
   print("your are unederweight")
elif BMI <= 24.9:
      print("You are healthy")
elif BMI <=34.9:
     print("you are severely overweight")
else :
     print(" ypu are severely obese")