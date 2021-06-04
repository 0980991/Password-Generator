import json
import random


class GUI:

    def __init__(self):
        print("Password Generator 6900\n" + (15 * "_"))
        print("What would you like to do today?\n" + (15 * "_") + "\n1.Open password manager\n2.Generate new password\n3. Quit")
        choice = input()
              
        while choice not in range(1-4):
            if choice == "1":
                PasswordManager()
                break
            if choice == "2":
                PasswordGenerator()
                break


class PasswordManager:
    
    def __init__(self): 
        self.userData = json.load(open("userData.json"))
        for username in self.userData:
            print(type(self.username))
            print(type(self.userData))

                                 
class PasswordGenerator:
    
    def Generate(self):
        password = ""
        length = input("How many characters would you like your password to be?")
        for i in length:
            password += ord(random.randint(x=97, y=122))
        print(password)

                

gui = GUI()