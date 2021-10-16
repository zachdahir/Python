# Zachary Dahir
# Assignment 6.1
#7-12-21

def addVehicle():
    print("""Select Vehicle type: 
            1: Car
            2: Pickup""")

    vehicleType = input()

    if vehicleType == 1:
        print('You have selected a car \n')
        make = input('Enter vehicle make: \n')
        model = input('Enter vehicle model: \n')
        color = input('Enter vehicle color: \n')
        fuelType = input('Enter vehicle fuel type: \n')
        engineSize = input('Enter vehicle engine size: \n')
        numDoors = input('Enter vehicles number of doors: \n')
        options = getOptions()

        make = Car(make, model, color, fuelType, engineSize, numDoors, options)

        cars.append(make)

    elif vehicleType == 2:
        print('You have selected a pickup \n')
        make = input('Enter vehicle make: \n')
        model = input('Enter vehicle model: \n')
        color = input('Enter vehicle color: \n')
        fuelType = input('Enter vehicle fuel type: \n')
        cabStyle = input('Enter cab style: \n')
        bedLength = input('Enter bed length: \n')
        options = getOptions()

        make = Pickup(make, model, color, fuelType, cabStyle, bedLength, options)

        pickups.append(make)

    else:
        print("Invalid option, please enter 1 for Car or 2 for Pickup")


class Vehicle: 
    def __init__(self, make, model, color, fuelType, options):
        self.make = make
        self.model = model
        self.color = color
        self.fueltype = fuelType
        self.options = options

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def getFuelType(self):
        return self.fueltype

    def getOptions(self):
        return self.options
        
class Car(Vehicle):
    def __init__(self, make, model, color, fuelType, options, engineSize, numDoors):
        self.engineSize = engineSize
        self.numDoors = numDoors

    def getEngineSize(self):
        return self.engineSize

    def getNumDoors(self):
        return self.numDoors
    
class Pickup(Vehicle):
    def __init__(self, make, model, color, fuelType, options, cabStyle, bedLength):
        self.cabStyle = cabStyle
        self.bedLength = bedLength

    def getCabStyle(self):
        return self.cabStyle

    def getBedLength(self):
        return self.bedLength
        

cars = []
pickups = []

def getOptions():
    options = ['Bluetooth', 'Navigation', 'Cruise Control', 'All Wheel Drive', 'Power Windows', 'Satillite Radio', 'Sun Roof', 'Security System']
    selectedOptions = []
    go = 'yes'

    def addChoice(choice):
        newChoice = options[choice]
        selectedOptions.append(newChoice)

    def hideChoice(choice):
        options.pop(choice)

    while (go == 'yes'):
        
        x = 1
        for option in options:
            print('[' + str(x) + '] ' + option)
            x = x + 1

        choice = input('Please select an option \n')
    
        choice = int(choice)
        choice = choice - 1

        addChoice(choice)
        hideChoice(choice)
    
        go = input('If you would like to add another option enter yes, if not enter no \n')
        x = 1
    return selectedOptions

def displayGarage():
    i = 0
    while i < len(cars):
        print(cars[i])
        i += 1

    i = 0
    while  i < len(pickups):
        print(pickups[i])
        i += 1

addVehicle()

displayGarage()