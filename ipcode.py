import socket
target_url = "google.com"
target_ip = socket.gethostbyname(target_url)
print(f"[+] The IP address of {target_url} is {target_ip}")
