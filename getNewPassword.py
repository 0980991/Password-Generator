import argparse
from Classes import PasswordGenerator as Gen


def getNewPassword(length):
    # Func Body
    Gen(int(length))


if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="ge")
    # Add the arguments you need
    parser.add_argument("--len", "-l",  help="The number of characters the password should be")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call your function with the provided arguments
    getNewPassword(args.len)
