#Get user input
initial = int(input("Enter initial investment\n"))
rate = float(input("Enter intrest rate\n"))

#Convert rate to percent
rate = rate / 100


double = initial * 2
count = 0 


while initial <= double:
    #calculate intrest
    intrest = initial * rate

    #add intrest to initial
    initial += intrest

    #increment count
    count += 1


print('Your investment took ' + str(count) + ' years to double')