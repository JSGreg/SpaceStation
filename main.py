import requests
import json



def main ():
    userInput = input('What do you want to know? (Number, People)')
    userInput = userInput.lower()

    # Filters invalid responses
    if not userInput == "number" and not userInput == "people":
        return print("Invalid Input")
    
    # API call    
    response = requests.get("http://api.open-notify.org/astros.json")
    response = response.text
    #turns response into a dictionary
    dict_object = json.loads(response)

    if userInput == "people":
        
        userInput2=input("Do you want names?(Y/N)")
        userInput2 = userInput2.lower()
        
        if userInput2 == "y":
            nameStr = "name"
            x = 0
            for number in dict_object[userInput]:
                
                print(dict_object[userInput][x][nameStr])
                x=x+1
        return

    # prints requested infomation
    print(dict_object[userInput])

main()