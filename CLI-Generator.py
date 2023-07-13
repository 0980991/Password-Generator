import argparse
from Classes import PasswordGenerator as Gen


def getNewPassword(length, chartypes):
    # Debug
    print(f"PW length: {length}")
    print(f"Character Mode: {chartypes}")

    # Func Body
    Gen(int(length), int(chartypes))


if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="ge")
    chartypes_desc = "\n1. lowercase only\n2. UPPERCASE ONLY\n3. UPPERCASE And lowercase\n4. Numb3r5 only\n5. UPPER, lower and numb3r5\n6. UPPER, lower and $pec!al characters\n7. UPPER, lower, $pec!al and numb3rs\n"
    # Add the arguments you need
    parser.add_argument("--len", "-l",  help="The number of characters the password should be")
    parser.add_argument("--chartypes", "-ct", help=f"Which types of characters should be used in the pasword. \n {chartypes_desc}")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call your function with the provided arguments
    getNewPassword(args.len, args.chartypes)
