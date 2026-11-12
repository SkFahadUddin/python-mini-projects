"""A simple substitution cipher for learning purposes (not secure encryption)."""

import random
import string


CHARACTERS = " " + string.punctuation + string.ascii_letters + string.digits


def make_key():
    """Create one shuffled character mapping for this program session."""
    shuffled = list(CHARACTERS)
    random.shuffle(shuffled)
    return shuffled


def encrypt(message, key):
    encrypted = []
    for char in message:
        if char in CHARACTERS:
            encrypted.append(key[CHARACTERS.index(char)])
        else:
            # Keep characters outside the cipher alphabet, such as emoji, unchanged.
            encrypted.append(char)
    return "".join(encrypted)


def decrypt(message, key):
    decrypted = []
    for char in message:
        if char in key:
            decrypted.append(CHARACTERS[key.index(char)])
        else:
            decrypted.append(char)
    return "".join(decrypted)


def main():
    key = make_key()
    print("=== Substitution Cipher ===")
    print("This is a learning example, not secure encryption.")
    print("The key changes each time you run the program.\n")

    while True:
        print("1. Encrypt text")
        print("2. Decrypt text from this session")
        print("3. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            message = input("Enter text to encrypt: ")
            print("Encrypted text:", encrypt(message, key))
        elif choice == "2":
            message = input("Enter text to decrypt: ")
            print("Decrypted text:", decrypt(message, key))
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, or 3.")
        print()


if __name__ == "__main__":
    main()
