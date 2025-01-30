from Crypto.PublicKey import RSA

def generate_key_pair():
    # Generate key pair using 2048 bits
    key = RSA.generate(2048)
    # Export private key to a variable
    private_key = key.export_key()
    # Export public key to a variable
    public_key = key.publickey().export_key()

    # Write private key to a file
    with open("private_key.pem", "wb") as f:
        f.write(private_key)
    # Write public key to a file
    with open("public_key.pem", "wb") as f:
        f.write(public_key)

if __name__ == "__main__":
    # Call generate function
    generate_key_pair()
    # Print confirmation once function has ran successfully
    print("Key pair generated and saved.")