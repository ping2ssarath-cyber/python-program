import hashlib
text = "SecureData123"
# Generate an un-reversable SHA-256 hash string
hashed = hashlib.sha256(text.encode()).hexdigest()
print(f"[+] SHA-256 Hash: {hashed}")
