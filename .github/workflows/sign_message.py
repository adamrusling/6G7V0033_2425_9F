from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import sys

def sign_message(message, private_key_file):
    # Read the private key file
    with open(private_key_file, "rb") as f:
        private_key = f.read()

    # Import the private key and assign to variable
    key = RSA.import_key(private_key)
    # Hash a given message using SHA256
    h = SHA256.new(message.encode())

    # Create the signature of the hashed message and return the value
    signature = pkcs1_15.new(key).sign(h)
    return signature

if __name__ == "__main__":
    # Check if correct number of arguments are given
    if len(sys.argv) != 3:
        print("Usage: python sign_message.py <message> <private_key_file>")
        sys.exit(1)

    message_to_sign = sys.argv[1]
    private_key_file = sys.argv[2]

    # Pass all variables into sign_message function to perform operation
    signature = sign_message(message_to_sign, private_key_file)
    # Print the hex value of the signature
    print(f"Signature (hex): {signature.hex()}")