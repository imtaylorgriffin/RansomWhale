from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import base64

# Generate RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Get the public key
public_key = private_key.public_key()

# Serialize the private key in PEM format
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Serialize the public key in PEM format
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Encode the public key in Base64
public_key_base64 = base64.b64encode(public_key_pem)

# Print the Base64-encoded public key
print(public_key_base64.decode())

# Save the private key to a file
with open('private_key.pem', 'wb') as private_key_file:
    private_key_file.write(private_key_pem)

# Save the public key to a file
with open('public_key.pem', 'wb') as public_key_file:
    public_key_file.write(public_key_pem)

print("Private and public keys generated and saved.")
