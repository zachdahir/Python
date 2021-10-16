#Zachary Dahir
#Assignment 7.1
#7/25/2021

#Function to add vehicle to garage
def addVehicle():
    go = 'yes'
    while go == str('yes'):
        print("""Select Vehicle type: 
            1: Car
            2: Pickup \n""")

        vehicleType = input()

        if vehicleType == str(1):
            print('You have selected a car \n')
            make = input('Enter vehicle make: \n')
            xxx = make
            model = input('Enter vehicle model: \n')
            color = input('Enter vehicle color: \n')
            fuelType = input('Enter vehicle fuel type: \n')
            engineSize = input('Enter vehicle engine size: \n')
            numDoors = input('Enter vehicles number of doors: \n')
            options = selectOptions()

            xxx = Car(make, model, color, fuelType, options, engineSize, numDoors)

            cars.append(xxx)

        elif vehicleType == str(2):
            print('You have selected a pickup \n')
            make = input('Enter vehicle make: \n')
            xxx = make
            model = input('Enter vehicle model: \n')
            color = input('Enter vehicle color: \n')
            fuelType = input('Enter vehicle fuel type: \n')
            cabStyle = input('Enter cab style: \n')
            bedLength = input('Enter bed length: \n')
            options = selectOptions()
            
            xxx = make = Pickup(make, model, color, fuelType, options, cabStyle, bedLength)

            pickups.append(xxx)

        else:
            print("Invalid option, please enter 1 for Car or 2 for Pickup")

        go = input('If you would like to add another car enter yes, otherwise hit enter')

#Vehicle class
class Vehicle(): 
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

#car class child of vehicle      
class Car(Vehicle):
    def __init__(self, make, model, color, fuelType, options, engineSize, numDoors):
        self.engineSize = engineSize
        self.numDoors = numDoors

        super().__init__(make, model, color, fuelType, options)

    def getEngineSize(self):
        return self.engineSize

    def getNumDoors(self):
        return self.numDoors

    
#pickup class child of vehicle
class Pickup(Vehicle):
    def __init__(self, make, model, color, fuelType, options, cabStyle, bedLength):
        self.cabStyle = cabStyle
        self.bedLength = bedLength

        super().__init__(make, model, color, fuelType, options)

    def getCabStyle(self):
        return self.cabStyle

    def getBedLength(self):
        return self.bedLength
        
# empty lists to use for garage
cars = []
pickups = []

#function to get selected options
def selectOptions():
    options = ['Bluetooth', 'Navigation', 'Cruise Control', 'All Wheel Drive', 'Power Windows', 'Satillite Radio', 'Sun Roof', 'Security System']
    selectedOptions = []
    go = 'yes'

    def addChoice(choice):
        newChoice = options[choice]
        selectedOptions.append(newChoice)

    def hideChoice(choice):
        options.pop(choice)

    while (go == 'yes'):
        print('---Please select an option---')
        x = 1
        for option in options:
            print('[' + str(x) + '] ' + option)
            x = x + 1
        
        choice = input()
        choice = int(choice)
        choice = choice - 1

        addChoice(choice)
        hideChoice(choice)
    
        go = input('If you would like to add another option enter yes, otherwise hit enter \n')
        x = 1
    return selectedOptions

#function to display vehicles in garage
def displayGarage():
    for x in range(len(cars)):
        print("--- Car --- ")
        print("Make: " + cars[x].make)
        print("Model: " + cars[x].model)
        print("Color: " + cars[x].color)
        print("Engine Size: " + cars[x].engineSize)
        print('Number of Doors: ' + cars[x].numDoors)
        print('Accessories: ' + str(cars[x].options))

    for x in range(len(pickups)):
        print("--- Pickup --- ")
        print("Make: " + pickups[x].make)
        print("Model: " + pickups[x].model)
        print("Color: " + pickups[x].color)
        print("Engine Size: " + pickups[x].cabStyle)
        print('Number of Doors: ' + pickups[x].bedLength)
        print('Accessories: ' + str(pickups[x].options))
       
addVehicle()

#if statement to ensure that there is atleast one pickup and car in garage
if len(cars) < 1:
    print('Please add at least one car to your garage')
    addVehicle()

elif len(pickups) < 1:
    print('Please add at least one pickup to your garage')
    addVehicle()

displayGarage()
