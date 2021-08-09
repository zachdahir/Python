#Zachary Dahir
#Assignment 9.1
#8-03-21

import os

path = 'C:/Users/zachd/Desktop/'

directory = input('Enter directory name: \n')

fileName  = input('Enter file name: \n')

#check if directory exists
if os.path.isdir(path + directory): 
    #create file name
    fullFile = os.path.join(path, directory, fileName + '.txt')

    #open file to write to
    editFile = open(fullFile, 'w+')

    name = input('Enter name: \n')
    address = input('Enter Address: \n')
    number = input('Enter phone number: \n')

    #write user input to file
    editFile.write(name + ', ' + address + ' ,' + number)
    editFile.close()

    display = open(fullFile, 'r')
    print(display.read())
    display.close()

#create directory if it does not exist
else:
    os.mkdir(path + directory)

    #create file name
    fullFile = os.path.join(path, directory, fileName + '.txt')    

    #open file to write to
    editFile = open(fullFile, 'w+')
    name = input('Enter name: \n')
    address = input('Enter Address: \n')
    number = input('Enter phone number: \n')
    print(fullFile)

    #write user input to file
    editFile.write(name + ', ' + address + ' ,' + number)
    editFile.close()

    display = open(fullFile, 'r')
    print(display.read())
    display.close()

