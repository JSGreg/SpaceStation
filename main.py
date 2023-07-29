import requests
import json

# Could sperate into different functions?
# Could also ask where coords? http://api.open-notify.org/iss-now.json


def main ():
    # API call    
    response = requests.get("http://api.open-notify.org/astros.json")
    response = response.text
    
    #turns response into a dictionary
    dict_object = json.loads(response)
    
    while True:
        try: 
            userInput = input('What do you want to know? (Number, People)')
            userInput = userInput.lower()

            # Filters invalid responses
            # if not userInput == "number" and not userInput == "people":
            #     print("Invalid Input")
                

            if userInput == "people":
                userInput2=input("Do you want names?(Y/N)")
                userInput2 = userInput2.lower()
                if userInput2 == "y":
                    nameStr = "name"
            
                    x = 0
                    for number in dict_object[userInput]:
                        print(dict_object[userInput][x][nameStr])
                    x=x+1
                elif userInput2 == "n":
                    print ("No data.")
                     
                    
            
            # prints requested infomation
            # print(dict_object[userInput])
            break
        except KeyError: 
            print("Invalid Input")
    


    return

    

main()