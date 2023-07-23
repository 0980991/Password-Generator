import secrets
import random
import os
import time
import json
import bcrypt
from cryptography.fernet import Fernet

# A generator that always combines upper&lowercase as well as numbers and characters.
# Implements makes use of python secrets instead of random
# TODO: Add a complexity parameter which determins how many special characters & numbers are used.
class PasswordGenerator:
    def __init__(self):
        self.password = ""
        self.all_ranges = [
                            [97, 122],
                            [65, 90],
                            [48, 57],
                            ["!", "@","#", "$", "%", "^", "&", "*",
                             "(", ")" , "_", "-", "\"", "\'", "\\"]
                        ]

    def generate(self, length):
        for i in range(length):
            i_range = secrets.randbelow(len(self.all_ranges))
            if i_range == 3:
                self.password += secrets.choice(self.all_ranges[i_range])
            else:
                self.password += chr(secrets.randbelow(self.all_ranges[i_range][1] - self.all_ranges[i_range][0] + 1) + self.all_ranges[i_range][0])
        # print(self.password)
        return self.password


class PasswordManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.key       = self.genKey()

    def setMasterPassword(self, master_password):
        self.master_password = master_password.encode('utf-8')

    def genKey(self):
        return Fernet.generate_key()

    def encrypt(self, password):
        fernet = Fernet(self.key)
        password_bytes = password.encode('utf-8')
        encrypted_password = fernet.encrypt(password_bytes)
        return encrypted_password

    def decrypt(self, encrypted_password):
        fernet = Fernet(self.key)
        password_bytes = fernet.decrypt(encrypted_password)
        password = password_bytes.decode('utf-8')
        return password

    def hashPassword(self, unhashed_password, salt_rounds):
        # salt_rounds can be in-or-decreased to hash a pw faster and less secure or slower and more secure (4-20 recommended)
        salt = bcrypt.gensalt(rounds=salt_rounds)
        hashed_password = bcrypt.hashpw(unhashed_password.encode('utf-8'), salt)
        print(hashed_password)
        return hashed_password

    def storePassword(self, obscured_password):
        with open(self.file_name, 'ab') as file:
            file.write(obscured_password + b'\n')

    def readPasswords(self):
        try:
            with open(self.file_name, 'r') as file:
                lines = file.readlines()
                lines = [line.strip() for line in lines]  # Remove leading/trailing whitespace and newlines
                return lines
        except FileNotFoundError:
            print(f"File not found: {self.file_name}")
            return []
        except Exception as e:
            print(f"Error reading file: {e}")
            return []






class GUI:

    def __init__(self):
        print("Password Generator 6900\n" + (15 * "_"))
        print("What would you like to do today?\n" + (15 * "_") +
              "\n1. Open password manager\n2. Generate new password\n3. Quit")
        self.choice = input()
        self.ClearTerminal()
        self.isLoggedIn = False

        while self.choice not in range(1-4):
            self.ClearTerminal()
            if self.choice == "1":
                pW = ""
                while pW != "password" and self.isLoggedIn:
                    pW = input("Please enter the correct password:\n")
                isLoggedIn = True
                self.choice = input("What would you like to do?\n" + (15 * "_") +
                                    "\n1. Show all passwords"
                                    "\n2. Search for a password\n")
                GUIPasswordManager(self.choice)

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


# Deprecated password generator which allows the user to generate a password with any combination of characters.
class oldPasswordGenerator:
    def __init__(self, length, charType):
        # Ascii values of text/symbols
        self.a_lowercase_range    = [97, 122]
        self.a_uppercase_range    = [65, 90]
        self.a_numbers_range      = [48, 57]
        self.a_special_chars      = ["!", "@","#", "$", "%", "^", "&", "*",
                                     "(", ")" , "_", "-", "\"", "\'", "\\"]


        self.password = ""
        self.length = length
        self.charType = charType
        self.minMax = []
        self.minMax2 = []
        self.minMax3 = []
        self.SelectRange()

    def SelectRange(self):
        # TODO This spaghetti logic needs an overhaul!
        isGenerating = True
        while isGenerating:
            self.password = ''
            if self.charType == 1:
                self.minMax.extend(self.a_lowercase_range)  # these parameters represent the decimal range from a - z lowercase letters
                self.Generate()
                print(self.password)

            elif self.charType == 2:
                self.minMax.extend(self.a_uppercase_range)
                self.Generate()
                #self.verifyPassword()

            elif self.charType == 3:
                self.minMax2.extend([self.a_lowercase_range,
                                     self.a_uppercase_range])
                self.Generate2()

            elif self.charType == 4:
                self.minMax.extend(self.a_numbers_range)
                self.Generate()

            elif self.charType == 5:
                self.minMax3.extend([self.a_lowercase_range,
                                     self.a_uppercase_range,
                                     self.a_numbers_range])
                self.Generate3()

            elif self.charType == 6:
                self.minMax3.extend([self.a_lowercase_range,
                                     self.a_uppercase_range,
                                     (0, len(self.a_special_chars))])
                self.Generate3()

            elif self.charType == 7:
                self.minMax.extend([33, 126])  # these parameters represent the decimal range of (essentially) all ascii characters
                self.Generate()

            #if not self.verifyPasswordCriteria():
                #continue


            # os.system("cls")
            choice = input(f"Your password is {self.password}\n\n Generate again? (y/N)")
            if choice not in ('Y', 'y'):
                isGenerating = False

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
                               (0, len(self.minMax3[2]))])

            self.password += chr(random.randint(r[0], r[1]))

    def verifyPasswordCriteria(self):
        lowercaseFlag = False
        uppercaseFlag = False
        numberFlag    = False
        characterFlag = False

        for char in self.password:
            lowercaseFlag = chr(char) in range(self.a_lowercase_range)
            uppercaseFlag = chr(char) in range(self.a_uppercase_range)
            characterFlag = chr(char) in range(self.a_special_char_range)
            numberFlag    = chr(char) in range(self.a_numbers_range)

# Deprecated password manager class
class GUIPasswordManager:
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
