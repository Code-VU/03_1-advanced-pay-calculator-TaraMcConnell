def calculatePay():
    # This first line is provided for you
    try:
        Enter_hours: 20
        Enter_rate: nine
    except: NameError:
    print("Error, please enter numeric input")


    hours = input("Enter Hours: ")
    hours = float(hours)

    hourly_rate = input("Enter Rate: ")
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
