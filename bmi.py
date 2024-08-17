def BMI_cal(weight,height):
    return weight / (height ** 2)
def BMI_cat(bmi):
    if bmi<18.5:
        return "under weight"
    elif 18.5>=bmi<24.9:
        return "normal weight"
    elif 24.9>=bmi<29.9:
        return "overweight"
    else:
        return "obese"

def main():
    weight=int(input("Enter weight in KG:"))
    height=float(input("Enter height in Meter:"))

    bmi=BMI_cal(weight,height)
    cat=BMI_cat(bmi)

    print(f"your BMI is {bmi:.2f}.catogory:{cat}")

if __name__=="__main__":
    main()
