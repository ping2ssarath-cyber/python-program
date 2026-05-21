import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# =========================
# SMTP Email Sender Script
# =========================

# Sender email credentials
smtp_server = "smtp.gmail.com"
smtp_port = 587

sender_email = "ping2sksarath@gmail.com"
password = "bpcu lpfd arxn iumn"   # Use App Password for Gmail

# Receiver email
receiver_email = "vikas07@gmail.com"

# Email content
subject = "Test Email from Python SMTP"
body = """
Hello,

This is a test email sent using Python SMTP.

Regards,
Python Script
"""

# Create message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach body
message.attach(MIMEText(body, "plain"))

try:
    # Connect to SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection

    # Login to email account
    server.login(sender_email, password)

    # Send email
    server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully!")

except Exception as e:
    print("Error:", e)

finally:
    server.quit()
