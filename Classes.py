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
        choice = input()
        self.ClearTerminal()

        while choice not in range(1-4):
            self.ClearTerminal()
            if choice == "1":
                PasswordManager()
                break

            if choice == "2":
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

            else:
                input("Please try something else...")
                time.sleep(2)
                GUI()

    def ClearTerminal(self):
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
        self.minMax2 = []
        self.minMax3 = []
        self.SelectRange()

    def SelectRange(self):
        if self.charType == 1:
            self.minMax.extend([97, 122])  # these parameters represent the decimal range from a - z lowercase letters
            self.Generate()
            print(self.password)

        elif self.charType == 2:
            self.minMax.extend([65, 90])  # these parameters represent the decimal range from A - Z uppercase letters
            self.Generate()

        elif self.charType == 3:
            self.minMax2.extend([(65, 90), (97, 122)])  # these parameters represent the decimal range from A - z (Upper & Lower)
            self.Generate2()

        elif self.charType == 4:
            self.minMax3.extend([(48, 57), (65, 90), (97, 122)])  # these parameters represent the decimal range from 0 - A - z (Upper, lower and numbers)
            self.Generate3()

        elif self.charType == 5:
            self.minMax2.extend([(33, 47), (58, 176)])  # these parameters represent the decimal range from upper lower and special chars
            self.Generate2()

        elif self.charType == 6:
            self.minMax.extend([33, 176])  # these parameters represent the decimal range of (essentially) all ascii characters
            self.Generate()

        self.ClearTerminal()
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