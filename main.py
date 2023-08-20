import requests
import json
from webbrowser import open
from sys import argv

# Could sperate into different functions?
# Could also ask where coords? http://api.open-notify.org/iss-now.json

def main():
    # API call    
    response = requests.get("http://api.open-notify.org/astros.json")
    response = response.text
    
    #turns response into a dictionary
    dict_object = json.loads(response)

    nameStr = "name"
    craftStr = "craft"
    
    while True:
        try: 
            print("Who is in space?")
            userInput = input('What do you want to know? (Number/People)')
            userInput = userInput.lower()

            if userInput == "people":
                for info in dict_object[userInput]:
                    print("\n", info[nameStr], "who is on the", info[craftStr])
        
            elif userInput == "number":
                print("There are currently", dict_object[userInput], "people in space.")
            else:
                raise KeyError ("Invalid Input")
            
            
            userInput2 = input('Do you want to know where the ISS is? (Y/N)')
            userInput = userInput.lower()
            
            if userInput2 == "y":
                map()
            elif userInput2 == "n":
                break
            else:
                raise KeyError("Invalid Input")
            break
                    
        except KeyError: 
            print("Invalid Input")

    return

def map():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response = response.text
    dict_object = json.loads(response)
    
    address = dict_object["iss_position"]["latitude"]
    address = address + " " + dict_object["iss_position"]["longitude"]
    

    open("http://www.google.com/maps/place/"+ address)
    return

main()