# Zachary Dahir
# Assignment 5.1
#7-08-21

#get user input
miles = float(input("Enter miles\n"))

def milesToKm (x):    

    #convert miles to km
    km = x * 1.609

    #output miles and km
    print(str(x) + ' miles is equal to ' + str(round(km, 2)) + ' kilometers')

#call function
milesToKm(miles)