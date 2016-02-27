yearsalary = 0;
OneTimeBonus = 0;
monthlysalary = 0;

yearsalary = input("Please enter your yaersalary" )
oneTimBbonus = input("Please enter your oneTimeBonus" )

monthlysalary = ((int(yearsalary) + int(OneTimeBonus))/12)

print() 

print("This is your monthly salary using int values: " + format(monthlysalary))
#Extra credit
print("Your monthly salary will be $%.2f" % monthlysalary) 

