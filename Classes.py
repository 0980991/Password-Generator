import random
import os
import time
import json
import functools as ft


class GUI:

    def __init__(self):
        print("Password Generator 6900\n" + (15 * "_"))
        print("What would you like to do today?\n" + (15 * "_") +
              "\n1. Open password manager\n2. Generate new password\n3. Quit")
        self.choice = input()
        self.ClearTerminal()

        while self.choice not in range(1-4):
            self.ClearTerminal()
            if self.choice == "1":
                pW = ""
                while pW != "password":
                    pW = input("Please enter the correct password:\n")

                self.choice = input("What would you like to do?\n" + (15 * "_") +
                                    "\n1. Show all passwords"
                                    "\n2. Search for a password\n")
                PasswordManager(self.choice)

            if self.choice == "2":
                self.SetPwParameters()
                GUI()

    def SetPwParameters(self):
        length = int(input("How many characters would you like your password to be?\n"))
        charTypes = 0
        while charTypes not in range(1, 7):
            # ClearTerminal()
            charTypes = int(input("Which characters would you like to have in your password?\n" + (15 * "_") +
                                    "\n1. lowercase only\n"
                                    "2. UPPERCASE ONLY\n"
                                    "3. UPPERCASE And lowercase\n"
                                    "4. UPPER, lower and numb3rs\n"
                                    "5. UPPER, lower and $pec!al characters\n"
                                    "6. UPPER, lower, $pec!al and numb3rs\n"))

            PasswordGenerator(length, charTypes)

        GUI()

    def ClearTerminal(self):
        os.system("cls")


class PasswordManager:
    def __init__(self, choice):
        self.userData = json.load(open("userData.json"))

        if choice == 1:
            self.GetInfo()

        elif choice == 2:
            self.Search()

        elif choice == 3:
            GUI.SetPwParameters()

        elif choice == 4:
            self.Logout()

    def GetInfo(self):
        for site in self.userData:
            print(15 * "-" + "\n"
                  f'Site: {site["site"]}\n'
                  f'Password: {site["password"]} ')

    def Search(self):
        while True:
            os.system("cls")
            searchChoice = input("===============================\n"
                                 "Please enter your search query?\n"
                                 "-------------------------------\n")

            flag = True
            while flag:
                output = ""
                i = 0
                while i < len(self.userData):
                    if searchChoice == self.userData[i]["site"]:
                        output += "\n" + str(self.userData[i])
                    i += 1
                if output != "":
                    print(f"{output}")
                    input()
                    flag = False
                else:
                    print("No items found matching your query. Check for spelling errors or adjust your query type.")
                    time.sleep(5)
                input("Press enter to continue...........")

    def Logout():
        GUI()


class PasswordGenerator:
    def __init__(self, length, charType):
        self.password = ""
        self.length = length
        self.charType = charType
        self.minMax = []
        self.minMax2 = []
        self.minMax3 = []
        self.SelectRange()

    def SelectRange(self):
        if self.charType == 1:
            self.minMax.extend([97, 122])  # these parameters represent the decimal range from a - z lowercase letters
            self.Generate()
            print(self.password)

        elif self.charType == 2:
            self.minMax.extend([65, 90])
            self.Generate()

        elif self.charType == 3:
            self.minMax2.extend([(65, 90),
                                 (97, 122)])
            self.Generate2()

        elif self.charType == 4:
            self.minMax3.extend([(48, 57),
                                 (65, 90),
                                 (97, 122)])
            self.Generate3()

        elif self.charType == 5:
            self.minMax2.extend([(33, 47),
                                (58, 176)])
            self.Generate2()

        elif self.charType == 6:
            self.minMax.extend([33, 176])  # these parameters represent the decimal range of (essentially) all ascii characters
            self.Generate()

        os.system("cls")
        input(f"Your password is {self.password}")

    def Generate(self):  # Generates pw based on 1 range of ascii values
        for i in range(self.length):
            self.password += chr(random.randint(self.minMax[0], self.minMax[1]))

    def Generate2(self):  # Generates pw based on 2 ranges of ascii values
        for _ in range(self.length):
            r = random.choice([(self.minMax2[0][0], self.minMax2[0][1]),
                               (self.minMax2[1][0], self.minMax2[1][1])])

            self.password += chr(random.randint(r[0], r[1]))

    def Generate3(self):  # Generates pw based on 3 ranges of ascii values
        for i in range(self.length):
            r = random.choice([(self.minMax3[0][0], self.minMax3[0][1]),
                               (self.minMax3[1][0], self.minMax3[1][1]),
                               (self.minMax3[2][0], self.minMax3[2][1])])

            self.password += chr(random.randint(r[0], r[1]))


gui = GUI()
# pwManager = PasswordManager(1)
