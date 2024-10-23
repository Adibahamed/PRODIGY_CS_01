# Function to apply Caesar Cipher encryption
def encryptMessage(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result
def decryptMessage(text, shift):
    return encryptMessage(text, -shift)
def cipherProgram():
    while True:
        choice = input("Type 'E' to encrypt, 'D' to decrypt, or 'Q' to quit: ").upper()
        if choice == 'Q':
            print("Exiting the  cipher program.")
            break  
        elif choice in ['E', 'D']:
            message = input("Enter your message: ")
            shiftValue = int(input("Enter the shift number: "))
            if choice == 'E':
                print(f"Encrypted Message: {encryptMessage(message, shiftValue)}")
            else:
                print(f"Decrypted Message: {decryptMessage(message, shiftValue)}")
        else:
            print("Invalid choice, please type 'E', 'D', or 'Q'.")
if __name__ == "__main__":
    cipherProgram()
