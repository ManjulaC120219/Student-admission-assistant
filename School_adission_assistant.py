import datetime
from datetime import date
print("                               Welcome to Sri Chaitanya Techno School")
age=None
grade=None
grade1=None

for i in range(0,2):
    query = input("would you like to join to our school: ").upper()
    if query == "YES":
        grade1 = input("Would you like to join LKG/Pre-nursery: ").upper()
        print("Age limit for Pre_Nursery: 2.6 years - 3.9 years ")
        print("Age limit for LKG: 3.10 years - 4.10 years")
        for i in range(0,2):
            try:
                date_entry = input("enter the age in YYYY-MM-DD format")
                year, month, day = map(int, date_entry.split('-'))
                date = datetime.date(year, month, day)
                print("entered date is: ",date)
                date_format = '%Y-%m-%d'
                date_obj = datetime.datetime.strptime(str(date), date_format)
                currentDate = date.today()
                print("todays date", currentDate)
                days_in_year = 365.2425
                age = float((currentDate - date).days / days_in_year)
                print("the child age is: ", round(age, 1), "years")
                break
            except ValueError:
                print("Incorrect data format, should be YYYY-MM-DD")

        if age <= 2.5:
            print("your kids is not eligible to get admission")
        elif age <= 4.10 and age >= 3.10:
            print("your kid is eligible for LKG")
            grade = input("do you want to join?: ").upper()
        elif age >= 2.6 and age <= 3.9:
            print("your kid is eligble for Pre - nursery")
            grade = input("do tou want to join?: ").upper()
        elif age >= 6.0:
            print("Sorry your kid is neither eligible for LKG nor eligible for Pre-nursery, since kid's age is, {0}, Thanks for visiting our Website".format(round(age,1)))
            break
        if age < 6 and age >4.10 and (grade1 =="LKG" or grade1 =="PRE-NURSERY"):
                print("your kid age falls under special category, kindly contact admin department")
                break
        if grade == "YES" and age <= 4.10 and age >= 3.10:
            def lkg(admission_fee,tution_fee):
                total = admission_fee+tution_fee
                return total
            fee =lkg(30000,90000)
            print("The total fee is:", fee)
            break
        elif grade == "YES" and age >= 2.6 and age <= 3.9:
            program=input("do you want your kid to maverick/starkids program?: ").upper()
            if program=="MAVERICK":
                def maverick(admission_fee,tution_fee):
                    total = admission_fee+tution_fee
                    return total
                fee = maverick(30000,80000)
                print("The fee for Maverick program is: ",fee)
            elif program=="STARKIDS":
                def starkids(admission_fee,tution_fee):
                    total = admission_fee+tution_fee
                    return total
                fee = starkids(30000,55000)
                print("The fee for Maverick program is: ",fee)
            break
        else:print("Thanks for visiting our Website")

    elif query=="NO":
        print("Thanks for vising our Website")
        break
    elif i == 1:
        print("Thanks for visiting our Website")
    else:print("Please enter the proper response")
