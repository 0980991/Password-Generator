import json
import random
import os
import time


class GUI:
     def __init__(self):
        print("Password Generator 6900\n" + (15 * "_"))
        print("What would you like to do today?\n" + (15 * "_") +
              "\n1. Open password manager\n2. Generate new password\n3. Quit")
        choice = input()
        ClearTerminal()

        while choice not in range(1-4):
            ClearTerminal()
            if choice == "1":
                PasswordManager()
                break

            if choice == "2":
                length = int(input("How many characters would you like your password to be?\n"))
                charTypes = 0
                while charTypes not in range(1, 7):
                    #ClearTerminal()
                    charTypes = int(input("Which characters would you like to have in your password?\n" + (15 * "_") +
                            "\n1. lowercase only\n"
                            "2. UPPERCASE ONLY\n"
                            "3. UPPERCASE And lowercase\n"
                            "4. UPPER, lower and numb3rs\n"
                            "5. UPPER, lower and $pec!al characters\n"
                            "6. UPPER, lower, $pec!al and numb3rs\n"))
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
        self.minMax = []
        self.MinMax2 = []
        self.MinMax3 = []
        self.SelectRange()

    def SelectRange(self):
        if self.charType == 1:
            self.minMax.extend([97, 122])
            self.Generate()
            print(self.password)

        elif self.charType == 2:
            self.minMax.extend([65, 90])
            self.Generate()

        elif self.charType == 3:
            self.MinMax2.extend([65, 90], [97, 122])
            self.Generate2()

        elif self.charType == 4:
            self.MinMax3.extend([(48, 57), (65, 90), (97, 122)])
            self.Generate3()

        elif self.charType == 5:
            self.MinMax2.extend([33, 47], [58, 176])
            self.Generate2()

        elif self.charType == 6:
            self.minMax.extend([33, 176])
            self.Generate()

    def Generate(self): # Generates pw based on 1 range of ascii values
        for i in range(self.length):
            self.password += chr(random.randint(self.minMax[0], self.minMax[1]))
        input(f"Your password is {self.password}")

    def Generate2(self): # Generates pw based on 2 ranges of ascii values
        for i in range(self.length):
            self.password += chr(random.randint(*random.choice(self.MinMax2)))
        input(f"Your password is {self.password}")

    def Generate3(self): # Generates pw based on 3 ranges of ascii values
        for i in range(self.length):
            self.password += chr(random.randint(*random.choice(self.MinMax2)))
        input(f"Your password is {self.password}")

gui = GUI()