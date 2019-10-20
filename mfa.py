#!/usr/bin/python3
##
## Script to generate OTP based on base32 MFA secret key
##
import pyotp
import time
import sys
import os
from termcolor import colored,cprint
os.system('clear')
key = input("Enter base32 secret key: ")
#print("Generating OTP for key:" + key)
cprint('\nNew OTP will be generated every 30 Seconds. Press Ctrl+C to exit', 'red')
print('')
totp = pyotp.TOTP(key)
OTP=totp.now()
print("Current OTP is: " + OTP)
print('')
while True:
  try:
    while totp.verify(OTP):
      pass
  except KeyboardInterrupt:
    print("Bye!")
    sys.exit()
  else:
    OTP=totp.now()
    print("Current OTP is: " + OTP)
    print('\n')
##EOF
