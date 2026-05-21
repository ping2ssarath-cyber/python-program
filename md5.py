MD5
import hashlib
 
text = "SecureData123"
 
hashed = hashlib.md5(text.encode()).hexdigest()
 
print(f"[+] MD5 Hash: {hashed}")
