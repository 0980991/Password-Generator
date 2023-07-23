from Classes import PasswordGenerator as Gen, PasswordManager as Man
import time

# Record the start time
start_time = time.time()

MANAGER = Man(".secrets")
GENERATOR = Gen()
# GENERATOR.key = b'Wu6xJdRXs2he57vue7tXZTSW0JCBYCYpZ0OcmGsWHJc='
test = 2
if test == 1:
    for i in range(10):
        GENERATOR.password = ""
        pw = "Hello World"
        MANAGER.storePassword(pw)
    passwords = MANAGER.readPasswords()
    for password in passwords:
        print(pw)

elif test == 2:
    for i in range(10):
        GENERATOR.password = ""
        e_pw = MANAGER.encrypt("Hello World")
        MANAGER.storePassword(e_pw)
    passwords = MANAGER.readPasswords()
    for password in passwords:
        pw = MANAGER.decrypt(password)
        print(pw)


# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the result
print(f"Elapsed time: {elapsed_time:.4f} seconds")