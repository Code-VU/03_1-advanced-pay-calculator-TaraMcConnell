def calculatePay():
    # This first line is provided for you



    try:
        hours = input("Enter hours: ")
        hours = float(hours)

    except:
        hours = input("Error, please enter numeric input: ")
        hours = float(hours)   

    try:
        hourly_rate = input("Enter rate: ")
        hourly_rate = float(hourly_rate)
    
    except:
        hourly_rate = input("Error, please enter numeric input: ")
        hourly_rate = float(hourly_rate)

    

    if hours > 40: 
        #logic that reads overtime
        overtime_hours = hours - 40 
        normal_hours = 40

        overtime_pay = overtime_hours * hourly_rate * 1.5
        normal_pay = normal_hours * hourly_rate

        gross_pay = normal_pay + overtime_pay
    else:
        #the usual
        gross_pay = hours * hourly_rate

    print(f"Pay: {gross_pay}")


    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
