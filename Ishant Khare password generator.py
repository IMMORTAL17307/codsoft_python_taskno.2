import random
import string

def run_password_generator():
    print("--- Password Generator ---")
    
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Error: Length must be a positive number.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a whole number.")
        return

    print("Choose complexity level:")
    print("  1. Low (Lowercase letters only)")
    print("  2. Medium (Letters and numbers)")
    print("  3. High (Letters, numbers, and symbols)")
    complexity = input("Enter choice (1, 2, or 3): ").strip()

    if complexity == '1':
        character_set = string.ascii_lowercase
    elif complexity == '2':
        character_set = string.ascii_letters + string.digits
    elif complexity == '3':
        character_set = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid choice. Defaulting to High complexity.")
        character_set = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(character_set)

    print("------------------------------------------")
    print("Generated Password:", password)
    print("------------------------------------------")

if __name__ == "__main__":
    while True:
        run_password_generator()
        print()
        again = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if again != "yes" and again != "y":
            print("Goodbye!")
            break
        print()
