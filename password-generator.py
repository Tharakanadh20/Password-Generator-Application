import string
import random
from csv import writer


def passgen():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    # Get platform name
    while True:
        platform = input('Enter the name of the platform: \n').strip()
        if platform:
            break
        else:
            print("Platform name cannot be empty. Please enter a valid name.")

    # Get password length
    while True:
        try:
            pass_length = int(input("Enter the length of the password: \n "))
            if pass_length < 6:  # Minimum length check for security reasons
                print(
                    "Password length should be at least 6 characters for security reasons.")
            else:
                break
        except ValueError:
            print("Please enter a valid positive integer for the password length.")

    # Generate password
    s = list(s1 + s2 + s3 + s4)
    random.shuffle(s)

    # Ensure password contains at least one character from each character set
    password = random.choice(s1) + random.choice(s2) + \
        random.choice(s3) + random.choice(s4)
    password += "".join(random.choices(s, k=pass_length - 4))

    # Shuffle the final password
    password = ''.join(random.sample(password, len(password)))

    print("Generated Password: ", password)

    passdata = [platform, password]

    try:
        # Specify the file path directly
        file_path = r"D:\Projects\Password Generator Application\Platforms.csv"

        # Write to CSV
        with open(file_path, 'a', newline='') as d:
            writedata = writer(d)
            writedata.writerow(passdata)
        print("Password saved successfully.")
    except PermissionError:
        print(
            f"Permission denied: Unable to write to {file_path}. Please check your permissions or try a different directory.")
    except FileNotFoundError:
        print(
            f"File not found: The path {file_path} does not exist. Please check the directory path.")
    except Exception as e:
        print(f"An error occurred: {e}")


passgen()
