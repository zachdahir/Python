'''
Zach Dahir
Assignment 2.1
6-17-21
'''


print ("Welcome to the Fiber Optic Cost Calculator!")

#Get user input
companyName = input("Enter company name \n")
cableLength = input("Enter number of feet of cable to be installed \n")

#change cableLength from string to int
cableLength = int(cableLength) 

#if statements to set price based on length
if cableLength > 500:
    pricePerFoot = .50

elif cableLength > 250:
    pricePerFoot = .70

elif cableLength > 100:
    pricePerFoot = .80

else:
    pricePerFoot = .87 


#Calculate total
total = float(cableLength) * float(pricePerFoot)

#Convert total to round number
total = round(total, 2)

#Display company and total
print(companyName + " your total will be $", total)