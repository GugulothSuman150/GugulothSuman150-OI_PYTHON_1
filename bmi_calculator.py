def calculate_bmi(weight, height):
    return weight / (height ** 2)

def main():
    print("Welcome to the BMI Calculator!")
    
    try:
        weight = float(input("Please enter your weight in kilograms: "))
        height = float(input("Please enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return
        
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")
        
        if bmi < 18.5:
            print("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            print("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")
    
    except ValueError:
        print("Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()
