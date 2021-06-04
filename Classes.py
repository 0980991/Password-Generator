import json
import random
import os
import time


class GUI:
     def __init__(self):
        print("Password Generator 6900\n" + (15 * "_"))
        print("What would you like to do today?\n" + (15 * "_") + "\n1.Open password manager\n2.Generate new password\n3. Quit")
        choice = input()
        ClearTerminal()

        while choice not in range(1-4):
            ClearTerminal()
            if choice == "1":
                PasswordManager()
                break

            if choice == "2":
                length = input("How many characters would you like your password to be?")
                charTypes = input("Which characters would you like to have in your password?"
                          "1. lowercase only"
                          "2. UPPERCASE ONLY"
                          "3. UPPERCASE And lowercase"
                          "4. UPPER, lower and numb3rs"
                          "5. UPPER, lower and $pec!al characters"
                          "6. UPPER, lower, $pec!al and numb3rs")
                PasswordGenerator(length, charTypes)

            else:
                input("Please try something else...")
                time.sleep(2)
                GUI()

def ClearTerminal():
    os.system("cls")



class PasswordManager:
    def __init__(self):
        self.userData = json.load(open("userData.json"))
        for username in self.userData:
            print(type(self.username))
            print(type(self.userData))


class PasswordGenerator:
    def __init__(self, length, charType):
        self.password = ""
        self.length = length
        self.charType = charType
        self.min = 0
        self.max = 0
        self.Generate()

    def Generate(self):
        if self.charType == "1":
            self.min = 97
            self.max = 122
            self.SelectRange()
            print(self.password)

        elif self.charType == "2":
            self.min = 65
            self.max = 90
            self.SelectRange()

    def SelectRange(self):
        for i in range(int(self.length)):
            self.password += chr(random.randint(self.min, self.max))
        input(f"Your password is {self.password}")






gui = GUI()