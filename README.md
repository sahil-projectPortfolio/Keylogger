# keylogger

Keyloggers are programs that capture your key strokes.
They can be used to keep logs of everything you press on the keyboard but on the 
flip side it can be used for malicious purposes as well.

It is a keylogger with basic functionality as the ones available in market today.
It captures your keystrokes and saves them in a file "keylogger.txt".

It then sends the contents of the file(i.e. the keystrokes) to your email id.

SYNTAX : python keylogger.py

[NOTE: You need to press esc key to exit out the keylogger.]

You need to have pynput , smtplib and ssl installed.

While python comes with the library smtplib and ssl preinstalled.
You can install pynput with :
pip install pynput


