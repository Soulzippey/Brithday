import utils, random

dict = {
    "Billy Joe": "09/15/1945",
    "Kenny Ko": "12/21/1998",
    "Martins Licis": "06/28/1990"
}
Go = 1
print("Welcome to the birthday dictionary. We know the birthdays of:")
print(dict.keys())
name = ""
while Go == 1:
    name = input("Who's birthday do you want to look up?  ") 
    name = name.lower()
    if (name == "billy joe"):
        print(dict["Billy Joe"])
        break
    else:
        if (name == "kenny ko"):
            print(dict["Kenny Ko"])
            break
        else:
            print(dict["Martins Licis"])
        break
        
