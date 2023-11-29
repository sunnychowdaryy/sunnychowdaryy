import random
import string

def generate_password(length=12):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure at least one character from each category
    password = (
        random.choice(lowercase_letters)
        + random.choice(uppercase_letters)
        + random.choice(digits)
        + random.choice(special_characters)
    )

    # Generate remaining charactersr
    password += ''.join(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the password to enhance randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

def generate_multiple_passwords(num_passwords, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

def main():
    print("Welcome to Secure Password Generator!")
    print("------------------------------------")
    print("This tool will generate strong passwords for you.")

    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            password_length = int(input("Enter the length of each password: "))
            generated_passwords = generate_multiple_passwords(num_passwords, password_length)

            print("\nGenerated Passwords:")
            for idx, password in enumerate(generated_passwords, start=1):
                print(f"Password {idx}: {password}")
            break
        except ValueError:
            print("Please enter valid numerical values.")

if __name__ == "__main__":
    main()
