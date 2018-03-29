#calculate the salary of a staff which consist of the following rules
#basic salary = 14000000
#overtime bonus = number of overtime (hrs) times 100.000
#attendance bonus
    #full attendance = plus 5%
    #days of absence = number of days absent *25000

#Data:
    #Overtime = 18 hrs
    #days of absence = 3


def salary(overtime, absence):
    basic_salary = 14000000
    overtime_bonus = overtime * 100000
    absent = absence * 25000
    if absence == 0:
        new_salary = basic_salary + int((5/100)*basic_salary) + overtime_bonus
        return new_salary
    else:
        new_salary = basic_salary + overtime_bonus - absent
        return new_salary

print(salary(18, 3))
