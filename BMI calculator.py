#BMI Calculator
#Nupur Kirwai
# taking inputs from the user 
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters:"))
the_BMI = weight / (height/100)**2  
# calculating and displaying the BMI  
print("Your Body Mass Index is: ", the_BMI)  
# using the if-elif-else conditions  
if the_BMI <= 18:  
    print("You are Underweight.")  
elif the_BMI <= 25:  
    print("You are healthy.")  
elif the_BMI <= 30:  
    print("You are Overweight.")  
else:  
    print("Obesity.") 
