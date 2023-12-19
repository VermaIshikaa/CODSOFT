import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length > 0:
                return length
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("Password Generator\n")
    
    password_length = get_password_length()
    generated_password = generate_password(password_length)

    print(f"\nGenerated Password: {generated_password}")

if __name__ == "__main__":
    main()
