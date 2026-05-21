 
import socket
 
s = socket.socket()
 
s.settimeout(5)
 
status = s.connect_ex(("127.0.0.1", 80))
 
if status == 0:
	print("[+] Port 80 is OPEN")
 
else:
	print("[-] Port 80 is CLOSED")
	print(f"Error Code : {status}")
 
	if status == 10061:
        print("Reason 	: Connection Refused")
 
	elif status == 10060:
        print("Reason 	: Connection Timed Out")
 
	elif status == 10035:
        print("Reason 	: Operation Would Block")
 
	else:
        print("Reason 	: Unknown")
