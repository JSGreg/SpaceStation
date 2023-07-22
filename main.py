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
    #turns into a dictionary
    response=response.text

    dict_object = json.loads(response)

    print(dict_object[userInput])

main()