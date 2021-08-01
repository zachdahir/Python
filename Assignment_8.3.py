#Zachary Dahir
#Assignment 8.3
#7-28-21

import requests, json

def main():
    apiKey = '25a8bf00b11974c7afaa326f12cea38c'

    #Select search method for api
    dataType = input('Select search method: \n [1] Zipcode \n [2] City \n')

    def veiwLocation():
        if dataType == str(1):
            #get zipcode
            zip = input('Please enter 5 digit zipcode: \n')

            if len(str(zip)) == 5:
                #call api
                url = 'http://api.openweathermap.org/data/2.5/weather?zip=' + zip + '&appid=' + apiKey

                #store response in var and print data
                response = requests.get(url)
                weatherData = response.json()
                print(weatherData)
        
            else:
                print('Invalid zipcode')
                veiwLocation()

        elif dataType == str(2):
            #get city name
            city = input('Please enter city name:\n')

            #call api
            url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city +  '&appid=' + apiKey

            #store response in var and print data
            response = requests.get(url)
            weatherData = response.json()
            print(weatherData)

        else:
            print('Invalid input')
            veiwLocation()
            
    veiwLocation()

    #ask user if the want to run program again
    runAgain = input('Would you like to veiw another location? Yes or No? \n')

    #if they enter yes call main
    if runAgain == 'Yes' or runAgain == 'yes':
        main()

    else:
        print('Goodbye!')

main()